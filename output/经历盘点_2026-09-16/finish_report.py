from pathlib import Path
import json,csv,collections,html,re,datetime
O=Path('/Users/USER/Documents/eli/output/经历盘点_2026-09-16')
items=json.loads((O/'尝试总表.json').read_text());rows=list(csv.DictReader((O/'全部任务索引.csv').open(encoding='utf-8-sig')))
byid={r['id']:r for r in rows};fs=list(csv.DictReader((O/'文件索引.csv').open(encoding='utf-8-sig')))
# Expanded research inventory includes top-level research notes and Research/ documents.
research=[];seen=set()
for r in fs:
 p=Path(r['path']);base=Path('/Volumes/EXTERNAL/app')
 if not p.is_relative_to(base) or p.suffix!='.md':continue
 rel=p.relative_to(base)
 if (len(rel.parts)==1 and p.name!='AGENTS.md') or (rel.parts[0]=='Research' and len(rel.parts)<=3):
  if p.name not in seen:research.append(r);seen.add(p.name)
with (O/'App研究与候选文档索引.csv').open('w',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=['path','bytes','modified']);w.writeheader();w.writerows(research)
extract=[]
for r in research:
 p=Path(r['path'])
 try:s=p.read_text()
 except:continue
 lines=[l for l in s.splitlines() if l.startswith(('## ','### ','| '))]
 if lines:extract.append('## '+p.name+'\n来源：'+str(p)+'\n\n'+'\n'.join(lines))
