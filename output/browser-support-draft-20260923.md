# Codex 浏览器与侧栏问题：支持草稿

日期：2026-09-23。最新提交状态：用户明确要求代发后，已在 help.openai.com 官方客服对话发送两项故障摘要，并通过现有账户登录。页面显示原摘要发送记录及 AI 客服回复；另已发送人工升级请求。人工升级回复曾报“生成助手回复时出错”，点击一次重试后仍未取得人工受理确认或工单编号。没有上传本文件、完整日志或会话记录；两项故障尚未修复。下文“未发送”描述仅指此前草稿阶段或本文件附件本身。

## 最新复测（优先于下方原始记录）

用户已正常重启 App，并手动重新打开 Example 页面。当前版本为 26.917.51856 (10492)，主进程 PID 52977，不能把变化只归因于重启。原诊断任务浏览器发现仍在 30.474 秒后失败。

人工新开的页面实际属于主任务 01a0cbf6-283e-73f1-9e91-55fb02e6518c，而非原诊断任务。日志 03:17:53.465 UTC 显示该页面 conversationId 与 ownerRoutePath 匹配，03:17:54.879 Example dom-ready。因此不把旧诊断任务失败当作新页面失败。

随后在主任务直接通过官方 cua.getTab({url:'https://example.com/'},{browser:'iab'}) 读取新页：首轮 60.015 秒超时并重置 runtime；日志 03:20:01 出现 10 次本主任务 No ChatGPT browser route 错误。03:20:31.274 注册 debugger listener 后，再次通过同一 API 绑定仍于 60.037 秒超时。新页的视觉加载没有恢复自动化读取，且问题跨越旧诊断任务与主任务；不能把全部故障仅归于旧临时任务 ID。尚无页面读取、三轮交互或原型运行通过证据。

本轮日志：/Users/USER/Library/Logs/com.openai.codex/2026/09/23/codex-desktop-72535f1a-050a-4a0c-9c10-d07ac8bcd5e5-52977-t0-i1-030548-0.log；主任务新页归属见 2175、2193 行，路由错误及后续注册见 2914–2924、3225 行。时间均 UTC。

局部诊断页重建和正常重启均未证明恢复。不再建议无新证据地重复重启、改网络或清缓存。浏览器自动化连接故障与本地原型 URL 安全拒绝仍应分开处理。下面提及“等待首次重启”的候选计划已被本节实验结果取代。

## 环境

- macOS；Codex 应用版本 26.915.31945，build 9922，bundle com.openai.codex。
- Chrome 153.0.8010.53。
- 已核查插件与应用版本匹配。未修改代理、VPN、权限、安全策略、缓存或应用配置。

## 问题一：浏览器自动化连接失败或操作延迟

预期：官方浏览器工具能连接浏览器，在普通允许网站完成读取、导航及回退。

实际：多个任务及普通网站复现；原生 Chrome 对照操作约 1–2 秒，但 Codex 浏览器操作曾耗时约 42–43 秒。新执行任务打开 Example 页面耗时 60.047 秒后超时；getState 耗时 31.266 秒，浏览器列表为空且返回 nodeRepl.fetch request failed。

将执行任务切到前台后，队列中的浏览器面板已实际打开，Example 页面出现 dom-ready；但 listTabs 仍在 30.965 秒后失败。因此“面板打开”不能证明自动化连接恢复。

日志可见任务路由从真实任务 ID 改派到 client-new-thread 临时 ID，此后持续出现 No ChatGPT browser route is available。前台打开后仍有真实 ownerRoutePath 与临时 conversationId 不一致的记录。路由异常有直接证据，但它是否解释全部延迟尚未确认。

请求支持：确认该版本的临时任务路由迁移是否存在缺陷，以及是否有受支持的单任务重新绑定或重建连接方法。当前未发现可用的单任务修复接口。

候选实验：在其他任务安全结束且用户批准后，正常退出并重开 Codex，再通过同一官方浏览器通路完成三轮读取、导航及回退。该实验尚未执行，不保证有效。

## 问题二：侧栏原型不能运行

两条历史事件必须分开：

1. 打开浣熊动作预览的 file URL 时，浏览器工具约 0.76 秒内明确返回 Browser Use rejected this action due to browser security policy，并禁止绕过限制。
2. 另一份基地交互样本 HTML 通过 open_in_codex 的 file 类型请求打开，返回 queued。该回执不证明文件面板已展示，也不证明 HTML 已运行。

两个事件对应不同文件、不同调用。尚无证据证明 URL 策略拒绝由问题一的连接异常导致。不能以换端口、协议、浏览器或托管方式绕过已明确拒绝的访问。

请求支持：说明此版本中本地 HTML 的受支持预览方式，以及该次 file URL 拒绝应如何通过正式机制诊断。侧栏文件预览、网页运行与浏览器自动化应分别验收。

## 公开资料对照

- https://github.com/openai/codex/issues/20678 ：macOS 浏览器后端连接异常报告。
- https://github.com/openai/codex/issues/29389 ：扩展存在但后端不可用的报告。
- https://github.com/openai/codex/issues/29385 ：页面操作延迟与 Statsig 超时报告；本机尚无对应超时证据。
- https://github.com/openai/codex/issues/23504 ：代理相关的 30–60 秒请求异常报告；未据此修改代理。
- https://developers.openai.com/codex/app/browser ：浏览器能力文档，不构成对本次安全拒绝的例外授权。

上述报告仅作相似现象参考，不能视为本机根因或已验证修复。第三方 codex-browser-fix skill 涉及认证、缓存或启动配置，未发现适用于当前证据的依据，未安装或执行。

## 本地证据位置（提交前另行审阅和脱敏）

- 浏览器诊断：/Users/USER/.codex/visualizations/2026/09/23/01a0cc23-ce5e-7e51-b8be-2569f6df4581/browser-diagnostics/report.md
- 原始计时：同目录 measurements.json。
- 路由摘录：同目录 route-evidence.txt。
- 侧栏诊断：/Volumes/EXTERNAL/app/Research/IdleExplorationGame-20260918/SIDEBAR-DIAGNOSIS-20260923.md

没有修改业务源码、原型或媒体。没有对外发送本草稿或日志。
