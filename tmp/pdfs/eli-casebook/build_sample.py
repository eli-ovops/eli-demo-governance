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
c=canvas.Canvas('output/pdf/Eli_案例集_设计样张.pdf',pagesize=(W,H),pageCompression=1)
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

# Cover
box(0,0,W,H,'#EFE7D8')
c.drawImage(ImageReader('output/pdf/assets/cover-architecture.png'),0,-20,width=960,height=640,mask='auto')
txt(42,32,'ELI',21,ink,'EB');txt(42,74,'BUSINESS & PRODUCT',10,ink,'EN')
txt(42,190,'连接业务，',47,ink,'CB');txt(42,246,'构建产品。',47,ink,'CB')
box(44,333,42,3,'#916C39')
wrap(43,360,'网站开发 · 企业协同 · 全域营销\n业务验收 · 交互原型 · 独立产品',388,15,ink,26)
txt(43,524,'项目实践 / 精选案例',15,ink,'CB');txt(43,565,'PORTFOLIO  /  2026',10,ink,'EN')
end()
# Water marketing editorial
box(0,0,W,H,'#F3EDE2')
c.drawImage(ImageReader('output/pdf/assets/water-editorial.png'),0,0,width=400,height=600,mask='auto')
txt(446,35,'ELI  /  SELECTED WORK',10,ink,'EB');txt(446,115,'英国滤水器企业',15,'#896A43','CB')
txt(444,155,'从产品，',39,ink,'CB');txt(444,207,'走向更完整的市场。',32,ink,'CB')
lineat(447,290,459,'#C6B9A3')
wrap(447,320,'参与英国滤水器企业全域营销项目，积累海外市场与营销协同经验。',444,17,ink,28)
txt(447,425,'项目类型',12,'#896A43','CB');txt(595,425,'全域营销',16,ink,'CB')
lineat(447,465,459,'#C6B9A3');txt(447,486,'行业 / 市场',12,'#896A43','CB');txt(595,486,'净水产品 / 英国',16,ink,'CB')
txt(447,565,'INTEGRATED MARKETING',10,ink,'EN');txt(888,558,'02',17,ink,'EN')
end();c.save()
Path('tmp/pdfs/eli-casebook/sample-text.txt').write_text(''.join(all_text))
print('sample exported')