(O/'研究候选与历史判定摘录.md').write_text('# 研究候选与历史判定摘录\n\n这是历史研究原文的标题/表格索引，不是当前市场建议，也不是我方营收。重复候选、竞品及被淘汰方向均可能出现。\n\n'+'\n\n'.join(extract))
intro='''# Eli：2026年5月底—9月16日的尝试与资产盘点

整理日期：2026-09-16。用途：回顾你究竟做过什么、留下了什么、哪些走到商业验证；不是对外案例宣传册。

## 先说结论

你不是“这几个月什么都没做”，也不是“只是一直学、从没找客户”。记录里同时存在：真实客户项目参与、多款原型/原生App、独立SaaS探索、真正的冷邮件与平台提案、内容生产，以及大量工具治理工作。

本报告合并出 **46条可辨识的工作方向/尝试链**。这不是46家创业公司，也不是46个产品：比如Proofline和Approval Workflow是一条探索链；Pocket Rove与其视频推广属于同一产品；同一项目的内置盘、移动盘、工作树、归档与多代PMO不重复计为新项目。条目用于把经历说清楚，不能相加成“完成了46个项目”。

最关键的区别是：**你积累的开发与交付证据很多，但能确认的、属于你个人独立业务的付费和复购证据少。** 本次没有登录支付、银行、邮箱或App Store后台，因此不能给出“历史总收入为零”的审计结论；你目前没有稳定收入是你本人当前陈述。旧公司客户项目、第三方创业故事的营收、模拟回测、投标报价，均不算你的独立收入。

## 这次实际检查了什么

- 本机Codex数据库：2,555条任务记录，含1,335条已归档记录。任务包含主对话、执行子任务、审批检查、交接与迁移，不能当作2,555次创业或2,555次你本人发起的工作。
- 日期：数据库最早创建于2026-05-30；内容扫描与文件复核截至2026-09-16，约三个半月。
- 会话文件：扫描数据库所指向的2,555个JSONL；另发现并检查13个未由数据库当前路径引用的文件，其中只有1个任务ID不在数据库，其余是同一ID的历史分片/副本。共2,568个文件、2,556个可辨识任务ID。
- 正文提取：流式处理约126.6万行会话数据；提取19,068个去重用户消息片段（包含部分系统包装/转交内容；按已知注入前缀过滤后17,629个），并保留各任务最近的助手输出用于定位。2,218个数据库任务包含过滤后的用户片段，2,524个有助手输出。
- 文件索引：84,615个文件元数据条目、1,359个浅层目录条目。扫描Documents、Desktop、Downloads、WeChatProjects、用户移交包、Pictures/Movies/Music/Public、lexar移动盘及Open Design用户项目空间。
- 对代表性README、状态/外联文档、研究表格和会话正文做了定向复核；索引附件保留全部已扫描任务与文件条目，方便继续查证。

**覆盖边界：这是索引级总盘点＋重点正文复核，不是逐字阅读Mac上每一个文件。** 为避免依赖/缓存噪声，文件遍历最多7层，排除node_modules、.git、构建物、模拟器、虚拟环境和系统缓存；不读取凭证库、私人通讯库，也未解压所有历史ZIP。单条会话记录超过2MB的3,642行跳过，以免把大图/巨大工具结果当正文载入；需要时可针对具体项目补读。照片图库因系统权限不可读。云端未同步、已删除且无留存、其他设备上的记录不在本次完整覆盖内。没有修改原项目、交易服务、VPN或线上数据。

## 按时间看，你的重心如何变化

| 时间 | 主要活动 | 可见转变 |
|---|---|---|
| 5月底—6月上旬 | BitLangLang、Serenity、GTC产业链、交易模拟；开始网站与小程序学习 | 投资研究与AI工作方法占较大位置 |
| 6月中下旬 | Otherwater KOC、WilliamRock库存、律所网站、AI录单、SEO、知识库 | 开始把AI用到客户交付和业务流程 |
| 7月 | 予善佑/卓建网站、原点官网与SEO、定制库存；Proofline、LotCost、垂直网站研究 | 一边交付，一边寻找可独立卖的工具 |
| 7月底—8月上旬 | LocalStamp、发型试戴、周易、Focumi；抖音内容、闲鱼、Upwork、AI音乐 | 扩展到个人产品、平台接单和内容变现 |
| 8月中下旬 | 海外小商户建站与冷邮件、小红书工作台、ClaimFlow、Pocket Rove；英语/移民 | 多条收入路线同时存在，部分开始真实获客 |
| 9月 | Pocket Rove迭代/推广、海外建站外联、库存验收、Hermes可靠性、FDE案例；周易重启 | 从单纯做出东西，逐步碰到获客、使用与付费问题 |

时间以记录出现期为主，不是精确工时。创建任务数为5月29、6月233、7月1,270、8月783、9月240；7月的大量执行/审批/交接任务不能直接解释为工作效率或时间分配。

## 已经发生的商业尝试：不能再当你没试过

| 尝试 | 核对到的历史证据 | 可以说什么 | 不能说什么 |
|---|---|---|---|
| 海外小商户建站 | 9月9日任务复核44家已发送客户：2家历史人工婉拒、2家出现退信、其余40家未检出相关回信；9月7日至该次复核无新增回复 | 你实际研究客户、做Demo、发过邮件，并非仅仅准备 | 44家送达/已读，或英国市场整体不行 |
| Upwork | 8月任务留有Build Treet Company Profile提案提交成功记录，报价$138.90，出现27 Connects Boost | 你确实做过平台投标 | 报价就是到账，或任务已经成交 |
| 闲鱼 | 状态文件记录你说已手机端发布，之后修订短文案和五图包 | 做过服务商品化及上架尝试 | 线上发布/曝光/订单已被本次独立确认 |
| Otherwater | 候选池、邮件/私信与合作沟通复盘 | 有海外资源开发和沟通经验 | 达人一定发片、带来销量，或整个营销团队成果都归于你 |
| 客户官网/OA/库存 | 网站源码/维护/验收链，业务系统需求和测试记录；OA另有你本人确认 | 这些是可整理的交付经验 | 原公司项目合同额就是你个人收入 |
| 独立App/内容 | 原生工程、上架流程、推广/短视频/创作者沟通材料 | 不只是PPT或空想 | 有下载就有付费、上架就有稳定收入 |

这些是本地历史记录，不是今天重新登录各平台的实时审计。旧快照不应覆盖更晚的新事实。

## 46条尝试总表

读法：“证据阶段”说明材料支持到哪里；“结果/边界”指出没有证实的部分。旧目录不存在时，保留历史路径用于追溯，不把缺失目录当从未做过。
'''
md=intro
for cat,group in __import__('itertools').groupby(items,key=lambda x:x['category']):
 group=list(group);md+='\n### '+cat+'\n\n| 编号 / 方向 | 时间 | 做过什么 | 证据阶段 | 结果 / 边界 |\n|---|---|---|---|---|\n'
 for x in group:md+=f"| {x['id']} {x['name']} | {x['period']} | {x['attempt']} | {x['stage']} | {x['boundary']} |\n"
