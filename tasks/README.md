# 候选任务与维护清单

唯一状态源：[candidates.json](candidates.json)。核验日期 2026-11-07。排序是工程建议，不是获奖概率。

| ID | 候选 | 推荐理由 | 主要成本/风险 | 下一步 |
|---|---|---|---|---|
| LAD-001 | Trace | 首题首选：当前新题、难度1、CANN9.0 | 跨步Gather、FP32归约、确定性、非方阵/Inf/NaN；不等于简单夺冠 | 选题确认后拿正式题包 |
| LAD-002 | ConfusionMulGrad | 第二备选：新题、难度2 | 双输出、多方向归约、共享输入复用，复杂度较高 | 比较题包与VT能力 |
| LAD-003 | MseLoss | none/mean/sum归约练习 | 跨月题需突破历史最佳；题面曾有溢出描述问题，不能无条件照抄 | 查榜单，不以奖励为目标 |
| COM-001 | 社区任务资格核验 | 正式设计评审→交付路线 | 旧任务书可能已结题，不能拿天梯资格替代认领 | 读当月任务及回复 |
| UP-001 | VDN基础NPU支持 | 你与VT已有共同成果，可形成真实上游增量 | TP/WebUI/基础适配依赖混杂，性能未复验 | 固定SHA并拆分审计 |
| UP-002 | Hunyuan3D 2mv/2.1 | 已有验证脚本，研究增量 | 许可、官方已有2.0、目标归属未定 | 对比已有实现 |
| DOC-001 | 官方文档缺陷 | 可降低贡献初期成本 | 尚无具体缺陷，不能保证积分或快速merge | 找可复现问题再建任务 |

## 维护方法

每次操作后更新 JSON，不另造一张独立状态表：
1. 新增稳定 ID、track、owner（未约定用 null）、source、验收标准。
2. 重新核查官方状态后更新 last_checked，不能只改日期。
3. evidence 记录读到/运行到的事实；计划放 next_action。
4. 缺硬件、题包、认领资格或授权时标 blocked，并列 blockers。
5. submitted 必须填 submission_url；done 要有验收证据，积分仍独立记 reward_status。
6. 改 owner、共享仓写范围、署名先与VT约定；不要替他接任务。
7. 运行 `bash scripts/preflight.sh` 后提交清单变更。

状态：candidate → ready → in_progress → submitted → done；任一步可 blocked/deferred。
不保证线性推进；被拒后保留记录，不覆盖历史证据。

## 本轮建议
同时只推进一题（Trace题包核验）和一个上游审计（VDN）。
社区任务认领与文档修复作为候补，不为拿积分先拆空PR。
后续可追加报名、Judge结果、设计PR、代码PR、到账记录，但不能互相替代。
没有创建后台监控或定时刷新。
