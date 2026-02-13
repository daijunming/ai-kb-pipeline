# ai-kb-pipeline

面向知识提炼与交付重组的 AI-native 流水线骨架仓库。

## 设计目标

本工程围绕四个工程特征构建：

- 中间表示稳定
- 可检索复用
- 可评测回归
- 可观测可追责

## 六层架构

1. **资料与中间产物层**：原文输入 + 结构化中间产物（segments/evidence/concepts/claims/...）。
2. **提示词工序层**：每个提示词是可版本化算子，依赖明确 schema。
3. **检索与记忆层**：全文索引 + 向量索引，优先复用概念口径与证据资产。
4. **流水线编排层**：统一 runner，支持单 stage 与全链路，输出 manifest。
5. **评测回归层**：黄金样本 + 指标脚本，变更模型/提示词后可自动对比。
6. **开发者体验层**：VS Code tasks 一键运行，便于持续迭代。

## 快速开始

```bash
python -m kb_pipeline.cli run
python -m kb_pipeline.cli stage --name segment
python -m kb_pipeline.cli eval
```

## 目录

请参考仓库目录结构，重点目录包括：

- `configs/`：运行、存储与评测配置
- `prompts/`：提示词算子注册与分 stage 提示词
- `schemas/`：结构化输出契约
- `src/kb_pipeline/`：pipeline 代码主体
- `data/fixtures/`：回归黄金样本
- `data/runs/`：每次运行归档结果与 manifest