md+='''
## 研究过但不能说已做成的候选

为了避免把灵感列表算成完成项目，这一层单列。已找到的主题包括：针织/钩织WIP与PDF图样阅读、LEGO拆解分袋、3D打印耗材净重、舞蹈老师音乐剪辑、宠物十字绣、染发师配方记录、陶艺试釉、缝纫打印比例、同机位复拍叠影、照片清理、降雨/天气工具、倒放音频、哼唱变动画乐队、试妆、聚会主持、运动成就、旅行介绍、个人杂志、AI婚礼辅助、今日吃什么、商品定格短片、真实评价邀请，以及记账/存钱、背单词/老师工作台的海外本土化。

此外还有AI编程工具额度可视化、视频精确取帧、旧收藏再发现、体育卡/车型收藏等候选；垂直网站侧研究过定制生产交接、宠物配对、SEO工具站及多个人工工作流。部分已被放弃或降级，部分只是竞品观察，不能合并成“我做过这些软件”。

完整已定位的研究题名见《App研究与候选文档索引.csv》；历史表格与标题见《研究候选与历史判定摘录.md》。文档中的竞品营收、报价、市场判断是当时的研究内容，不是已重新验证的当前事实，也不是你的收入。

## 这份记录让我修正前面给你的建议

1. **我不能再简单建议你“先做一份案例、先发一条客户消息”。** 你已经做过案例、冷邮件、平台提案和商品上架尝试。下一步需要复盘具体哪里断了，而不是把已做过的动作重新当起点。
2. **你留下的资产不只是代码。** 包括真实机构网站的参与经验、英国达人沟通、业务需求与测试能力、多个App工程、内容/设计资产和外联记录。但“资产可复用”不等于“市场会自动购买”。
3. **材料显示出多路线并行和大量反复筛选、制作、审查、交接。** 这是可观察的模式；它可能分散持续获客与验证精力，但本次没有可靠工时，不能算出浪费比例，也不能据此下结论说你不努力或没有执行力。
4. **你最需要补的不是又一个抽象点子清单，而是已有路线的收入链条。** 对独立产品分别核对：谁看见→谁实际使用→谁回来→谁付费；对服务核对：谁有明确需求→谁愿意沟通→谁接受报价→谁实际付款。不同路线不可混用成果指标。
5. **旧工作交付、独立创业、投资和长期生活准备需要分开评价。** 英语和移民不是失败生意；投资盈亏不是SaaS收入；付费试验失败也不抹掉已积累的工程能力。

本报告不替你决定回去上班，也不新增开发项目。它先把过去的事实摆完整，供你选择下一条主线。

## 哪些资产现在最容易拿来复用

| 资产 | 可复用方式 | 先补的一项证据 |
|---|---|---|
| 卓建/予善佑参与经验 | FDE案例、机构网站/后台交付能力说明 | 你本人具体负责哪部分 |
| Otherwater达人开发 | 海外资源研究、表格清理、沟通跟进方法 | 哪些合作真正完成、你的职责边界 |
| ERP业务验收/AI录单原型 | 业务流程梳理与小范围提效方案 | 客户具体痛点、基线耗时及付费意愿 |
| Pocket Rove | 已有产品继续做使用/付费验证 | 产品分析和实际收入记录 |
| Focumi/LocalStamp/周易/发型 | 复用已做原型和工程，而非从零再建 | 选定人群的真实使用/付费证据 |
| 小红书工作台/ClaimFlow/Proofline/LotCost | 演示或验证材料、可拆出的单环节方案 | 真实目标用户试用/采购证据 |
| 海外建站44家外联记录 | 复盘买方需求、触达渠道、回复与报价 | 逐家区分正在采购、可达、拒绝原因 |
| 闲鱼商品包/Upwork档案 | 继续已有销售入口时复用 | 真实曝光、咨询、合同/订单 |

## 证据入口

总表中的每条都附有历史根目录和可定位任务ID，详见《尝试总表.csv》。下面保留代表性入口；不存在的旧目录不要作为当前执行根。
'''
for x in items:
 md+=f"\n- **{x['id']} {x['name']}**："
 if Path(x['root']).exists():md+=f"[现存材料目录](<{x['root']}>)"
 else:md+=f"历史路径 `{x['root']}`（本次未见原目录）"
 if x['thread_id']:
  r=byid[x['thread_id']];md+=f"；任务 `{x['thread_id']}`；[本地会话记录](<{r['rollout_path']}>)"
