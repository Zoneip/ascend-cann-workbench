# 官方流程核验与操作清单

核验日期：2026-11-07。网页会更新；实际投稿前重新读取。没有任务的官方确认，不代报名/认领。

## 来源
- S1 [赛事main README](https://raw.atomgit.com/cann-competition/2026JuneCANNOperatorLadderCompetitiion/raw/main/README.md)：10—11月规则、前三名；不是作品仓里旧的9月冠军制。
- S2 [当前CANNJudge赛场](https://cannjudge.cn/public/ladder_october)：Trace、ConfusionMulGrad、MseLoss均可读题面。
- S3 [赛事报名入口](https://competition.gitcode.com/competition/2057085957316272129/intro)。
- S4 [作品PR指南](https://atomgit.com/cann/cann-ops-competitions/blob/master/01_official/cann-ops-ladder-2026/CONTRIBUTING.md)：账号/实名、CLA、团队目录、PR、/compile。
- S5 [社区任务认领](https://gitcode.com/org/cann/discussions/22)、[流程注意事项](https://atomgit.com/org/cann/discussions/39)。
- S6 [CANN积分任务中心](https://atomgit.com/setting/points?type=growth&task=cann)：需要本人登录读取当前规则。
- S7 [CANNLab手册](https://atomgit.com/cann/infrastructure/blob/master/docs/CANNLab/V2/CANNLab用户手册.md)。
- S8 [VDN上游](https://github.com/OpenVDN/vdn-minimax-h3)、[合作分支](https://github.com/vtloader/vdn-minimax-h3/tree/ascend-npu-a3)。

## 路线A：天梯赛
1. 读取S1/S2/S3，确认活动、合法参赛范围、队伍1—3人及成员身份；保存报名和组队结果，不以按钮文字判断成功。
2. 按S4检查实名/CLA及提交邮箱；协议必须用户本人读签。以当前签署页面/机器人为准。
3. 下载**完整比赛作用域**的题包，记录题目URL、日期、题包hash、可编辑文件、CANN/芯片要求；不套用其他题模板。
4. 在独立分支实现，验证合法输入域、dtype/shape/特殊值、确定性、UB/GM边界；只允许基于规格和硬件的通用优化，不能写死测试用例。
5. Judge前做dry-run；用户授权实际提交后记录提交ID、全用例结果、逐点性能和源码SHA。当前规则每日最多50次，不能靠无效尝试刷次数。
6. 开源作品按主办方确认的月份/算子/团队目录提PR，含源码、README、构建脚本、证据；目录不存在先询问，不自行认定November。
7. 按目标PR提示触发 `/compile`，记录CI、review、merge；比赛排名及赛后泛化验收另行记录。

**冲突**：S1仍写“11/31 17:00”；S2的MseLoss页显示2026/11/30 17:00。分别保留，不宣称主办方已更正S1。奖池表头与60/30/10分配文字也需确认。
新题首月前三分配、跨月历史最佳提升>3%、每月最多三题奖励属于当次赛事规则；不保证当前榜单空缺或易获奖。

## 路线B：社区算子任务
按S5先核当前认领状态；旧任务书不证明仍可参与。
认领确认 → 设计PR审核 → 自验 → 提交交付验收 → 后台测试 → 收到通知后向指定代码仓提PR → 合入后最终审核。
设计、测试、代码PR是不同里程碑；先通过测试可能影响其他人的资格，投入前询问。
需保留任务编号、官方回复、自验报告、逐点性能表、打包约束与验收通知。

## 路线C：VDN联合上游PR
与VT确认仓库访问、贡献归属和独立分工；固定上游/源分支SHA。
按依赖审计基础NPU、卸载、并行、WebUI；文件分类统计不是可直接删除模块的依据。
首个PR应可独立构建与验收，保留原作者与真实co-author。CUDA/NPU回归、精度、端到端计时分别说明。
分支文档中的3.85倍是特定配置去噪阶段报告，不是本次复验或所有输入加速保证。
共享fork权限与跨仓PR能力要实测；无写权限才考虑个人fork，不能替VT授权。
上游无CONTRIBUTING时询问维护者，不从已有open PR推断接受承诺。

## 联合PR、积分与署名
前序账户页“非竞赛仓PR合入”指南明确写PR作者获5000分；有效参赛指南只写竞赛仓PR合入计1000且不叠加前者。
**未核实**：co-author领取规则、联合PR分摊、每人每PR上限、转赠、参赛资格是否要求个人PR记录。
因此不能承诺“各开一个都拿分”，也不能认定co-author能替代资格。
团队先约定真实分工、署名、谁回复review；奖励归属问主办方并保留答复。
同一PR review修正通常更新原分支；真正独立功能可拆PR，不为积分重复提交。
VDN的GitHub PR没有已知自动发CANN积分的依据。

## 操作安全
不用官方教程中的全局身份修改/删除fork/裸force作为默认命令。使用repo-local身份、独立分支、正常同步；已发布历史改写需确认，必要时用force-with-lease。
密码、PAT、Cookie不写进仓库或聊天；报名、CLA、付费/卡时启停均由本人确认。

## GitHub与AtomGit
本工作台GitHub为主。镜像workflow默认禁用，需要变量 ATOMGIT_MIRROR_ENABLED=true、ATOMGIT_OWNER、ATOMGIT_REPO 和密钥 ATOMGIT_USER/ATOMGIT_TOKEN。
只推main，拒绝分叉，不强推/不prune；验证远端main SHA与HEAD一致。认证由临时askpass读取环境，不写remote URL。
不自动同步tags/LFS/issue/PR/附件；这些若需要须分别设计与确认。
没有新增定时计划；仅push和手动触发。未配置/未验证AtomGit前不能说“双平台已同步”。
