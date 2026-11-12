from pathlib import Path
import csv,json,collections,re,html
O=Path('/Users/USER/Documents/eli/output/经历盘点_2026-09-16')
# Curated workstreams; stages are evidence levels, not current external verification.
raw='''投资与自动化研究|BitLangLang / bit浪浪|5—6月|加密交易研究、公式注册、历史窗口、shadow/paper observation、模拟实验与交接包|已有研究与模拟产物|不是已证实盈利策略；未核对真实收益|/Users/USER/Documents/bit浪浪万倍|019ed3d8-1431-7991-b0a3-120da247b819
投资与自动化研究|Serenity Alpha Research / 国内版|5—9月|美股/国内股票研究、AI供应链瓶颈、小市值候选、GARP入场框架、持仓与条件跟踪|持续研究与决策辅助|投资收益与经营收入分开；未审计盈亏|/Users/USER/Documents/serenity|019f2364-a80d-7823-bbbb-dbbf7170084f
投资与自动化研究|NVIDIA GTC / AI Factory研究站|6月|GTC相关产业链与候选股证据刷新、静态研究网站、与Serenity论点整合|研究包与静态站尝试|与Serenity有关联，不算第二份独立收入|/Users/USER/Documents/黄仁勋 GTC大会|
投资与自动化研究|QuantCrypto / Gate永续策略实验|7月|回测引擎、成本与初始权益修正、保证金/仓位/止盈止损组合实验|有代码与回测报告记录|历史结论：123个预注册变体没有合格策略；工程通过不等于赚钱|/Users/USER/Documents/量化|019f4a3d-f904-7970-8fc0-d02be682b586
投资与自动化研究|Hermes / 乔帮主策略执行自动化|7—9月|本机Agent、消息连接、策略到订单、状态台账、保护单与自动下单可靠性修复|有部署与运行记录|9月11日记录仍需新策略实盘回执验收；本次未碰账户或服务|/Users/USER/Documents/Hermes|01a07436-9fd6-7b41-a33b-52cbe25e5ba6
投资与自动化研究|MT4 EA跟单评估|9月|服务商策略与多账号对比、终端连接可行性|评估/连接尝试|不证明已跟单、盈利或可持续；不收录账号凭证|/Volumes/EXTERNAL/wr库存系统/ea量化|01a084a4-499f-78a0-872a-9bae7d0a27ef
客户交付与业务系统|卓建（光明）律所官网|6—7月|前后端接收、地图跳转、中文/英文内容、Hero排版、Payload CMS、浏览器验收与发布维护|参与实际网站开发与维护|团队项目经验；未核对你个人收款|/Users/USER/Documents/T1   淇  卓建律所|019f3c1a-e064-7f10-9a15-56c688724463
客户交付与业务系统|予善佑公益基金会官网|7月|公益站参考拆解、品牌/页面改造、项目与信息公开、前后台与发布验收|参与实际网站开发；曾经历大量迭代|韩红参考Demo属于该项目过程，不另算真实客户|/Users/USER/Documents/慈善网站demo|019f2325-6c65-7ab3-9e7e-6ccee8f160c9
客户交付与业务系统|律所OA / 知识库相关经验|7月及本人补充|会议里有律所二期OA/知识库规划；你明确说参与过OA搭建|本人确认有经验，历史会议可佐证方向|具体已交付模块、个人责任和验收证据仍未定位，不能替你补写|/Users/USER/Documents/T1   淇  卓建律所|019f22f6-b3c3-7232-92d0-74bb6d710d83
客户交付与业务系统|原点向量官网重塑 / V2|7月|OpenAI等网站参考、内容与服务定位、九行业评估、23单元信息架构、迁移蓝图与设计方案|研究/设计/迁移实现记录|多个重塑目录归并为一条持续尝试；不据此认定全部上线|/Users/USER/Documents/原点向量官网V2|019f8d90-223a-7241-a7ac-43d75abf183c
客户交付与业务系统|原点向量SEO / GEO|6—7月|品牌事实统一、旧域迁移、页面Meta与内容、Bing/百度检查、外部信号与监测清单|有优化与核查材料|不等于排名、询盘或收入已提升|/Users/USER/Documents/原点向量SEO|
客户交付与业务系统|Otherwater英国KOC与营销协同|6—7月|Instagram/TikTok达人搜集、活跃度核验、候选表、邮件/私信、brief和合作进度复盘|有候选池、外联与沟通记录|7月28日复盘未有可核验内容发布/转化数据；不能等同全域营销全模块均由你完成|/Users/USER/Documents/T1-UK KOC淇|019fa636-8810-7571-9254-ad1c6954207e
客户交付与业务系统|WilliamRock库存与到货周期系统|6—9月|库存查询、数据模型、前后端原型、PRD与客户确认表、后续国内工厂/海外仓选型|有原型/需求包，后续选型与试点探索|旧库存项目、库存系统及wr库存系统合并理解；生产交付未证实|/Volumes/EXTERNAL/wr库存系统|
客户交付与业务系统|WilliamRock家具展示站 / CMS / Shopify|8—9月|家具目录、参考站复刻研究、前台视觉、双语/媒体、Payload本地L1、Shopify需求确认|静态目录与本地工程存在|不把本地L1、模板或Shopify需求当完成生产商城|/Volumes/EXTERNAL/wl|01a07431-f0e8-7a10-83b3-964de94dce01
客户交付与业务系统|WilliamRock海外B2B开发信|8—9月|家具采购商研究、模板、分批发信和退信核查|有开发信与外联材料|这是家具业务获客，不是你个人建站服务的44家客户；未核对成交|/Volumes/EXTERNAL/wl/output/prospecting|
客户交付与业务系统|淼瀚洁具库存ERP业务验收|8—9月|采购、发货、退换货、仓库、盘点等业务测试，整理9项问题反馈|有业务测试与缺陷清单|参与业务验收，不等于你独立开发整个ERP；反馈不等于修复|/Users/USER/Documents/ChatGPT/淼瀚洁具 库存管理系统|01a07437-1907-77b1-8afb-4d15b09c95bb
客户交付与业务系统|华奕农牧单据到报表|7月|约10类异构单据、字段映射/计算、人工复核、现有Excel报表需求理解|需求/会议梳理|当时项目目录为空，未找到完成开发或上线证据|/Users/USER/Documents/华奕农牧|019f5e53-b408-7031-955c-816a53907d38
客户交付与业务系统|Eli AI录单Demo与FDE案例包装|6—9月|需求包、报价模板、单据上传/字段查看/人工校验交互、案例PDF|L0交互原型与案例集存在|没有接真实OCR/LLM/后端；PDF是销售材料，不是新增客户成果|/Users/USER/Documents/eli|01a07491-0287-7072-b0d4-c1ba06b2a83d
独立网站与SaaS探索|Proofline / 印刷报价确认|7月|客户修改、V1→V3版本确认、批准→生产的可点击HTML演示|历史L0预览部署与浏览器验收记录|是Mock预览，不是已收费的生产SaaS|/Users/USER/Documents/网站/印刷报价确认Demo|019f6ba8-e8b5-7b12-8e7c-dfcd1d84d71d
独立网站与SaaS探索|Approval Workflow / Production Handoff|7月|定制生产错版、批准/交接痛点、22个事故和现有补丁反证|完成方向研究，独立版本工具曾被DROP|该方向被否定不等于创业能力被否定；与Proofline是同一探索链的不同阶段|/Users/USER/Documents/Approval Workflow|019f7974-608d-7b02-83f2-4c719b649e4b
独立网站与SaaS探索|LotCost Tracker|7月|批量拍卖/转售商品成本分摊、库存、销售、利润和CSV导出|PRD与本地交互实现/返工记录|没有发现收费与持续使用证据|/Users/USER/Documents/网站开发|019f6695-3bfb-7191-abfb-6beb24c55756
独立网站与SaaS探索|垂直窄赛道/批量网站Hunter|7月|Micro SaaS、SEO工具站、国内人工工作流、Starter Story反向筛选、宠物配对等|大量研究与候选评估|候选不是已启动产品；多个Hunter/Studio目录合并|/Users/USER/Documents/批量网站|
独立网站与SaaS探索|ClaimFlow / 付费SaaS筛选|8月|TrustMRR/Starter Story研究；工程分包变更订单、合同通知与索赔证据包概念|有可编辑静态落地页|README明确无后台、登录、AI处理、支付或真实索赔服务|/Volumes/EXTERNAL/saas|01a028a8-76d7-7360-b495-4e76bddef69d
独立App与小程序|Focumi / 自律宠物|8—9月|专注与应用屏蔽、宠物Milo、3D/Blender动作与视觉、SwiftUI、真机与上架修复|有原生工程、测试和App Store流程记录|出现过审核/权限阻塞；用户看到商店与独立确认分开，未查收入|/Volumes/EXTERNAL/app/自律宠物-iOS|01a07434-8b28-7c80-bf0d-87a56bb1e8d1
独立App与小程序|LocalStamp旅行水印相机|7—8月|拍摄、时间/GPS地点、三种样式、本机JPEG合成、Photos与分享|原生iOS MVP与模拟器验证记录|无支付；历史真机签名暂停，不当作已发布收费App|/Volumes/EXTERNAL/app/LocalStampMVP|
独立App与小程序|真实发型试戴|7—8月|三视图上传、发质约束、面部关键点校准、2D/2.5D跟随、真实换发效果试验|网页/模拟器原型与技术实验|README明确没有接真实换发AI；真实效果是关键未决项|/Volumes/EXTERNAL/app/真实发型试戴MVP|
独立App与小程序|周易留白阅读 / 海外反思仪式|7—9月|经典文本整理、六爻与阅读体验、网页/iOS原型、付费定位；9月重新评估|原型工程存在；9月16日有重启PRD与验证方案|当前是重启材料，真实购买与留存未证实|/Volumes/EXTERNAL/app/周易留白阅读原型|01a0a7f5-1938-7d01-8b61-5bace1bbddd9
独立App与小程序|Pocket Rove / EarthOnlineGuide|8—9月|每日小冒险任务、像素视觉、双语、历史/收藏、付费相关设计、上架与版本迭代|有完整工程、上架核验历史与持续迭代|最新1.8系列构建/发布不混淆；本次未登录查看销量与收入|/Volumes/EXTERNAL/app/EarthOnlineGuide|01a07e82-3a5a-79f1-9814-bbb74b012171
独立App与小程序|轻量App机会研究池|7—9月|海外付费信号、差评/影子工作流、亚洲产品英语本土化、消费产品评分|至少50份去重研究/PRD题名索引|这是研究文档数，不是50个完成产品；见附录候选池|/Volumes/EXTERNAL/app/Research|01a09a61-f98b-7492-939a-e3ab46f96f7d
独立App与小程序|微信小程序广告变现项目|6月|小程序产品/UI、前端、后端方案、测试合规与上架准备|有规划与协作任务记录|没有据此确认上线、广告展示或收入|/Users/USER/Documents/微信小程序开发|
独立App与小程序|AI创作工坊 / Vibe Coding作品社区|6月|AI创作者项目分享、作品展示、微信小程序MVP与本地体验修复|本地Mock与审查任务记录|与广告变现小程序有关联，是否同产品演化待确认|/Users/USER/Documents/小程序|
接单与获客实验|澳大利亚/英国小商户建站|8—9月|找商户、研究旧站、AU$800/£600方案、制作替换Demo、公开预览和邮件外联|确实做过Demo及发信；9月9日记录复核44家已发送客户|2家历史婉拒、2家出现退信、其余40家未检出相关回复；9月11日记录尚无成交，非今天邮箱实时结果|/Volumes/EXTERNAL/海外落地页|01a0850e-ae8b-7aa1-a253-cfd0a6a467cd
接单与获客实验|Upwork自由职业接单|8—9月|英文档案/作品集、岗位筛选、Connects成本、公司简介等提案|有真实提案提交成功记录|报价$138.90是提案价格不是收入；记录出现27 Connects Boost；无合同/收款核验|/Users/USER/Documents/ChatGPT/upwork|019ffe16-8780-73e3-af4e-087494bfae84
接单与获客实验|UUMIT与其他接单渠道|8月|平台注册可行性、基于既有案例筛工作、网页Audit/QA服务切口、国内外渠道研究|渠道与能力准备|未查到可确认的成交；注册/候选不是客户|/Volumes/EXTERNAL/uumit|
接单与获客实验|闲鱼AI视觉服务小店|8月|职业头像、形象照、换装、个人写真、电商主图；价格、五图与客服/履约SOP|用户曾报告手机端已发布，已有发布后修订包|未独立核验线上商品及订单；另研究PPT/表格/远程数字交付|/Volumes/EXTERNAL/咸鱼|
内容工具与媒体|织境 / 小红书本地AI工作台|8月|账号风格、产品图理解、文案/逐图生成、编辑确认、Provider/BYOK与Windows包|本地产品化Mock及Provider工程基础|README明确真实服务E2E和Windows真机验收未通过，不是成熟商业成品|/Volumes/EXTERNAL/小红书|
内容工具与媒体|抖音AI真假/防骗教育IP|7—8月|主题→短脚本→分镜→生成Prompt→配音字幕/发布话术；即梦接入与视频迭代|有脚本、生成/审片与内容工作流尝试|不是视频SaaS，未查到账号收入|/Users/USER/Documents/抖音ai|019fb0e7-7860-7fc1-a150-e1e3dc036b82
内容工具与媒体|Pocket Rove海外推广与AI短片|9月|TikTok/Instagram/Reddit/YouTube推广、创作者名单/邮件、脚本/关键帧、即梦短片、发布与低曝光检查|有推广与素材产出，属于Pocket Rove获客链|发片/发邀请不等于安装、付费；与App不是两笔生意|/Volumes/EXTERNAL/ai视频|01a08542-c7b7-7780-be54-bc33294dc502
内容工具与媒体|AI虚拟音乐人 / Suno变现|8月|音乐变现模式、原创人格/声线/歌词/视觉基线、歌手案例和商用条件研究|方向研究与项目规则|未查到发行作品和版税收入闭环|/Volumes/EXTERNAL/ai音乐|019fe4e0-8e46-70a1-9ea1-41d05dd1e0f1
内容工具与媒体|原点向量动漫数字人|8月|接收5.3.4/5.3.6包、本机启动/Gatekeeper/GPT-SoVITS语音诊断|软件接收与运行诊断经验|不能把接收调试写成你独立开发数字人模型|/Users/USER/Documents/淇 数字人|019fbb07-a4cb-7982-81e8-9e0e94b7a50c
工作基础与长期准备|AI Workflow OS / Obsidian记忆库|6—8月|自动知识库、会话总结模板、Codex长任务母版、内容回流与项目记忆|脚本/模板/知识库尝试|主要是自用生产力基础设施，未证实商业收入|/Users/USER/Documents/obsidian辅助记忆库|
工作基础与长期准备|Skills、PMO、Agent工具与Mac维护|贯穿5—9月|技能筛选安装、SOP/AGENTS、分工交接、Harness、浏览器、网络重连、磁盘与远程连接排查|大量持续治理和工具维护工作|不另算客户项目；任务量不等于工时或有效产值|/Users/USER/Documents/skills|
工作基础与长期准备|网站/系统工程化学习|6—7月|JS/Next.js/Payload、部署/基础安全、SEO/GEO、CRM/ERP边界、需求/测试/交付入门|学习任务和练习Demo|学习材料不等于完成生产交付|/Users/USER/Documents/学习专用|
工作基础与长期准备|英语 / 雅思词根词缀学习|8—9月|学习方式研究、日/周教练、词汇与例句、系统学习计划|持续学习记录|长期准备，不属于已失败生意|/Volumes/EXTERNAL/移民|01a06a24-4a0e-76a3-a589-40de1d0727d0
工作基础与长期准备|海外居住与移民路径|8—9月|职业/学历材料整理、多国留学工作与永居路径研究|路径核查与材料准备|未核验申请/录取/签证结果；此报告不展开家庭财务隐私|/Volumes/EXTERNAL/移民|01a07432-6c38-7810-8b63-4420dcda2586
工作基础与长期准备|其他零散制作与技术探索|6—9月|CAD转STL可行性、Blender房间/游戏讨论、拼豆工程图、Logo/去底/配色素材、企业微信群Bot设想|混合：问答、实验及部分制作记录|这些不应自动归为正式商业项目|/Users/USER/Documents/Codex|
'''
items=[]
for i,l in enumerate(raw.strip().splitlines(),1):
 cat,name,period,attempt,stage,boundary,root,tid=l.split('|')
 if name.startswith('WilliamRock库存'):tid='' # source selected below, do not invent an identifier
 items.append(dict(id=f'{i:02}',category=cat,name=name,period=period,attempt=attempt,stage=stage,boundary=boundary,root=root,thread_id=tid))
rows=list(csv.DictReader((O/'全部任务索引.csv').open(encoding='utf-8-sig')))
for x in items:
 if not x['thread_id']:
  rr=[r for r in rows if r['cwd']==x['root']]
  if not rr and x['name'].startswith('WilliamRock库存'):rr=[r for r in rows if 'T1-WilliamRock库存管理' in r['cwd']]
  if rr:x['thread_id']=rr[0]['id']
 x['root_exists']=str(Path(x['root']).exists())
 if x['thread_id']:assert x['thread_id'] in {r['id'] for r in rows},x
with (O/'尝试总表.csv').open('w',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(items[0]));w.writeheader();w.writerows(items)
(O/'尝试总表.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
print('curated workstreams',len(items))
