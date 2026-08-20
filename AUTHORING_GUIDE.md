# 论文技术路线网站维护指南

本文档规定本仓库的内容组织、目录层级、命名方式和新增论文流程。目标是让每个页面围绕一个研究问题组织多篇相互关联的论文，而不是简单地“一篇论文对应一个孤立页面”。

## 1. 核心组织原则

### 1.1 一个主题主页面可以包含多篇论文

一个主题主页面对应一个研究问题或一组存在继承、对比、互补关系的论文。例如：

- 主题：从一段人类视频到灵巧机器人
- 论文：Human2Sim2Robot、Video2Sim2Real
- 主题主页面：`01-human-video-to-robot.html`

主题页需要解释论文之间的关系，包括：

1. 它们解决的共同问题；
2. 后续工作继承了什么；
3. 两篇论文在哪些设计选择上存在分歧；
4. 技术路线如何演进；
5. 哪些结论有实验支持；
6. 仍有哪些共同局限。

### 1.2 单篇页面是补充材料，不是主要入口

如果某篇论文需要展示更细的公式、观测空间、动作空间或完整训练流程，可以在主题目录的 `papers/` 下增加单篇扩展页。用户首先进入主题主页面，再按需打开单篇扩展页。

### 1.3 论文 PDF 与网页内容分层保存

公开论文 PDF 放入主题目录的 `sources/`，不与 HTML 混放。主题专属图片、视频或数据可以放入可选的 `media/` 目录。

## 2. 标准目录结构

```text
robot_paper_routes/
├── index.html                                  # 全站研究主题目录
├── AUTHORING_GUIDE.md                          # 本维护指南
├── README.md                                   # 使用和运行说明
├── scripts/
│   └── validate_site.py                        # 目录与链接验证脚本
├── assets/
│   ├── styles.css                              # 全站共享样式
│   └── app.js                                  # 全站共享交互
└── topics/
    ├── 01-human-video-to-robot/
    │   ├── 01-human-video-to-robot.html         # 主题主页面
    │   ├── papers/
    │   │   ├── human2sim2robot.html             # 单篇扩展页
    │   │   └── video2sim2real.html              # 单篇扩展页
    │   ├── sources/
    │   │   ├── Human2Sim2Robot.pdf
    │   │   └── Video2Sim2Real.pdf
    │   └── media/                               # 可选：主题专属图像/视频
    └── 02-next-topic/
        ├── 02-next-topic.html
        ├── papers/
        ├── sources/
        └── media/
```

## 3. 命名规范

### 3.1 主题目录

格式：

```text
两位数字编号-英文主题短名
```

示例：

```text
01-human-video-to-robot
02-vision-language-action
03-tactile-dexterous-manipulation
```

规则：

- 编号固定使用两位数字：`01`、`02`、`03`；
- 英文短名全部小写；
- 单词之间使用连字符 `-`；
- 不使用空格、中文、下划线或日期；
- 主题名要表达研究问题，不要只写某篇论文名。

### 3.2 主题主页面

主题主页面文件名必须与主题目录名完全一致：

```text
topics/01-human-video-to-robot/01-human-video-to-robot.html
```

不要在主题目录中使用通用的 `index.html`，这样从文件路径即可判断页面属于哪个主题。

### 3.3 单篇扩展页

单篇扩展页使用论文项目名的英文小写形式：

```text
papers/human2sim2robot.html
papers/video2sim2real.html
```

### 3.4 原始论文

论文 PDF 放入 `sources/`。使用稳定、可读的英文名称：

```text
sources/Human2Sim2Robot.pdf
sources/Video2Sim2Real.pdf
```

不要使用 `paper.pdf`、`final.pdf` 或带下载随机编号的文件名。

## 4. 主题主页面的推荐内容结构

每个主题主页面建议包含以下部分：

1. **Hero / 主题问题**：用一句话定义该组论文共同回答的问题；
2. **论文关系**：说明继承、对比、互补或技术演进；
3. **并行技术路线**：把多篇论文的输入、抽象、学习、迁移和输出并排展示；
4. **关键机制**：解释真正决定方法差异的模块或目标函数；
5. **对照表**：按照监督、策略学习、动作生成、迁移和泛化范围比较；
6. **实验证据**：列出直接支持方法主张的指标、表格或消融结果；
7. **边界与局限**：明确适用范围和未解决问题；
8. **论文入口**：链接本地 PDF、官方项目页、代码和可选的单篇扩展页。

