from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from pathlib import Path
W,H=960,600
OUT=Path('output/pdf/Eli_AI业务落地_精选案例.pdf')
pdfmetrics.registerFont(TTFont('CN','/System/Library/Fonts/STHeiti Light.ttc'))
pdfmetrics.registerFont(TTFont('CB','/System/Library/Fonts/STHeiti Medium.ttc'))
pdfmetrics.registerFont(TTFont('EN','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('EB','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
ink='#153C37'; paper='#F5F3EB'; muted='#64766E'; lime='#D6EE8D'; teal='#24796C'; orange='#D97C50'; white='#FFFFFF'; line='#D5DCD1'
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle('Eli | AI 业务落地与产品实践');c.setAuthor('Eli');c.setSubject('精选案例与合作方式')
def box(x,y,w,h,col,r=0):
 c.setFillColor(HexColor(col));c.setStrokeColor(HexColor(col))
 if r:c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=0)
 else:c.rect(x,H-y-h,w,h,fill=1,stroke=0)
def txt(x,y,s,size=14,col=ink,font='CN'):
 c.setFillColor(HexColor(col));c.setFont(font,size);c.drawString(x,H-y-size*.84,s)
def wrap(x,y,s,width=370,size=14,col=muted,leading=23,font='CN'):
 yy=y
 for para in s.split('\n'):
  out=''
  for ch in para:
   if pdfmetrics.stringWidth(out+ch,font,size)>width:
    txt(x,yy,out,size,col,font);yy+=leading;out=ch
   else:out+=ch
  if out:txt(x,yy,out,size,col,font);yy+=leading
 return yy
def rule(x,y,w,col=line):box(x,y,w,1,col)
def tag(x,y,s,col=teal,bg='#E4EBDD'):
 w=pdfmetrics.stringWidth(s,'CN',10)+20;box(x,y,w,23,bg,5);txt(x+10,y+6,s,10,col)
def base(n,k,dark=False):
 bg=ink if dark else paper;box(0,0,W,H,bg)
 color=paper if dark else ink
 txt(44,28,'ELI',18,color,'EB');txt(91,34,'AI / BUSINESS / PRODUCT',9,lime if dark else muted,'EN')
 txt(685,34,k,10,lime if dark else muted,'EN')
 rule(44,555,872,'#396057' if dark else line)
 txt(44,570,'SELECTED WORK  /  2026',9,'#ACBEB5' if dark else muted,'EN')
 txt(890,568,f'{n:02d}',12,color,'EN')
def end():c.showPage()
# Cover
base(1,'CAPABILITY & CASE STUDIES',True)
box(44,110,44,4,lime)
txt(44,140,'让业务问题',47,paper,'CB');txt(44,207,'成为可验证的方案。',47,paper,'CB')
wrap(46,291,'从业务流程梳理、交互原型，到产品实现与验收。\n以一个具体场景为起点，逐步推进落地。',460,17,'#BACCC1',29)
tag(46,395,'业务分析',ink,lime);tag(140,395,'原型验证',ink,lime);tag(234,395,'产品实践',ink,lime)
txt(46,488,'Eli  /  AI 业务落地与产品实践',17,paper,'CB')
# architectural abstract diagram
for i,(a,b) in enumerate([(660,160),(715,250),(650,345)]):
 box(a,b,175,91,['#28534A','#356B5E','#D6EE8D'][i],12)
 txt(a+18,b+18,['01  UNDERSTAND','02  PROTOTYPE','03  VALIDATE'][i],12,ink if i==2 else lime,'EB')
 txt(a+18,b+47,['看清业务','做出方案','验证结果'][i],22,ink if i==2 else paper,'CB')
end()
# Method
base(2,'HOW I WORK')
txt(44,91,'先把问题定义清楚，再让技术进入流程。',31,ink,'CB')
wrap(44,145,'适合需要梳理业务、验证数字化方案，或推进早期产品的团队。',820,16)
items=[('01','业务拆解','从真实工作方式开始','角色与操作步骤\n输入、输出与关键字段\n异常、权限与人工判断'),('02','原型验证','让讨论变成可见的东西','关键页面与操作路径\n样例数据与人工复核\n明确可做与暂不做范围'),('03','交付验收','用具体结果推进决策','可演示的软件或原型\n问题复现与验收清单\n阶段结论与后续计划')]
for i,(num,title,sub,body) in enumerate(items):
 x=44+i*295;box(x,210,282,269,white,10);txt(x+22,231,num,40,teal,'EN');txt(x+22,292,title,24,ink,'CB');txt(x+22,332,sub,13,teal);wrap(x+22,365,body,238,14,muted,27)
txt(44,509,'以下为精选项目实践，分别展示业务验收、流程原型与独立产品。',13,muted)
end()
# ERP
base(3,'CASE 01 / BUSINESS VALIDATION')
tag(44,83,'企业业务验收 · 匿名案例')
txt(44,122,'库存系统：把“能操作”验到“账实一致”。',31,ink,'CB')
wrap(44,178,'围绕卫浴行业的采购、发货、退换货与盘点流程，梳理页面状态、库存变化和操作结果之间的关系。',375,15,muted,24)
for yy,head,body in [(271,'业务切入','检查货物状态与库存数量是否一致，识别重复操作、状态滞后等业务风险。'),(351,'已有成果','形成业务地图、实操复现记录和开发反馈清单；其中 9 项问题已反馈，待修复后复查。')]:
 txt(44,yy,head,17,ink,'CB');wrap(44,yy+30,body,370,14,muted,23)
box(455,180,461,305,white,12);txt(480,202,'一个典型问题：退货尚未入仓，库存却增加',17,ink,'CB')
for i,(h,s) in enumerate([('创建退货','记录退货意向'),('货物到仓','核实实际到货'),('确认入库','更新可用库存')]):
 x=480+i*143;box(x,251,127,74,'#EAF0E7',7);txt(x+12,266,h,16,ink,'CB');txt(x+12,295,s,11,muted)
 if i<2:txt(x+132,273,'>',14,teal,'EB')
rule(480,354,410)
txt(480,374,'验收重点',12,teal,'CB');wrap(480,399,'数量变化必须对应真实业务事件。\n发现偏差后，提供可复现步骤与期望结果。',402,15,ink,26)
wrap(44,508,'案例范围：业务分析与验收测试；不代表整套 ERP 的独立开发或全部问题已修复。图为匿名流程示意。',865,11,muted,17)
end()
# AI
base(4,'CASE 02 / WORKFLOW PROTOTYPE')
tag(44,83,'AI 录单 · L0 交互原型')
txt(44,122,'先跑通人工审核，再讨论自动化。',32,ink,'CB')
wrap(44,179,'将“上传单据、查看结果、人工校验、确认记录”转成可演示的交互流程。',346,15,muted,24)
for y,h,b in [(269,'设计重点','字段可编辑、异常可识别、人工判断有位置。'),(351,'现有资产','React + TypeScript 本地原型，配套字段映射、功能范围和客户确认问题清单。')]:
 txt(44,y,h,17,ink,'CB');wrap(44,y+30,b,346,14,muted,23)
box(423,180,493,310,white,12);box(423,180,493,42,ink,12);txt(442,194,'单据审核工作台',14,white,'CB');txt(748,197,'界面重绘 / 虚拟数据',10,lime)
box(442,240,170,216,'#F0F1E9',6);txt(456,258,'演示送货单',17,ink,'CB');txt(456,298,'单号 DEMO-001',11,muted,'CN')
for j,(a,b) in enumerate([('品类','示例物料 A'),('数量','12 件'),('单价','¥ 80.00'),('合计','¥ 960.00')]):
 txt(456,329+j*26,a,11,muted);txt(505,329+j*26,b,11,ink)
for j,(a,b) in enumerate([('客户','示例客户 A'),('数量','12'),('总额','960.00')]):
 txt(635,242+j*62,a,11,muted);box(635,260+j*62,260,30,paper,4);txt(647,269+j*62,b,12,ink)
box(635,438,116,28,teal,5);txt(650,446,'人工确认',12,white)
wrap(44,507,'当前验证流程与交互；识别结果为 Mock，尚未接入真实 OCR、LLM、数据库或真实导出。本页为基于原型功能重绘的示意。',867,11,muted,17)
end()
# Product
base(5,'CASE 03 / INDEPENDENT PRODUCT')
tag(44,83,'Pocket Rove · 独立产品实践')
txt(44,129,'把一个想法，',36,ink,'CB');txt(44,179,'推进到真实的产品迭代。',36,ink,'CB')
wrap(44,247,'以日常微冒险为核心的 iOS 产品，围绕任务发现、完成反馈、历史回看与纪念品体验持续打磨。',500,16,muted,26)
for y,h,b in [(348,'产品与体验','功能拆解、双语内容、界面设计与交互迭代。'),(415,'实现与验证','App 实现、模拟器和真机验证、版本管理及上架流程实践。')]:
 txt(44,y,h,18,ink,'CB');wrap(44,y+31,b,500,14,muted,23)
img='/Volumes/EXTERNAL/app/Pocket-Rove-人工上传-五张截图-20260911/2-今日任务-Today.png'
c.drawImage(ImageReader(img),645,H-96-421,width=194.5,height=421,mask='auto')
txt(633,527,'既有产品宣传素材 · 历史版本',10,muted)
wrap(44,510,'展示产品建设与迭代经历，不以收入、用户规模或留存增长作效果承诺。',524,11,muted,17)
end()
# engagement
base(6,'START WITH ONE WORKFLOW',True)
txt(44,102,'先选一个流程，',40,paper,'CB');txt(44,157,'做一轮范围明确的付费试点。',40,paper,'CB')
wrap(44,233,'从最耗时、最容易出错，或最难讲清楚的环节开始。\n先约定成果和验收，再决定是否扩大投入。',805,18,'#BFD0C6',30)
for i,(num,h,b) in enumerate([('01','带来一个问题','一份脱敏样例，或一次现有流程演示。'),('02','约定一个范围','明确交付内容、周期、报价与验收标准。'),('03','获得一个判断','通过演示或测试结果，决定下一阶段。')]):
 x=44+i*295;rule(x,335,271,'#467063');txt(x,358,num,15,lime,'EB');txt(x,390,h,23,paper,'CB');wrap(x,433,b,252,14,'#BFD0C6',24)
txt(44,515,'联系 Eli  /  直接回复本资料的发送人，预约一次业务沟通。',16,lime,'CB')
end();c.save()
print(OUT.resolve())
