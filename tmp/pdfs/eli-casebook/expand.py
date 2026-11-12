from pathlib import Path
import json,base64
f=Path('/Users/USER/.codex/sessions/2026/09/06/rollout-2026-09-06T10-34-15-01a07491-0287-7072-b0d4-c1ba06b2a83d.jsonl')
imgs=[]
for ln in f.open():
 d=json.loads(ln);p=d.get('payload',{})
 if d.get('type')=='response_item' and p.get('role')=='user':
  for it in p.get('content',[]):
   if it.get('type')=='input_image' and it.get('image_url','').startswith('data:image/png;base64,'):imgs.append(it['image_url'])
for nm,im in zip(['foundation','lawfirm'],imgs[-2:]):
 Path('tmp/pdfs/eli-casebook/'+nm+'.png').write_bytes(base64.b64decode(im.split(',',1)[1]))
p=Path('tmp/pdfs/eli-casebook/build.py');s=p.read_text()
s=s.replace("OUT=Path('output/pdf/Eli_AI业务落地_精选案例.pdf')","OUT=Path('output/pdf/Eli_AI业务落地_精选案例_扩展版.pdf')")
s=s.replace('以下为精选项目实践，分别展示业务验收、流程原型与独立产品。','精选经历涵盖网站开发、全域营销、OA 搭建、业务验收、流程原型与独立产品。')
s=s.replace("base(3,'CASE 01 / BUSINESS VALIDATION')","base(7,'CASE 05 / BUSINESS VALIDATION')").replace("base(4,'CASE 02 / WORKFLOW PROTOTYPE')","base(8,'CASE 06 / WORKFLOW PROTOTYPE')").replace("base(5,'CASE 03 / INDEPENDENT PRODUCT')","base(9,'CASE 07 / INDEPENDENT PRODUCT')").replace("base(6,'START WITH ONE WORKFLOW',True)","base(10,'START WITH ONE WORKFLOW',True)")
insert='''# Additional experience
for n,name,head,desc,img,url,items in [
 (3,'公益机构官网 · 参与开发','深圳市予善佑公益基金会','让机构介绍、公益项目与公开信息，拥有清晰的展示入口。','foundation','https://ysy.ovops.com/',['机构介绍 / 公益项目','新闻动态 / 信息公开','志愿参与 / 联系入口']),
 (4,'律师事务所官网 · 参与开发','广东卓建（光明）律师事务所','围绕专业服务品牌，呈现业务领域、团队与资讯内容。','lawfirm','https://zj.ovops.com/',['专业领域 / 律师名录','资讯文章 / 机构文化','联系入口 / 中英文入口'])]:
 base(n,f'CASE {n-2:02d} / WEBSITE DEVELOPMENT')
 tag(44,80,name)
 txt(44,118,head,30,ink,'CB')
 txt(44,163,desc,15,muted)
 # original user-provided screenshot, kept intact
 c.drawImage(ImageReader('tmp/pdfs/eli-casebook/'+img+'.png'),44,H-210-278,width=548,height=278,mask='auto')
 txt(622,217,'页面展示',17,ink,'CB')
 for j,it in enumerate(items):
  rule(622,251+j*51,292);txt(622,269+j*51,it,14,ink)
 txt(622,425,'参与方式',13,teal,'CB')
 wrap(622,450,'参与网站开发。展示范围以提供的页面为准，保留原项目品牌归属。',283,13,muted,22)
 txt(44,510,url,11,teal,'EN')
 c.linkURL(url,(44,H-525,430,H-504),relative=0)
 txt(44,533,'图片：本人提供的项目页面截图。网站机构数据不作为个人开发业绩指标。',10,muted)
 end()
base(5,'CASE 03 / INTEGRATED MARKETING')
tag(44,82,'英国滤水器企业 · 全域营销参与经历')
txt(44,124,'从产品表达，到跨渠道营销协同。',32,ink,'CB')
wrap(44,180,'参与英国滤水器企业的全域营销项目。将这段经历作为海外业务与营销实践的一部分，支持围绕客户触点讨论整体方案。',377,15,muted,25)
txt(44,297,'项目经验',18,ink,'CB')
wrap(44,330,'行业：滤水器 / 净水产品\\n市场：英国\\n项目类型：全域营销',368,15,muted,30)
box(456,183,460,294,white,12)
txt(480,205,'营销协同视角',18,ink,'CB');txt(480,236,'示意框架 · 非项目渠道清单或业绩数据',11,muted)
for j,(h,b) in enumerate([('产品表达','说明产品与使用场景'),('触点协同','连接内容与咨询入口'),('反馈复盘','根据反馈持续调整')]):
 yy=281+j*59;box(480,yy,58,37,teal,5);txt(497,yy+10,f'{j+1:02d}',16,white,'EB');txt(555,yy,h,16,ink,'CB');txt(555,yy+25,b,12,muted)
wrap(44,512,'匿名展示参与经历；右图为沟通框架示意，不声称具体投放渠道、预算、销售额或转化提升。',865,11,muted,18)
end()
base(6,'CASE 04 / INTERNAL SYSTEMS')
tag(44,82,'律师事务所 · OA 系统搭建经历')
txt(44,124,'从对外展示，延伸到内部办公协同。',32,ink,'CB')
wrap(44,180,'具备律师事务所 OA 系统搭建经历。与机构官网面向公众的展示不同，内部系统建设关注日常工作的组织与协同。',375,15,muted,25)
txt(44,299,'项目经验',18,ink,'CB')
wrap(44,333,'行业：法律专业服务\\n项目类型：内部办公系统\\n参与方向：OA 系统搭建',373,15,muted,30)
box(456,183,460,294,white,12);txt(480,205,'内部协同设计视角',18,ink,'CB');txt(480,236,'能力示意 · 非真实 OA 系统截图',11,muted)
for x,y,h,b in [(480,282,'人','谁发起与处理'),(693,282,'流程','如何流转工作'),(480,367,'信息','需要哪些内容'),(693,367,'状态','进展如何可见')]:
 box(x,y,197,69,'#EAF0E7',6);txt(x+14,y+13,h,21,teal,'CB');txt(x+49,y+24,b,13,ink)
wrap(44,512,'匿名展示搭建经历；具体系统模块、技术方案与验收结果按实际项目另行说明，不展示内部业务数据。',865,11,muted,18)
end()
'''
s=s.replace('# ERP\n',insert+'\n# ERP\n')
Path('tmp/pdfs/eli-casebook/build_expanded.py').write_text(s)
