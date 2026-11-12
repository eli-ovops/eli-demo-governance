import sqlite3,json,datetime,collections,re,statistics,csv
from pathlib import Path
O=Path('output/额度审计_2026-09-18');start=1790033128-604800;cut=datetime.datetime.now().timestamp()
c=sqlite3.connect('file:/Users/USER/.codex/state_5.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
rows=[dict(r) for r in c.execute('select id,rollout_path,title,name,model,reasoning_effort,cwd,updated_at from threads where updated_at>=?',(start-86400,))]
records={};contexts={};requests={};tc=collections.Counter();toolnames=collections.Counter();errs=collections.Counter()
def ts(s):
 try:return datetime.datetime.fromisoformat(s.replace('Z','+00:00')).timestamp()
 except:return 0
def safe(s):
 s=re.sub(r'(?im)^.*(?:密码|password|api[_ -]?key|secret|私钥|助记词|Bearer).*$','[敏感行略]',s)
 return re.sub(r'\s+',' ',s)[:180]
for r in rows:
 context={};turn='';user=''
 for line in open(r['rollout_path']):
  if len(line)>2000000:continue
  if not any(t in line[:200] for t in ['turn_context','response_item','event_msg','token_usage_record']):continue
  try:o=json.loads(line)
  except:continue
  p=o.get('payload',{});typ=o.get('type');stamp=ts(o.get('timestamp',''))
  if typ=='turn_context':
   context={k:p.get(k) for k in ['model','effort','service_tier']};turn=p.get('turn_id','');contexts[(r['id'],turn)]=context
  if not start<=stamp<=cut:continue
  if typ=='response_item' and p.get('role')=='user':
   s='\n'.join(v.get('text','') for v in p.get('content',[]) if isinstance(v,dict))
   if not s.startswith(('<recommended','# AGENTS','<environment_context','<permissions','<INSTRUCTIONS')):
    user=safe(s);requests[(r['id'],turn)]=user
  if typ=='response_item' and p.get('type') in ['function_call','custom_tool_call']:
   name=p.get('name','unknown');toolnames[name]+=1;tc[r['id']]+=1
  if typ=='token_usage_record':
   rid=p.get('response_id')
   if not rid:continue
   tid=p.get('thread_id',r['id']);trn=p.get('turn_id',turn);u=p.get('usage',{})
   records[rid]={'id':tid,'turn':trn,'root_turn':p.get('root_turn_id'),'timestamp':o.get('timestamp'),**context,**u,'request':requests.get((tid,trn),user),'response_id':rid}
# Best metadata; user titles may be raw prompts, so bounded.
meta={r['id']:r for r in rows};groups=collections.defaultdict(list)
for v in records.values():groups[v['id']].append(v)
summary=[]
for tid,rr in groups.items():
 m=meta.get(tid,{});d={'id':tid,'title':safe(m.get('name') or m.get('title','')),'cwd':m.get('cwd',''),'calls':len(rr),'turns':len({v['turn'] for v in rr}),'tools_in_file':tc[tid]}
 for k in ['input_tokens','cached_input_tokens','output_tokens','reasoning_output_tokens','total_tokens']:d[k]=sum(v.get(k,0) for v in rr)
 d['uncached_input']=d['input_tokens']-d['cached_input_tokens'];d['avg_context']=round(d['input_tokens']/len(rr));d['max_context']=max(v.get('input_tokens',0) for v in rr)
 d['model_effort']=dict(collections.Counter(str(v.get('model'))+'/'+str(v.get('effort')) for v in rr));summary.append(d)
summary.sort(key=lambda d:d['uncached_input'],reverse=True)
(O/'逐次请求.json').write_text(json.dumps(list(records.values()),ensure_ascii=False,indent=2));(O/'任务汇总.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
with (O/'任务汇总.csv').open('w',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
print('files',len(rows),'responses',len(records),'threads',len(summary),'window',datetime.datetime.fromtimestamp(start),datetime.datetime.fromtimestamp(cut))
print('TOTAL', {k:sum(x.get(k,0) for x in summary) for k in ['input_tokens','cached_input_tokens','uncached_input','output_tokens','reasoning_output_tokens','total_tokens']})
print('MODEL EFFORT',dict(collections.Counter(str(v.get('model'))+'/'+str(v.get('effort')) for v in records.values())))
print('SERVICE',dict(collections.Counter(str(v.get('service_tier')) for v in records.values())))
for d in summary[:18]:print(json.dumps(d,ensure_ascii=False))
print('TOOLS',toolnames.most_common(12))
