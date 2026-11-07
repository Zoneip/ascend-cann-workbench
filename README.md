# Ascend / CANN contribution workbench

Zoneip 与 VtLoader 合作贡献的研究、选题和流程工作台。**非官方项目**，不分发权重、第三方仓库副本或私人实验素材。

## 当前主线
1. **天梯赛**：首选 Trace，备选 ConfusionMulGrad；先获取正式题包和报名/队伍证据，不能把PR合入当比赛验收。
2. **社区任务**：先确认认领资格，再设计评审、自验、交付和代码PR；旧任务书不等于仍开放。
3. **VDN上游**：与VT确认分工、固定SHA并审计依赖，分阶段提交真正独立的NPU改动；不把整个混合分支当已审核作品。

## 入口
- [项目规则](AGENTS.md)
- [候选比较与维护方法](tasks/README.md)
- [机器可读任务清单](tasks/candidates.json) — 唯一状态源，7项候选
- [官方流程与来源](docs/official-workflow.md)
- [初始化审查与历史纠正](docs/review-notes.md)
- [可复用操作skill](skills/cann-contribution-ops/SKILL.md)
- [只读预检](scripts/preflight.sh) / [预检实现](scripts/preflight.py) / [回归测试](tests/test_preflight.py)
- [AtomGit同步配置](.github/workflows/mirror.yml)

## 使用
```bash
bash scripts/preflight.sh
python3 -B -m unittest discover -s tests -v
```
Python3标准库即可，无需安装CANN、PyTorch或额外依赖。
每次工作后更新任务JSON的状态、证据、阻塞与下一步；不自动认领/提交，不创建定时任务。

## Skill
名称 `cann-contribution-ops`，完整指令在仓内。
**状态：文件已保存；DSH安装请求被拒，尚未安装。** 后续用户确认安装后再通过宿主安装工具注册。
不把仓内文件存在等同于宿主可调用。

## 仓库与同步
目标GitHub仓： https://github.com/Zoneip/ascend-cann-workbench 。
GitHub公开首次发布已获用户授权；发布验收以远端HEAD与本地一致为准。
AtomGit同步默认关闭，只有配置开关/目标/密钥后才运行。仅main、无force/prune，无定时器；不同步Issue/PR/附件。
具体配置和边界见[官方流程](docs/official-workflow.md)。

## 发布范围
公开文件只包含上面列出的当前入口、工具和来源链接。
旧docs/research、docs/operations、rules、specs保留本地但不进入首次公开提交；其未经核验推断已由当前流程纠正。
forks/repos/models/workspace只保留目录占位，实际内容不发布。
工作台许可证待选择；不替第三方代码或权重重新授权。

## 尚未完成
官方报名/组队/CLA状态核验、题包与NPU测试、社区任务认领、VDN完整diff审计、AtomGit端到端同步、skill宿主安装。
本工作台初始化完成不代表已参赛、获积分、代码合入或模型验证通过。
