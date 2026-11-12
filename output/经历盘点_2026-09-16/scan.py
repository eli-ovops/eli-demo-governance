import sqlite3,json,csv,re,os,datetime,collections
from pathlib import Path
O=Path('/Users/USER/Documents/eli/output/经历盘点_2026-09-16')
def clean(s):
 s=re.sub(r'(?im)^.*(?:密码|password|api[_ -]?key|secret|access[_ -]?token|私钥|助记词|账号[:：]|账户[:：]).*$', '[敏感行已省略]',s)
 s=re.sub(r'(?i)\b(?:sk-[\w-]{10,}|gh[pousr]_[\w]+|Bearer\s+\S+)','[已省略]',s)
 return s
c=sqlite3.connect('file:/Users/USER/.codex/state_5.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
rows=[dict(r) for r in c.execute('select id,cwd,title,created_at,updated_at,archived,rollout_path,first_user_message from threads order by created_at')]
for r in rows:
 for k in ['created_at','updated_at']:
  v=r[k];r[k]=datetime.datetime.fromtimestamp(v/1000 if v>1e11 else v).isoformat(timespec='seconds')
 r['title']=clean(r['title'])[:350];r['first_user_message']=clean(r['first_user_message'])[:1800]
with (O/'全部任务索引.csv').open('w',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
g=collections.defaultdict(list)
for r in rows:g[r['cwd']].append(r)
with (O/'任务分组摘录.txt').open('w') as f:
 for cwd,rr in sorted(g.items(),key=lambda kv:-len(kv[1])):
  f.write(f'\n## {cwd} ({len(rr)})\n')
  for r in rr:f.write(f"{r['created_at'][:10]} | {r['title'][:180]} | {r['id']}\n")
roots=['/Users/USER/Documents','/Users/USER/Desktop','/Users/USER/Downloads','/Users/USER/WeChatProjects','/Users/USER/乔帮主项目_移交包','/Users/USER/Pictures','/Users/USER/Movies','/Users/USER/Music','/Users/USER/Public','/Volumes/EXTERNAL','/Users/USER/Library/Application Support/Open Design/namespaces']
skip={'.git','node_modules','.next','.venv','venv','Pods','DerivedData','build','dist','coverage','__pycache__','.cache','.Trash','.Trashes','CoreSimulator','Library','runtime','Focumi-iOS17-runtime','Focumi-iOS17-DerivedData','Focumi-DeviceSupport','XCTestCloneBackups','.Spotlight-V100','.fseventsd'}
files=[];dirs=[];errors=[]
for root in roots:
 for p,ds,fs in os.walk(root,onerror=lambda e:errors.append(str(e))):
  rel=Path(p).relative_to(root);depth=len(rel.parts)
  ds[:]=[d for d in ds if d not in skip and not d.startswith('.') and depth<7]
  if depth<=3:dirs.append(p)
  for fn in fs:
   if fn.startswith('.') or any(x in fn.lower() for x in ['secret','credential','password','auth.json']):continue
   fp=Path(p)/fn
   try:st=fp.stat()
   except OSError:continue
   files.append([str(fp),st.st_size,datetime.datetime.fromtimestamp(st.st_mtime).isoformat(timespec='seconds')])
with (O/'文件索引.csv').open('w',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['path','bytes','modified']);w.writerows(files)
(O/'目录索引.txt').write_text('\n'.join(dirs))
(O/'扫描范围.json').write_text(json.dumps({'roots':roots,'excluded_dirs':sorted(skip),'max_depth':7,'thread_count':len(rows),'archived':sum(x['archived'] for x in rows),'first':rows[0]['created_at'],'file_count':len(files),'directory_count_depth3':len(dirs),'errors':errors},ensure_ascii=False,indent=2))
print('Indexed',len(rows),'threads',len(files),'files',len(dirs),'directories','errors',len(errors))
