from pathlib import Path
p=Path('tmp/pdfs/eli-casebook/build_fde.py');s=p.read_text()
start=s.index('# 3 and 4 website:');end=s.index('# 5 OA',start)
new='''# Website case studies: live high-resolution captures, editorial detail views.
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
viewport(f,337,387,268,150,198,995,510,285)
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
'''
s=s[:start]+new+s[end:]
s=s.replace('明确 AI 如何介入、交付内容与验收标准。','明确 AI 介入方式与验收标准。').replace('用实际流程验证效果，再决定下一步投入。','验证流程效果，决定下一步投入。')
s=s.replace('Eli_FDE_AI业务提效_精选案例.pdf','Eli_FDE_AI业务提效_案例设计版.pdf')
Path('tmp/pdfs/eli-casebook/build_redesigned.py').write_text(s)
