# Cyber-Security-Engineer

## 环境要求

`Python >= 3.8 `


## 依赖项安装

### 一键安装

在项目根目录创建 `requirements.txt` 文件，复制粘贴以下内容：

```text
mkdocs>=1.5.3          # 核心构建工具
mkdocs-material>=9.4.0  # Material主题支持
mkdocs-simple-hooks>=0.1.5 # 导航生成钩子
mkdocs-section-index>=0.3.5 # 章节索引功能
pygments>=2.15.1        # 代码高亮依赖
pymdown-extensions>=10.4.1 # Markdown扩展支持
```

打开命令行，进入项目根目录，执行安装命令：
   
```bash
cd CISSP
pip install -r requirements.txt
```

### 手动安装

```bash
# 核心构建工具
pip install mkdocs>=1.5.3

# 主题与插件
pip install mkdocs-material>=9.4.0
pip install mkdocs-simple-hooks>=0.1.5
pip install mkdocs-section-index>=0.3.5

# 扩展依赖
pip install pygments>=2.15.1
pip install pymdown-extensions>=10.4.1
```

### 验证安装

```bash
mkdocs --version
```

## 本地预览网站

```bash
mkdocs serve
```

## 部署到GitHub Pages

```bash
mkdocs gh-deploy
```

