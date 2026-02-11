from pathlib import Path
import re


def extract_chapter_number(file_or_folder_name):
    """从文件或文件夹名中提取章节号"""
    # 使用正则表达式查找"第 X 章"或"第 XX 章"的数字
    match = re.search(r'第\s*(\d+)\s*章', str(file_or_folder_name))
    if match:
        return int(match.group(1))
    # 如果找不到数字，返回一个很大的数，这样会排在最后
    return float('inf')


def generate_nav(config, **kwargs):
    """自动遍历docs目录生成导航，支持文件夹层级"""
    docs_dir = Path(config["docs_dir"])
    nav = []
    
    # 获取所有一级文件夹，并按其中最小的章节号排序
    folders_with_numbers = []
    for item in docs_dir.iterdir():
        if item.is_dir() and item.name != "img":  # 排除图片文件夹
            # 获取该目录下所有md文件的章节号，取最小值作为该目录的序号
            chapter_nums = []
            for md_file in item.glob("*.md"):
                num = extract_chapter_number(md_file.name)
                if num != float('inf'):
                    chapter_nums.append(num)
            
            # 如果目录中有章节文件，则使用最小章节号排序；否则使用目录名排序
            if chapter_nums:
                min_chapter_num = min(chapter_nums)
                folders_with_numbers.append((min_chapter_num, item.name))
            else:
                # 如果没有找到数字，将其放在最后
                folders_with_numbers.append((float('inf'), item.name))
    
    # 按照章节号排序
    sorted_folders = [folder[1] for folder in sorted(folders_with_numbers, key=lambda x: (x[0], x[1]))]
    
    for folder in sorted_folders:
        folder_path = docs_dir / folder
        if not folder_path.exists():
            continue  # 跳过不存在的文件夹
        
        # 遍历文件夹下的所有md文件，按章节号排序
        files = []
        md_files = list(folder_path.glob("*.md"))
        # 按文件名中的数字排序
        sorted_md_files = sorted(md_files, key=lambda f: extract_chapter_number(f.name))
        
        for md_file in sorted_md_files:
            # 生成相对路径（如 "Coding Language/C.md"）
            rel_path = str(md_file.relative_to(docs_dir)).replace("\\", "/")  # 适配Windows路径
            # 用文件名作为标题（去掉.md）
            title = md_file.stem
            files.append({title: rel_path})
        
        # 将文件夹和文件添加到导航
        nav.append({folder: files})
    
    # 覆盖配置中的nav
    config["nav"] = nav
    

def fix_image_paths(markdown, page, config, files):
    return markdown.replace("../img/", "../../img/")