from pathlib import Path
import json,datetime
P=Path(__file__).parent
items=[
('01_PocketRove产品开发.md','Pocket Rove PMO｜1.8.0 PRD执行','01a09ef1-3d80-7e41-88b0-9635e91af695','/Volumes/EXTERNAL/app/EarthOnlineGuide',
'''**当前状态：本轮模拟器交付已完成，产品整体仍有待验项。** 名称保留1.8.0，但最新内容回执实际版本是1.8.6(1)，内容版本source-v3-recording-186-r1，不要按旧任务名回退版本。

- 已完成：242条任务（187核心、55彩蛋），录屏114条均有对应任务及中英文结语；默认字号两行排版、限定单测及模拟器中英文完成/历史流程据回执通过。
- 最新用户操作：要求刷新“模拟”；日志记录iPhone 17模拟器已刷新为3核心+1未拆开彩蛋，保留历史与设置。
- 未完成：这一轮内容未更新真实手机、未上传发布；既有iOS17数据库迁移和性能待验项未解除；真人趣味性、留存未证实。
- 下一步：若继续，先由用户选择真机体验或已有待验项，读取对应证据后做单一交付；当前“刷新模拟器”没有遗留执行，不自动新增功能或发布。
- 边界：保留历史、设置、旧任务快照和结果模板；不擅自重置真机。旧单次磁盘门槛豁免不是未来所有任务的无限授权。
''',[
'/Volumes/EXTERNAL/app/EarthOnlineGuide/Planning/ContentReviews/Recording-Integration-20260918/README.md',
'/Volumes/EXTERNAL/app/EarthOnlineGuide/Planning/ContentReviews/Recording-Integration-20260918/全部接入任务与结语.md']),
('02_创作者筛选.md','Pocket Rove｜第二批100位UGC创作者筛选','01a0acf3-9e0c-7733-9977-bf3ed25b22c0','/Volumes/EXTERNAL/app/EarthOnlineGuide/Marketing/Creator-Rescreen-20260917',
'''**当前状态：暂停，未达到100人。** 最新交付文件明确“用户暂停”，不是等待自动续跑。

- 保存结果：原生研究去重85位＝TikTok已核验21、待核验/低活跃40、当前平台排除24；另有旧YouTube补充3、低活跃备选3，单列，不冒充新完成。
- 本轮研究未发邮件；同目录另一任务后续发送47封，研究状态与发送状态分开管理。
- 阻断/风险：部分原站读取曾异常；播放量仅为核验时快照，待核验不能算合格。旧回复检查内容不再当最新邮箱状态。
- 下一步：保持暂停。若用户恢复筛选，只从已保存队列接续，先约定一小批验收标准；不从零重搜、不为凑100降低标准。
- Owner边界：本任务只维护候选与研究证据；发信/谈合作由“Pocket Rove 邮件”负责，避免重复联系。恢复研究不自动授权发信。
''',[
'/Volumes/EXTERNAL/app/EarthOnlineGuide/Marketing/Creator-Rescreen-20260917/CURRENT-CREATORS-PAUSED.md',
'/Volumes/EXTERNAL/app/EarthOnlineGuide/Marketing/Creator-Rescreen-20260917/CURRENT-CREATORS-PAUSED.csv']),
('03_短视频与TikTok.md','00 PMO总控｜Pocket Rove 短视频','01a08542-c7b7-7780-be54-bc33294dc502','/Volumes/EXTERNAL/ai视频',
'''**当前状态：最新交互停在TikTok异常反馈之后；等待官方回复。** 用户明确说“我提交了”，不再次提交，不将其升级为已取得官方回执。

- 当前问题：截至9月17日原检查，招募图文、冰箱视频、披萨视频均公开但零播放；未见明确违规/取消推荐通知。统计“处理中”不证明内容审核或封号，原因UNKNOWN。
- 手机TikTok不可用，不再把手机端账号检查作为必要前提；本次未重新查询平台，以上是时间标注的历史快照。
- 素材：Pizza v4修改记录为9.9秒、1080×1920、真实UI终卡；文件自带未完成项：正常/静音实时播放验收未完成，不能以抽帧/音轨测量替代。
- 下一步：收到回复后核对官方原因与处理；制作方面只接续具体素材的未验项，不重新立完整创意流水线。
- 边界：保留三条原帖及原素材；不自动删帖重发、改VPN、生成付费视频或投广告。用户原始目标为英语母语人群，真实产品UI不得用生成界面替代。
- 旧材料：Production-R6、Fridge-Knock等只在处理对应素材时读取，不能把早期“尚无成片”当整个项目最新状态。
''',[
'/Volumes/EXTERNAL/ai视频/Deliverables/Pocket-Rove-Pizza-Task-Ad-v4/修改记录.md']),
('04_邮件与合作.md','Pocket Rove 邮件','01a09a96-7df8-7643-a823-f4dbfa77200f','/Volumes/EXTERNAL/app/EarthOnlineGuide/Marketing/Creator-Rescreen-20260917',
'''**当前状态：已有合作意向，尚未达成新合作或投放。** 9月18日最新日志明确总预算上限150美元：视频合作/素材100、广告测试50；平台可为Instagram或TikTok。预算不是付款授权。

- 发送：9月17日台账47封发出、20位邮箱缺失/未确认未发、24位排除；SENT不等于送达。原邮件不提预算、不附附件，只介绍合作、下载链接并询价，避免重复发送。
- 回复快照（9月18日历史检查，本轮未刷新邮箱）：Rebecka是用户首选、尚未回复；El已报IG Reel $100/TikTok $200；Elyssia、Anna、Gabby有意向但尚未最终报价；Helen拒绝；存在退信需沿用排除台账。
- 尚未确认：原始素材、干净版、二剪、广告使用权是否含在报价中。30天授权、45–60秒/3任务等是旧回复中的建议，不能自动当对方同意或用户最终合同条款。
- 下一步：先整理一个具体候选的合作需求与询问草稿，确认价格包含内容；只有收到用户明确发送指令才发出。不自动用完150美元。
- Owner边界：只负责外联和合作记录；候选扩搜由筛选任务管理。最新重点为El/Elyssia/Anna，Rebecka保留；名单偏好不等于已认可效果。
''',[
'/Volumes/EXTERNAL/app/EarthOnlineGuide/Marketing/Creator-Rescreen-20260917/OUTREACH-SENT-20260917.md']),
('05_周易项目.md','周易项目重启｜产品与验证负责人','01a0a7f5-1938-7d01-8b61-5bace1bbddd9','/Volumes/EXTERNAL/app/周易留白阅读原型',
'''**当前状态：原生样板与五页重塑已交，真机核心流程通过，体验验收未全部完成。** 文件在移动硬盘Lexar，不在内置盘项目目录。

- 已完成：首页/投掷及阅读、历史、备注、来源、设置统一纸面宋体风格；六次后首页直接进阅读；真机启动卡住通过WKWebView inactiveSchedulingPolicy局部调整修复。
- 原始记录：DeviceFlow-v2的恢复/备注/设置/返回通过；主入口单独DeviceFinal复验1/1通过。此前失败和中间编译失败保留，不写成所有测试从未失败。
- 未完成：音频主线程setActive警告；真实声音/触觉、VoiceOver、键盘展开保存入口、飞行模式、Files备份闭环仍待验。铜钱是分层翻转，非完整三维物理模拟。
- 下一步：优先音频性能定位和一项明确真机验收，不扩展新页或重新生成整套视觉。需设备交互时明确实际连接状态。
- 边界：现手机打开隔离手动体验容器，正式数据未清除。保留origin/schema/原记录与参考视觉；不要用整页截图叠透明按钮假冒原生实现。
''',[
'/Volumes/EXTERNAL/app/周易留白阅读原型/audit/device-r8-2026-09-18/REVIEW.md',
'/Volumes/EXTERNAL/app/周易留白阅读原型/audit/visual-r6-2026-09-18/PREVIEW.md']),
('06_学习App.md','学习 App 达标提醒｜核心验证与最小原型','01a0add0-c73f-7673-86d2-b6185c5bb846','/Volumes/EXTERNAL/app/学习App达标提醒',
'''**当前状态：新版已安装指定iPhone 17，核心能力仍待真机验收，不能宣称可靠自用。** 最新用户目标是先闭环核心功能供本人使用，不是继续美化。

- 已完成：VisualPreview三个Target接入DeviceActivityReport/Monitor、共享目标配置与今日一次提醒实验；签名构建、覆盖安装、启动有9月18日记录，保留原选择/计划。
- 未完成：真实App分钟正确性、系统授权、报告读取目标配置；达标取消通知范围/时效、未达标送达；每日自动续排、跨日/时区/撤权/异常终止可靠性均未通过。
- 最新证据优先：VisualPreview/Evidence/core-device-20260918.md。PROJECT_CORE.md、Evidence/RESULTS.md部分仍为早期“未安装/权限受阻”状态，不能据此回退；也不能把旧七日方案当新版当日实验已实现。
- 下一步：用户在“真实记录与提醒→更新今日计划与报告”核对真实分钟；通过后按文档做两个App（一个达标一个未达标）、关闭主App的当日对照。实验开关默认不启动，明确接受可能误提醒后才启用。
- 边界：报告在系统报告扩展内处理和显示；不导出实际分钟/衍生百分比，不伪造进度。当前实验仅当日、提醒时间至少20分钟后；不宣称永久自动运行。达标误提醒为FAIL，不能用UI通过替代系统能力。
''',[
'/Volumes/EXTERNAL/app/学习App达标提醒/VisualPreview/Evidence/core-device-20260918.md',
'/Volumes/EXTERNAL/app/学习App达标提醒/PROJECT_CORE.md'])]
manifest=[]
for fn,title,tid,root,body,refs in items:
 text=f'# {title}\n\n交接材料快照：2026-09-18。仅整理，未交出Owner、未新建任务、未唤醒执行。\n\n旧任务：`{tid}`\n工作根：`{root}`\n\n'+body+'\n## 最小读取入口\n\n'
 for ref in refs:
  p=Path(ref);assert p.exists(),ref;text+=f'- [{p.name}]({ref})\n';manifest.append({'task':tid,'path':ref,'size':p.stat().st_size,'mtime':datetime.datetime.fromtimestamp(p.stat().st_mtime).isoformat()})
 text+='\n## 接续规则\n\n先读本页和直接相关入口，按需定位原证据，不读取旧任务全文。文档中测试结论来自原回执，本次未重跑；邮箱、平台和设备状态须在实际行动前刷新。未来执行只接当前明确目标，不从历史命令推断外写、删除、付款或发布授权。模型路由拟沿用Astra：PMO medium，明确小任务low；本次没有应用设置。\n'
 (P/fn).write_text(text)