页面中应区分：

- `论文事实`：论文原文明确陈述的方法、数据、指标或限制；
- `结构化解读`：为了说明论文关系而进行的归纳或推断。

实验指标必须注明是作者报告结果，不得表述为独立复现结论。

## 5. 新论文到来时如何判断放在哪里

先回答以下问题：

1. 新论文是否与某个现有主题回答同一个核心研究问题？
2. 它与现有论文之间是否存在直接继承、对比、替代或互补关系？
3. 把它放入现有主题后，是否仍能用一个清晰标题概括全部论文？

如果三个问题大多为“是”，加入现有主题。如果核心问题已经发生变化，应创建新主题目录。

## 6. 向现有主题加入论文

以 `01-human-video-to-robot` 为例：

1. 下载正式论文 PDF 到：

   ```text
   topics/01-human-video-to-robot/sources/NewPaper.pdf
   ```

2. 阅读论文并提取：输入、感知模块、中间表示、训练目标、动作空间、sim-to-real 方法、实验指标和限制；
3. 更新主题主页面 `01-human-video-to-robot.html`：
   - 在论文关系中加入新论文；
   - 将两列路线改为三列或其他合适结构；
   - 更新对照表和研究演进结论；
   - 更新首页卡片中的论文数量；
4. 如需深度讲解，在 `papers/` 新增 `new-paper.html`；
5. 在主题主页面加入 PDF、项目页、代码和扩展页链接；
6. 运行验证脚本并本地浏览检查。

向现有主题加入论文时，不需要在根目录 `index.html` 新建主题卡片，只需要更新原主题卡片的论文数量和摘要。

## 7. 创建新的论文主题

假设要创建 `02-vision-language-action`：

1. 创建目录：

   ```text
   topics/02-vision-language-action/
   topics/02-vision-language-action/papers/
   topics/02-vision-language-action/sources/
   topics/02-vision-language-action/media/
   ```

2. 创建同名主题主页面：

   ```text
   topics/02-vision-language-action/02-vision-language-action.html
   ```

3. 复用 `assets/styles.css` 和 `assets/app.js`；
4. 按第 4 节结构整理该组论文的关系和技术路线；
5. 在根目录 `index.html` 增加一张主题卡片，链接到：

   ```text
   topics/02-vision-language-action/02-vision-language-action.html
   ```

6. 下载论文到该主题的 `sources/`，需要时增加 `papers/` 扩展页；
7. 运行验证脚本和本地服务器。

## 8. 相对链接规则

### 根目录首页

```html
<link rel="stylesheet" href="assets/styles.css">
<a href="topics/01-human-video-to-robot/01-human-video-to-robot.html">...</a>
<script src="assets/app.js"></script>
```

### 主题主页面

```html
<link rel="stylesheet" href="../../assets/styles.css">
<a href="../../index.html">返回主题目录</a>
<a href="papers/human2sim2robot.html">单篇扩展页</a>
<a href="sources/Human2Sim2Robot.pdf">论文 PDF</a>
<script src="../../assets/app.js"></script>
```

### 单篇扩展页

```html
<link rel="stylesheet" href="../../../assets/styles.css">
<a href="../01-human-video-to-robot.html">返回合并主题页</a>
<a href="../sources/Human2Sim2Robot.pdf">论文 PDF</a>
<script src="../../../assets/app.js"></script>
```

不要使用本机绝对路径、`file://` 地址或只在开发电脑上有效的链接。

## 9. 验证与本地预览

在 `robot_paper_routes/` 目录运行：

```bash
python3 scripts/validate_site.py
python3 -m http.server 8000
```

浏览：

```text
http://localhost:8000/
http://localhost:8000/topics/01-human-video-to-robot/01-human-video-to-robot.html
```

发布前必须确认：

- 根目录只有一个站点入口 `index.html`；
- 每个主题目录都有一个与目录同名的主题主页面；
- 所有本地 HTML、CSS、JS、PDF 和锚点链接有效；
- 页面在桌面和窄屏下均无明显溢出；
- 论文事实、结构化解读和作者报告指标标记清楚；
- 不存在 `TODO`、`FIXME` 或占位文本。