md+='''

## 附件与核查限制

- `尝试总表.csv`：46条人工归并方向、阶段、边界、根目录、任务ID。
- `全部任务索引.csv`：数据库2,555条任务；有敏感行的内容已做省略处理。
- `文件索引.csv`：84,615条元数据，未复制文件正文；扫描时生成的本报告目录也可能出现在索引中，不作为历史业务资产。
- `App研究与候选文档索引.csv` / `研究候选与历史判定摘录.md`：研究主题查漏入口。
- `扫描范围.json` / `会话扫描统计.json`：扫描口径、排除项、权限错误与数量。
- `未入数据库会话概览.json`：额外13个历史分片/副本的简要登记。
- `会话内容证据.jsonl` / `任务分组摘录.txt`：内部查证材料。助手历史“已完成”只当历史陈述，关键项目另用README/状态文件交叉核对。

未查：各账户实时收入、全部客户合同/银行流水、每个历史ZIP内部文件、未同步云端对话、图库内部内容。已知没有独立核验的结果均未写成成功。此轮没有删除、移动或改写原业务文件；新增内容仅在本报告目录。
'''
(O/'完整盘点.md').write_text(md)
# Compact, searchable local HTML with only curated content, no external scripts.
css='''body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif;background:#f3ede2;color:#18233b;margin:0}main{max-width:1250px;margin:auto;padding:48px 32px}h1{font-size:38px;letter-spacing:-1px}p{line-height:1.8}small{color:#78654c}input,select{padding:12px;border:1px solid #c7b9a6;border-radius:6px;background:#fff;font-size:15px;margin:6px 10px 20px 0}input{width:380px;max-width:85%}.item{display:grid;grid-template-columns:60px 1fr 1fr;gap:24px;border-top:1px solid #c7b9a6;padding:25px 0}.num{color:#896a43;font-size:28px}h2{margin:0 0 9px;font-size:22px}.meta{font-size:13px;color:#78654c}.path{font-size:11px;word-break:break-all;color:#58657a}.tag{font-size:13px;border-left:3px solid #896a43;padding-left:10px}a{color:#745832}@media(max-width:700px){main{padding:24px}.item{grid-template-columns:36px 1fr}.detail{grid-column:2}}'''
page=f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Eli · 三个半月尝试盘点</title><style>{css}</style><main><small>PERSONAL WORK ARCHIVE / 2026.05—09</small><h1>你这几个月，究竟做过什么。</h1><p>46条归并后的尝试链 · 2,555条数据库任务 · 84,615条文件元数据。<br>包含研究、交付、产品、获客与学习，不等于46个完成产品。历史结果与今日实时状态分开。</p><p><a href="完整盘点.md">完整报告与核查边界</a> · <a href="尝试总表.csv">下载总表 CSV</a></p><input id="q" placeholder="搜索项目、经历、阶段或关键词"><select id="cat"><option value="">所有方向</option>'
for cat in dict.fromkeys(x['category'] for x in items):page+='<option>'+html.escape(cat)+'</option>'
page+='</select><div id="count"></div><section id="items">'
for x in items:
 esc=lambda k:html.escape(x[k]);page+=f'<article class="item" data-cat="{esc("category")}"><div class="num">{esc("id")}</div><div><div class="meta">{esc("category")} / {esc("period")}</div><h2>{esc("name")}</h2><p>{esc("attempt")}</p><p class="path">{esc("root")}<br>任务：{esc("thread_id") or "见文件索引"}</p></div><div class="detail"><p class="tag">{esc("stage")}</p><p>{esc("boundary")}</p></div></article>'
page+='''</section><p class="meta">本地只读盘点，未操作账户、支付、交易、VPN或线上服务。覆盖边界与原始索引详见完整报告。</p></main><script>function filter(){let n=0;for(const e of document.querySelectorAll('.item')){const ok=(!cat.value||e.dataset.cat===cat.value)&&e.textContent.toLowerCase().includes(q.value.toLowerCase());e.style.display=ok?'':'none';n+=ok}document.getElementById('count').textContent='显示 '+n+' / 46 条'}q.oninput=cat.onchange=filter;filter()</script></html>'''
(O/'浏览版.html').write_text(page)
print('report',len(md),'characters; research documents',len(research))