index='''# 六个任务的精简交接包

2026-09-18｜已整理并核对直接证据入口。按用户要求：不创建新任务、不发送续跑消息、不归档旧任务、不改模型或速度。以下不是“接任者已验收”，Owner仍为旧任务。

'''
for fn,title,tid,root,body,refs in items:index+=f'- [{title}]({fn})\n'
index+='''
## 阅读方式

每个接续者只读自己的一页及该页列出的直接证据。不要一次加载六份，更不要复制旧对话。完整原始记录仍保留在旧任务，本包仅保存必要事实和路径。

## 跨任务边界

- 产品开发负责源码、测试及产品版本；模拟器/真机/商店版本分开，营销不自行改产品真值。
- 创作者筛选负责名单与证据，当前暂停；邮件任务负责联系和报价，不重复联系同一人。两者共用Creator-Rescreen目录，文件职责按各自台账划分，未来不能同时改同一份发送账。
- 视频任务负责素材与平台异常；邮件任务谈素材权益与预算。报价、原始文件、广告授权三者不能混同。
- 周易与学习App是独立目录，不能因同属app项目混用签名、数据或真机状态。

## 关键待验

1. Pocket Rove最新242条内容仍以模拟器交付为证据，尚非真机/商店更新。
2. 创作者名单未到100，保留暂停，不自动恢复。
3. TikTok反馈由用户自述已提交，等回复，不重复提交。
4. 150美元为合作与测试预算上限，不是付款或投放批准。
5. 周易音频、无障碍及若干真机体验仍待验。
6. 学习App真实用量与达标抑制提醒未闭环；早期核心文档存在落后于最新安装记录的段落。

## 证据与范围

任务接口读取后，针对返回空items的任务查对应本机rollout的最近完成记录，并核对本包列出的文件。本轮未重新打开邮箱、平台、模拟器或真机，也未重新运行测试。未来变化以实时状态为准。

source-manifest.json仅记录已核对的来源路径、大小和mtime，不复制用户邮箱、凭证或完整日志。新增文件均位于本交接目录；未改业务资产和原审计文件。
'''
(P/'README.md').write_text(index);(P/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('cards',len(items),'verified_sources',len(manifest))
for fn,*_ in items:print(fn,len((P/fn).read_text()))
print('total_bytes',sum(f.stat().st_size for f in P.iterdir() if f.is_file()))
