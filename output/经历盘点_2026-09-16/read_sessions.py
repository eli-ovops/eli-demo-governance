import csv,json,re,collections,time
from pathlib import Path
O=Path('/Users/USER/Documents/eli/output/经历盘点_2026-09-16')
rows=list(csv.DictReader((O/'全部任务索引.csv').open(encoding='utf-8-sig')))
def clean(s):
 s=re.sub(r'<(?:environment_context|appshot|INSTRUCTIONS)[\s\S]*?</(?:environment_context|appshot|INSTRUCTIONS)>','',s)
 s=re.sub(r'(?im)^.*(?:密码|password|api[_ -]?key|secret|access[_ -]?token|私钥|助记词|账号[:：]|账户[:：]).*$', '[敏感行已省略]',s)
 s=re.sub(r'(?i)\b(?:sk-[\w-]{10,}|gh[pousr]_[\w]+|Bearer\s+\S+)','[已省略]',s)
 return s.strip()
out=(O/'会话内容证据.jsonl').open('w'); stats=collections.Counter();t=time.time()
for i,r in enumerate(rows):
 users=[];finals=collections.deque(maxlen=3);seen=set();skipped=0
 with open(r['rollout_path'],'rb') as f:
  for b in f:
   stats['lines']+=1
   if len(b)>2000000:skipped+=1;continue
   if b'"event_msg"' not in b and b'"response_item"' not in b:continue
   if not any(k in b for k in [b'"role":"user"',b'"role": "user"',b'"role":"assistant"',b'"role": "assistant"',b'"agent_message"']):continue
   try:o=json.loads(b)
   except Exception:stats['bad_json']+=1;continue
   p=o.get('payload',{});s=''
   if o.get('type')=='response_item' and p.get('role')=='user':
    s=clean('\n'.join(v.get('text','') for v in p.get('content',[]) if isinstance(v,dict)))
    if s.startswith(('# AGENTS.md','<environment_context>','<permissions','<INSTRUCTIONS>')):continue
    if s and s not in seen:
     seen.add(s);users.append({'date':o.get('timestamp',''),'text':s[:1500]})
   elif p.get('role')=='assistant' and p.get('channel') in [None,'final']:
    s=clean('\n'.join(v.get('text','') for v in p.get('content',[]) if isinstance(v,dict)))
    if s:finals.append({'date':o.get('timestamp',''),'text':s[:2400]})
 r.update(user_messages=users,last_finals=list(finals),oversized_lines_skipped=skipped)
 out.write(json.dumps(r,ensure_ascii=False)+'\n');stats['users']+=len(users);stats['oversized']+=skipped
 if (i+1)%400==0:print(i+1,'/',len(rows),'seconds',round(time.time()-t),flush=True)
out.close();stats['threads']=len(rows);stats['seconds']=round(time.time()-t)
(O/'会话扫描统计.json').write_text(json.dumps(dict(stats),indent=2));print(dict(stats),flush=True)
