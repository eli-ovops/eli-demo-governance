from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from pathlib import Path
D=Path('tmp/pdfs/eli-casebook'); W,H=960,600
for n,f in [('CN','Redesign-Noto-Regular.ttf'),('CB','Redesign-Noto-Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,str(D/f)))
for n,f in [('EN','Arial.ttf'),('EB','Arial Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,'/System/Library/Fonts/Supplemental/'+f))
ink='#18233B';paper='#F5F3ED';blue='#3259DC';muted='#58657A';white='#FFFFFF';orange='#F8895C';lime='#E4F0AE';line='#DBDFE7'
c=canvas.Canvas('output/pdf/Eli_FDE_AI业务提效_案例设计版.pdf',pagesize=(W,H),pageCompression=1)
c.setTitle('Eli | FDE 与 AI 业务提效');c.setAuthor('Eli')
from PIL import Image
from io import BytesIO
_image_cache={}
def pdfimage(file):
 key=str(file)
 if key not in _image_cache:
  im=Image.open(file).convert('RGB');buf=BytesIO();im.save(buf,format='JPEG',quality=94,subsampling=0);buf.seek(0);_image_cache[key]=ImageReader(buf)
 return _image_cache[key]
all_text=[]
def box(x,y,w,h,col,r=0):
 c.setFillColor(HexColor(col));c.setStrokeColor(HexColor(col))
 if r:c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=0)
 else:c.rect(x,H-y-h,w,h,fill=1,stroke=0)
def txt(x,y,s,size=14,col=ink,font='CN'):
 all_text.append(s);c.setFillColor(HexColor(col));c.setFont(font,size);c.drawString(x,H-y-size*.94,s)
def wrap(x,y,s,width=370,size=14,col=muted,leading=24,font='CN'):
 yy=y
 for para in s.split('\n'):
  buf=''
  for ch in para:
   if pdfmetrics.stringWidth(buf+ch,font,size)>width:
    if ch in '，。；：、！？':buf+=ch;continue
    txt(x,yy,buf,size,col,font);yy+=leading;buf=ch
   else:buf+=ch
  if buf:txt(x,yy,buf,size,col,font);yy+=leading
 return yy
def photo(n,x,y,w,h):c.drawImage(pdfimage(str(D/(n+'.png'))),x,H-y-h,width=w,height=h,mask='auto')
def lineat(x,y,w,col=line):box(x,y,w,1,col)
def base(n,label,bg=paper):
 box(0,0,W,H,bg);dark=bg in [ink,blue];co=white if dark else ink
 txt(38,24,'ELI',19,co,'EB');txt(93,30,'SELECTED WORK',9,co,'EN');txt(38,567,label,10,co,'EN');txt(886,562,f'{n:02}',19,co,'EN')
def label(x,y,s,bg=blue,fg=white):
 box(x,y,pdfmetrics.stringWidth(s,'CN',11)+22,27,bg,3);txt(x+11,y+6,s,11,fg)
def end():c.showPage()


cream='#F3EDE2';gold='#896A43';rulecol='#C6B9A3';espresso='#302B26'
def head(n,topic,bg=cream):
 box(0,0,W,H,bg);co=cream if bg==espresso else ink
 txt(42,30,'ELI',20,co,'EB');txt(91,37,'FDE / AI ENABLEMENT',9,co,'EN')
 txt(43,568,topic,10,co,'EN');txt(889,558,f'{n:02d}',18,co,'EN')
def img(file,x,y,w,h):c.drawImage(pdfimage(file),x,H-y-h,width=w,height=h,mask='auto')
def row(y,h,b,x=446,w=464):
 lineat(x,y,w,rulecol);txt(x,y+19,h,12,gold,'CB');txt(x+145,y+17,b,16,ink,'CB')
# 1 cover
img('output/pdf/assets/cover-architecture.png',0,-20,960,640)
txt(42,32,'ELI',21,ink,'EB');txt(42,74,'FDE / AI ENABLEMENT',10,ink,'EN')
txt(42,190,'深入业务，',47,ink,'CB');txt(42,246,'让 AI 落地。',47,ink,'CB')
box(44,333,42,3,gold)
wrap(43,360,'FDE · AI 业务落地\n流程自动化 · 业务提效',388,15,ink,26)
txt(43,524,'FDE / AI 业务提效实践',15,ink,'CB');txt(43,565,'PORTFOLIO  /  2026',10,ink,'EN')
end()
# 2 evidence map
head(2,'EXPERIENCE MAP')
txt(42,103,'理解业务，把 AI 用在关键环节。',34,ink,'CB')
wrap(43,161,'从业务场景切入，识别重复工作与信息断点，设计可验证的 AI 提效方案。',844,16,muted,26)
for i,(num,h,b,pages) in enumerate([
 ('01','机构展示','公益基金会官网 / 律师事务所官网','03 - 04'),
 ('02','协同与营销','律所 OA 系统 / 英国滤水器全域营销','05 - 06'),
 ('03','业务验证','库存业务验收 / AI 录单交互原型','07 - 08')]):
 y=244+i*96;lineat(43,y,870,rulecol);txt(43,y+22,num,30,gold,'EN');txt(130,y+25,h,23,ink,'CB');txt(396,y+31,b,15,ink);txt(835,y+32,pages,11,gold,'EN')
end()
# Website case studies: live high-resolution captures, editorial detail views.
def viewport(file,x,y,w,h,sx,sy,sw,sh):
 # Source coordinates in CSS pixels; original screenshots use device scale 2.
 iw,ih=Image.open(file).size;scale=w/(sw*2)
 c.saveState();path=c.beginPath();path.rect(x,H-y-h,w,h);c.clipPath(path,stroke=0)
 c.drawImage(pdfimage(file),x-sx*2*scale,H-y+sy*2*scale-ih*scale,width=iw*scale,height=ih*scale)
 c.restoreState()

head(3,'SELECTED EXPERIENCE / 01')
txt(43,97,'公益机构 / 官网开发',12,gold,'CB')
txt(42,135,'深圳市予善佑',27,ink,'CB');txt(42,172,'公益基金会',27,ink,'CB')
box(43,223,38,3,gold)
wrap(43,250,'参与官网开发，将机构介绍、公益项目与公开信息呈现在统一的网站入口。',252,15,ink,25)
lineat(43,355,251,rulecol)
txt(43,375,'项目呈现',12,gold,'CB')
for y,h,b in [(407,'公益项目','分类展示项目与进展'),(474,'信息公开','集中呈现新闻与公告')]:
 txt(43,y,h,18,ink,'CB');txt(43,y+29,b,13,muted)
f='output/pdf/assets/foundation-web-hd.png'
box(327,89,598,270,'#E4DAC9')
viewport(f,339,101,574,246,0,0,1440,617)
# Two complete project cards, enlarged independently from the hero.
box(327,377,288,170,'#E4DAC9')
viewport(f,337,383,268,159,198,994,524,311)
txt(641,382,'从机构形象',20,ink,'CB');txt(641,412,'到项目内容。',20,ink,'CB')
wrap(642,458,'让访问者沿着项目与信息入口，进一步了解机构。',259,14,muted,23)
txt(642,526,'ysy.ovops.com',11,gold,'EN');c.linkURL('https://ysy.ovops.com/',(638,59,850,82),relative=0)
end()

head(4,'SELECTED EXPERIENCE / 02')
txt(43,97,'专业服务机构 / 官网开发',12,gold,'CB')
txt(42,135,'广东卓建（光明）',25,ink,'CB');txt(42,172,'律师事务所',27,ink,'CB')
box(43,223,38,3,gold)
wrap(43,250,'参与律所官网开发，呈现专业服务、律师团队与机构内容，连接对外展示和咨询入口。',252,15,ink,25)
lineat(43,379,251,rulecol);txt(43,399,'项目呈现',12,gold,'CB')
txt(43,434,'服务 / 团队 / 资讯',18,ink,'CB');txt(43,467,'中英文网站入口',13,muted)
txt(43,526,'zj.ovops.com',11,gold,'EN');c.linkURL('https://zj.ovops.com/',(40,58,218,81),relative=0)
f='output/pdf/assets/lawfirm-web-hd.png'
box(327,89,598,206,'#E4DAC9')
viewport(f,339,101,574,182,0,0,1440,456)
for x,num,h,b in [(340,'01','专业形象','品牌主视觉与服务入口'),(635,'02','内容组织','资讯分类与团队展示')]:
 txt(x,321,num,13,gold,'EN');txt(x+31,317,h,20,ink,'CB');txt(x,353,b,13,muted)
lineat(340,390,572,rulecol)
viewport(f,339,413,574,110,40,1263,1360,260)
txt(340,535,'机构与团队入口 / 网页局部',10,gold)
end()
# 5 OA
head(5,'INTERNAL SYSTEMS')
img('output/pdf/assets/office-editorial.png',0,0,400,600)
txt(446,35,'ELI  /  SELECTED WORK',10,ink,'EB');txt(446,105,'律师事务所',15,gold,'CB')
txt(444,150,'从机构展示，',37,ink,'CB');txt(444,204,'延伸到内部协同。',34,ink,'CB')
lineat(447,279,459,rulecol)
wrap(447,309,'参与律师事务所 OA 系统搭建，具备专业服务机构内部办公系统的项目经验。',434,17,ink,28)
row(408,'项目类型','OA 系统搭建');row(472,'行业方向','法律专业服务')
end()
#6 marketing retain accepted page style
head(6,'INTEGRATED MARKETING')
img('output/pdf/assets/water-editorial.png',0,0,400,600)
txt(446,35,'ELI  /  SELECTED WORK',10,ink,'EB');txt(446,115,'英国滤水器企业',15,gold,'CB')
txt(444,155,'从产品，',39,ink,'CB');txt(444,207,'走向更完整的市场。',32,ink,'CB')
lineat(447,290,459,rulecol)
wrap(447,320,'参与英国滤水器企业全域营销项目，积累海外市场与营销协同经验。',444,17,ink,28)
row(409,'项目类型','全域营销');row(472,'行业 / 市场','净水产品 / 英国')
end()
#7 ERP: evidence, not decorative fake KPI
head(7,'BUSINESS VALIDATION')
txt(42,92,'库存系统业务验收',15,gold,'CB');txt(42,131,'系统里的数量，需要对得上业务。',31,ink,'CB')
wrap(43,190,'围绕采购、发货、退换货与盘点，核对操作结果、单据状态和库存变化。',841,16,muted,25)
box(43,258,244,275,espresso,9);txt(62,272,'09',94,cream,'EB');txt(65,396,'项问题反馈',24,cream,'CB')
wrap(65,447,'已反馈给开发\n待修复后逐项复查',204,14,'#E1D2BA',25)
txt(326,260,'一项典型发现',13,gold,'CB');txt(326,292,'退货未入仓，库存却增加。',26,ink,'CB')
wrap(326,338,'从操作步骤追到数据变化，把异常转成可复现、可核对、可反馈的具体问题。',566,16,ink,28)
for i,(h,b) in enumerate([('流程梳理','角色、路径与业务事件'),('异常复现','触发条件与实际结果'),('验收反馈','期望结果与复查事项')]):
 x=326+i*199;lineat(x,433,182,rulecol);txt(x,457,h,19,ink,'CB');wrap(x,493,b,181,12,muted,20)
end()
#8 Prototype, type-led process rather than fake screen
head(8,'WORKFLOW PROTOTYPE',espresso)
txt(42,92,'AI 辅助录单 / 交互原型',15,'#D7BA8D','CB')
txt(42,137,'先让审核流程，',35,cream,'CB');txt(42,187,'变得清楚、可操作。',35,cream,'CB')
wrap(43,273,'将单据上传、字段查看与人工校验，转成可演示的页面和操作路径。',370,16,'#D4CBBF',27)
lineat(43,407,367,'#75695A');txt(43,432,'配套交付',14,'#D7BA8D','CB')
wrap(43,463,'字段映射 / 功能范围\n客户确认问题 / React + TypeScript 原型',375,14,cream,25)
for i,(num,h,b) in enumerate([('01','上传单据','建立操作起点'),('02','查看字段','组织结构化内容'),('03','人工校验','保留必要的业务判断'),('04','确认记录','明确流程结束状态')]):
 y=124+i*98;lineat(465,y,450,'#75695A');txt(469,y+19,num,28,'#D7BA8D','EN');txt(535,y+20,h,22,cream,'CB');txt(535,y+56,b,13,'#D4CBBF')
end()
#9 closing: same art detail as cover, quiet coherent bookend
head(9,'LET’S WORK TOGETHER')
txt(42,104,'从一个高频业务场景开始提效。',35,ink,'CB')
wrap(43,164,'先明确提效目标、实施范围与验收方式，再推进一轮付费试点。',830,17,ink,28)
for i,(num,h,b) in enumerate([('01','带来业务场景','梳理现有流程、重复工作与关键耗时。'),('02','确定试点范围','明确 AI 介入方式与验收标准。'),('03','用结果推进决策','验证流程效果，决定下一步投入。')]):
 x=43+i*296;lineat(x,272,269,rulecol);txt(x,299,num,28,gold,'EN');txt(x,351,h,23,ink,'CB');wrap(x,398,b,259,15,ink,25)
lineat(43,505,870,rulecol);txt(43,524,'联系 Eli',19,ink,'CB');txt(237,529,'回复资料发送人，预约业务沟通。',15,gold)
end();c.save()
Path('tmp/pdfs/eli-casebook/book-text.txt').write_text(''.join(all_text))
missing=sorted({ch for s in all_text for ch in s if ord(ch)>127 and ord(ch) not in pdfmetrics.getFont('CN').face.charToGlyph})
assert not missing,missing
print('PDF exported; no missing glyphs')
