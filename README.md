# Human2Sim2Robot & Video2Sim2Real 技术路线展示

双击 `index.html` 即可离线浏览；也可以在本目录运行：

```bash
python3 -m http.server 8000
```

然后访问 <http://localhost:8000/>。

目录内容：

```text
robot_paper_routes/
├── index.html                              # 研究主题总目录
├── AUTHORING_GUIDE.md                      # 新增论文与主题的维护指南
├── assets/
│   ├── styles.css                          # 全站共享样式
│   └── app.js                              # 全站共享交互
├── scripts/
│   └── validate_site.py                    # 目录与链接验证
└── topics/
    └── 01-human-video-to-robot/
        ├── 01-human-video-to-robot.html     # 本次可直接分享的合并主题页
        ├── papers/
        │   ├── human2sim2robot.html         # 单篇扩展页
        │   └── video2sim2real.html          # 单篇扩展页
        └── sources/
            ├── Human2Sim2Robot.pdf          # 原始论文
            └── Video2Sim2Real.pdf           # 原始论文
```

页面内容依据论文公开版本整理。页面中的实验指标均为作者报告结果，不代表独立复现。

后续新增相关论文组时，在 `topics/` 下创建 `02-topic-name/`、`03-topic-name/` 等独立目录，并创建与目录同名的主题 HTML。完整操作流程见 [`AUTHORING_GUIDE.md`](AUTHORING_GUIDE.md)。

每次修改后运行：

```bash
python3 scripts/validate_site.py
```

## GitHub Pages 发布

仓库通过 `.github/workflows/deploy-pages.yml` 自动部署。每次推送到 `main` 后，工作流会：

1. 从 arXiv 下载两份公开论文 PDF；
2. 运行站点验证脚本；
3. 构建并发布 GitHub Pages。

PDF 保存在本地工作目录并会进入部署产物，但通过 `.gitignore` 排除在 Git 历史之外，避免仓库因论文文件持续膨胀。