## 10. 使用 Git 命令更新 GitHub

本仓库远程地址为：

```text
https://github.com/wangst0181/robot-paper
```

以下流程适用于修改主题页面、增加论文、调整样式或更新维护文档。

### 10.1 修改前先同步远程分支

进入本地仓库并确认当前分支：

```bash
cd "/Users/siting/Desktop/化学具身/robot_paper_routes"
git branch --show-current
git status --short
```

在工作区没有未提交修改时，同步远程 `main`：

```bash
git pull --ff-only origin main
```

正常情况下当前分支应为 `main`。如果 `git status --short` 已经显示文件，不要立即执行 pull；先确认这些修改是否需要保留。

### 10.2 修改后先验证页面

```bash
python3 scripts/validate_site.py
python3 -m http.server 8000
```

在浏览器检查：

```text
http://localhost:8000/
```

检查结束后，在运行服务器的终端按 `Ctrl+C` 停止服务。

### 10.3 检查本次修改范围

```bash
git status --short
git diff
```

确认输出中只有本次任务相关文件。不要使用 `git add .` 或 `git add -A`，避免把临时文件或无关修改一起提交。

### 10.4 精确暂存文件

如果只修改了当前主题主页面：

```bash
git add -- topics/01-human-video-to-robot/01-human-video-to-robot.html
```

如果同时修改主题页、首页和样式：

```bash
git add -- \
  index.html \
  assets/styles.css \
  topics/01-human-video-to-robot/01-human-video-to-robot.html
```

如果创建了一个完整的新主题，应明确写出该主题目录和首页：

```bash
git add -- \
  index.html \
  topics/02-topic-name/
```

论文 PDF 已被 `.gitignore` 排除，不应提交到 Git 历史。新增论文时，需要在 `.github/workflows/deploy-pages.yml` 的下载步骤中增加对应 arXiv PDF 下载命令，并把该工作流文件一起暂存。

### 10.5 提交前检查暂存区

```bash
git diff --cached --stat
git diff --cached
```

如果暂存了错误文件，可以在提交前取消暂存，不会删除本地修改：

```bash
git restore --staged -- 路径/文件名
```

### 10.6 创建提交并推送

提交信息应简短说明修改目的：

```bash
git commit -m "Update human video to robot topic"
git push origin main
```

常用提交信息示例：

```text
Add a new paper to human video topic
Create tactile manipulation topic
Update shared page styles
Fix GitHub Pages deployment
Update authoring guide
```

### 10.7 查看 GitHub Pages 部署

每次推送到 `main` 都会触发 `.github/workflows/deploy-pages.yml`。可以打开：

```text
https://github.com/wangst0181/robot-paper/actions
```

如果已登录 GitHub CLI，也可以运行：

```bash
gh run list --repo wangst0181/robot-paper --limit 5
```

等待最新的 `Deploy research pages` 工作流变为绿色后，再检查线上页面。

### 10.8 常见 Git 问题

#### `nothing to commit, working tree clean`

没有新的修改需要提交，或修改尚未保存。运行 `git status --short` 检查。

#### `non-fast-forward` 或 push 被拒绝

远程分支存在本地没有的更新。不要强制推送。先运行：

```bash
git status --short
git pull --rebase origin main
git push origin main
```

如果 rebase 出现冲突，停止继续推送，先检查冲突文件。

#### Pages 工作流失败在 `Configure GitHub Pages`

进入仓库：

```text
Settings → Pages → Build and deployment → Source → GitHub Actions
```

首次发布必须手动选择一次 GitHub Actions。工作流中的 `actions/configure-pages@v5` 不应设置 `enablement: true`，因为默认 `GITHUB_TOKEN` 无权首次创建 Pages 站点。

## 11. GitHub Pages 发布路径

当前仓库名为 `robot-paper`：

```text
主题总目录：
https://wangst0181.github.io/robot-paper/

本主题页面：
https://wangst0181.github.io/robot-paper/topics/01-human-video-to-robot/01-human-video-to-robot.html
```

后续新增主题不会改变已有主题链接。
