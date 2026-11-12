from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from pathlib import Path
D=Path('tmp/pdfs/eli-casebook'); W,H=960,600
for n,f in [('CN','Noto-Regular.ttf'),('CB','Noto-Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,str(D/f)))
for n,f in [('EN','Arial.ttf'),('EB','Arial Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,'/System/Library/Fonts/Supplemental/'+f))
ink='#18233B';paper='#F5F3ED';blue='#3259DC';muted='#58657A';white='#FFFFFF';orange='#F8895C';lime='#E4F0AE';line='#DBDFE7'
c=canvas.Canvas('output/pdf/Eli_项目案例集_视觉重制版.pdf',pagesize=(W,H),pageCompression=1)
c.setTitle('Eli | 业务与产品精选案例');c.setAuthor('Eli')
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
def photo(n,x,y,w,h):c.drawImage(ImageReader(str(D/(n+'.png'))),x,H-y-h,width=w,height=h,mask='auto')
def lineat(x,y,w,col=line):box(x,y,w,1,col)
def base(n,label,bg=paper):
 box(0,0,W,H,bg);dark=bg in [ink,blue];co=white if dark else ink
 txt(38,24,'ELI',19,co,'EB');txt(93,30,'SELECTED WORK',9,co,'EN');txt(38,567,label,10,co,'EN');txt(886,562,f'{n:02}',19,co,'EN')
def label(x,y,s,bg=blue,fg=white):
 box(x,y,pdfmetrics.stringWidth(s,'CN',11)+22,27,bg,3);txt(x+11,y+6,s,11,fg)
def end():c.showPage()
# 01 cover: architectural editorial collage
base(1,'BUSINESS / DIGITAL / PRODUCT',ink)
box(38,103,51,5,orange);txt(38,142,'把业务想法',47,white,'CB');txt(38,209,'做成看得见的成果',39,white,'CB')
wrap(41,294,'网站开发 · 企业协同 · 全域营销\n业务验收 · 交互原型 · 独立产品',447,17,'#BAC8E3',31)
txt(40,437,'Eli',31,lime,'EB');txt(40,484,'业务与产品精选案例',21,white,'CB')
box(564,85,356,411,blue,16)
photo('foundation',587,111,310,157);photo('lawfirm',587,283,310,157)
label(587,456,'参与开发 / 项目实践',lime,ink)
end()
#02 index magazine
base(2,'EXPERIENCE MAP')
txt(38,89,'从对外连接，到内部协同。',36,ink,'CB')
wrap(39,147,'跨行业项目实践，围绕业务理解、数字化建设与产品迭代展开。',830,16)
sections=[('01','品牌与增长','公益基金会官网 / 律师事务所官网\n英国滤水器企业全域营销',blue),('02','流程与系统','律师事务所 OA / 库存业务验收\nAI 辅助录单交互原型',ink),('03','独立产品','Pocket Rove\niOS 产品设计与持续迭代',orange)]
for i,(n,h,bgtext,col) in enumerate(sections):
 y=226+i*102;txt(39,y,n,42,col,'EB');txt(137,y+4,h,25,ink,'CB');wrap(460,y+5,bgtext,440,14,muted,25);lineat(137,y+77,783)
end()
#03/04 sites broad image plates
for n,nm,title,sub,im,url,features,col in [(3,'公益机构官网','深圳市予善佑公益基金会','参与开发','foundation','https://ysy.ovops.com/','机构介绍  /  公益项目  /  新闻动态  /  信息公开',blue),(4,'专业服务机构官网','广东卓建（光明）律师事务所','参与开发','lawfirm','https://zj.ovops.com/','专业领域  /  律师团队  /  资讯文章  /  中英文入口',ink)]:
 base(n,'WEBSITE DEVELOPMENT',col)
 txt(38,77,title,29,white,'CB');txt(39,123,nm+'  ·  '+sub,14,'#CED8F1')
 photo(im,125,161,710,360)
 txt(39,534,features,11,white)
 txt(565,566,url,11,'#CED8F1','EN');c.linkURL(url,(562,15,850,40),relative=0)
 end()
#05 marketing circle visual
base(5,'INTEGRATED MARKETING')
label(38,83,'英国滤水器企业 / 全域营销')
txt(38,139,'把产品带入',38,ink,'CB');txt(38,193,'更完整的市场触点。',38,ink,'CB')
wrap(39,278,'参与英国滤水器企业全域营销项目，积累海外市场与营销协同经验。',355,17,muted,29)
lineat(39,411,350);txt(39,432,'净水产品 × 英国市场',21,blue,'CB');txt(39,478,'海外业务与营销实践',15,muted)
# concept circles, explicitly conceptual by heading
box(440,83,480,441,'#E5EAFE',15);txt(466,107,'营销协同视角',17,blue,'CB')
c.setStrokeColor(HexColor('#B7C7F5'));c.setLineWidth(2)
c.circle(680,H-315,155,fill=0,stroke=1);c.circle(680,H-315,109,fill=0,stroke=1)
for x,y,s,co in [(488,192,'产品表达',ink),(736,224,'内容触点',blue),(717,401,'反馈复盘',ink),(479,375,'咨询转化',blue)]:
 box(x,y,150,63,co,10);txt(x+19,y+18,s,22,white,'CB')
box(603,281,157,71,orange,12);txt(630,302,'市场连接',23,ink,'CB')
end()
#06 OA dark typographic
base(6,'INTERNAL SYSTEMS',ink)
label(38,83,'律师事务所 / OA 系统搭建',lime,ink)
txt(38,142,'让工作协同',40,white,'CB');txt(38,198,'有清晰的组织方式。',36,white,'CB')
wrap(39,289,'律师事务所 OA 系统搭建经历，延伸专业服务机构的内部数字化能力。',372,17,'#BCCAE0',30)
txt(39,459,'法律专业服务',22,lime,'CB');txt(39,498,'从机构展示，走向内部办公。',15,'#BCCAE0')
txt(476,107,'协同设计视角',17,'#BCCAE0','CB')
for i,(h,b) in enumerate([('人','谁发起，谁处理'),('流程','工作如何流转'),('信息','内容如何组织'),('状态','进展如何可见')]):
 y=157+i*89;box(469,y,449,73,['#2B3C5C','#324A71','#3B567E','#45648C'][i],8);txt(491,y+13,h,29,white,'CB');txt(650,y+26,b,16,'#E1E9F6')
end()
#07 ERP editorial numeral
base(7,'BUSINESS VALIDATION')
label(38,82,'库存系统 / 业务验收')
txt(38,132,'从页面操作，验到业务结果。',33,ink,'CB')
wrap(39,192,'围绕采购、发货、退换货与盘点，检查业务状态和库存变化的一致性。',837,17)
box(38,255,250,278,blue,12);txt(59,275,'09',99,white,'EB');txt(62,400,'项问题反馈',25,white,'CB');wrap(62,448,'已反馈给开发\n待修复后逐项复查',208,14,'#DFE7FF',25)
txt(331,261,'典型问题',14,blue,'CB');txt(331,297,'货物未入仓，库存却增加。',27,ink,'CB')
wrap(331,344,'将异常操作整理成复现步骤、实际结果与期望结果，帮助开发定位业务偏差。',570,16,muted,28)
for i,(h,b) in enumerate([('业务地图','厘清角色与路径'),('复现记录','说明触发与偏差'),('反馈清单','支持后续复查')]):
 x=331+i*201;lineat(x,432,185);txt(x,457,h,20,ink,'CB');txt(x,494,b,13,muted)
end()
#08 prototype no imaginary results
base(8,'WORKFLOW PROTOTYPE')
label(38,81,'AI 录单 / 交互原型')
txt(38,130,'把审核流程，做成可操作的原型。',32,ink,'CB')
wrap(39,190,'从单据上传到字段校验，明确每一步输入、操作与人工判断。',850,17)
box(38,257,564,273,ink,12)
for i,(a,b) in enumerate([('01','上传单据'),('02','查看字段'),('03','人工校验'),('04','确认记录')]):
 y=275+i*60;txt(60,y,a,22,orange,'EB');txt(112,y,b,19,white,'CB');lineat(263,y+15,303,'#42516A')
txt(637,265,'原型交付内容',22,ink,'CB');wrap(637,314,'关键页面与交互路径\n字段映射与校验设计\n功能范围与确认问题',280,16,muted,34)
label(637,447,'React + TypeScript',blue,white)
end()
#09 product poster bigger designed
base(9,'INDEPENDENT PRODUCT',orange)
txt(38,88,'Pocket',64,ink,'EB');txt(38,153,'Rove',64,ink,'EB')
txt(40,258,'把日常，变成一次小冒险。',27,ink,'CB')
wrap(41,327,'围绕任务发现、完成反馈、历史回看与纪念品体验，持续推进产品设计与实现。',460,17,ink,29)
lineat(40,449,452,ink);txt(40,468,'产品设计 / 双语体验 / iOS 实现',17,ink,'CB');txt(40,507,'版本迭代 · 测试验证 · 上架流程实践',14,ink)
img='/Volumes/EXTERNAL/app/Pocket-Rove-人工上传-五张截图-20260911/2-今日任务-Today.png'
c.drawImage(ImageReader(img),634,H-70-476,width=220,height=476,mask='auto')
end()
#10 closing oversized typography
base(10,'LET’S BUILD SOMETHING USEFUL',blue)
txt(38,102,'下一步，',51,white,'CB');txt(38,173,'从你的一个业务问题开始。',38,white,'CB')
wrap(40,265,'带来一个具体场景。一起确定范围、交付成果与验收方式，\n从一轮付费试点开始推进。',850,19,'#E2E8FF',33)
for i,(h,b) in enumerate([('沟通场景','现在怎么做，卡在哪里'),('明确方案','做什么，何时交付，如何验收'),('推进试点','先验证，再决定下一步投入')]):
 x=40+i*296;lineat(x,385,269,'#7894F5');txt(x,414,h,25,white,'CB');wrap(x,459,b,265,14,'#E2E8FF',25)
txt(40,527,'联系 Eli  /  回复资料发送人，预约业务沟通。',16,lime,'CB')
end();c.save()
# Check every authored glyph exists in the embedded Chinese typeface.
cn=pdfmetrics.getFont('CN').face.charToGlyph
missing=sorted({ch for s in all_text for ch in s if ord(ch)>127 and ord(ch) not in cn})
print('missing_glyphs',missing)
print(Path('output/pdf/Eli_项目案例集_视觉重制版.pdf').resolve())
