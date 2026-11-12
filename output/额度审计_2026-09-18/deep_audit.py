import json,sqlite3,collections,re,datetime,csv
from pathlib import Path
P=Path('output/额度审计_2026-09-18'); rec=json.loads((P/'逐次请求.json').read_text());wanted={v['response_id']:v for v in rec};start=min(x['timestamp'] for x in rec);end=max(x['timestamp'] for x in rec)
c=sqlite3.connect('file:/Users/USER/.codex/state_5.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
rows=[dict(x) for x in c.execute('select id,rollout_path from threads where updated_at>=?',(1790033128-691200,))]
settings={};rates=[];tools=collections.Counter();toolchars=collections.Counter();threadtools=collections.defaultdict(collections.Counter);large=[];enriched={};skips=0
for row in rows:
 tid=row['id'];setting={};turn='';calls={};pending=[];prev=None;turnfirst=set();compact_at=None
 for lineno,line in enumerate(open(row['rollout_path']),1):
  if len(line)>2000000:skips+=1;continue
  try:o=json.loads(line)
  except:continue
  p=o.get('payload',{});typ=o.get('type');sub=p.get('type');stamp=o.get('timestamp','')
  if typ=='event_msg' and sub=='thread_settings_applied':setting=p.get('thread_settings',{})
  if typ=='turn_context':turn=p.get('turn_id','')
  if typ=='compacted':compact_at=stamp
  if typ=='response_item' and sub in ['function_call','custom_tool_call']:
   name=p.get('name','?');args=p.get('arguments','') or p.get('input','');nested=re.findall(r'tools\.([a-zA-Z0-9_]+)',str(args));label=','.join(sorted(set(nested))) or name
   calls[p.get('call_id')]=label
   if start<=stamp<=end:
    tools[label]+=1;threadtools[tid][label]+=1;pending.append(label)
  if not start<=stamp<=end:continue
  if typ=='response_item' and sub in ['function_call_output','custom_tool_call_output']:
   name=calls.get(p.get('call_id'),'?');out=p.get('output','');text=out if isinstance(out,str) else json.dumps(out,ensure_ascii=False);n=len(text)
   toolchars[name]+=n
   if n>30000:large.append({'thread':tid,'tool':name,'chars':n,'timestamp':stamp,'line':lineno})
  if typ=='event_msg' and sub=='token_count':
   lim=p.get('rate_limits') or {};win=lim.get('primary') or {}
   if win.get('window_minutes')==10080 and win.get('resets_at')==1790033128:rates.append({'time':stamp,'used':win.get('used_percent'),'thread':tid})
  if typ=='token_usage_record':
   rid=p.get('response_id');v=wanted.get(rid)
   if not v:pending=[];continue
   tr=p.get('turn_id');n=v['input_tokens'];cc=v['cached_input_tokens'];out=v['output_tokens']
   z={**v,'tier_applied':setting.get('service_tier','UNKNOWN'),'first_in_turn':tr not in turnfirst,'previous_input':prev['input_tokens'] if prev else None,'previous_time':prev['timestamp'] if prev else None,'previous_effort':prev.get('effort') if prev else None,'recent_compaction':compact_at,'action_labels':pending[:],'source_line':lineno}
   z['proxy_weight']=n-cc+cc*.1+out*5
   enriched[rid]=z;turnfirst.add(tr);prev=v;pending=[]
R=list(enriched.values());S=json.loads((P/'任务汇总.json').read_text());names={x['id']:x['title'] for x in S}
for s in S:s['proxy_weight']=s['uncached_input']+.1*s['cached_input_tokens']+5*s['output_tokens']
S.sort(key=lambda x:x['proxy_weight'],reverse=True);tot=sum(x['proxy_weight'] for x in S)
print('MATCH',len(R),len(rec),'TIERS',dict(collections.Counter(x['tier_applied'] for x in R)))
parts={'uncached':sum(x['input_tokens']-x['cached_input_tokens'] for x in R),'cached_weighted':sum(x['cached_input_tokens']*.1 for x in R),'output_weighted':sum(x['output_tokens']*5 for x in R),'reasoning_subset_weighted':sum(x['reasoning_output_tokens']*5 for x in R)}
print('PROXY_PARTS',parts,'total',tot)
print('RANK')
for x in S[:10]:print(names[x['id']][:45],round(x['proxy_weight']/tot*100,2))
print('TOOLS',tools.most_common(16));print('OUTPUT_CHARACTERS',toolchars.most_common(10))
print('COLD',dict(collections.Counter('turn_first' if x['first_in_turn'] else 'within_turn' for x in R if x['cached_input_tokens']==0)))
print('COLD_EFFORT_CHANGE',sum(x['cached_input_tokens']==0 and x['previous_effort']!=x['effort'] and x['previous_effort'] is not None for x in R))
print('COLD_CONTEXT_DROP',sum(x['cached_input_tokens']==0 and x['previous_input'] is not None and x['input_tokens']<.7*x['previous_input'] for x in R))
# Daily account observations, not per-thread charges
D=collections.defaultdict(list)
for x in rates:D[x['time'][:10]].append(x['used'])
print('DAILY_QUOTA', {d:(min(v),max(v)) for d,v in D.items()})
for s in S[:6]:print('TASK_TOOLS',names[s['id']][:45],threadtools[s['id']].most_common(6))
(P/'深化逐次请求.json').write_text(json.dumps(R,ensure_ascii=False,indent=2));(P/'历史额度快照.json').write_text(json.dumps(sorted(rates,key=lambda x:x['time']),ensure_ascii=False,indent=2));(P/'工具输出体积.json').write_text(json.dumps({'characters':dict(toolchars),'large':sorted(large,key=lambda x:x['chars'],reverse=True)[:40]},ensure_ascii=False,indent=2))
(P/'参考成本排序.json').write_text(json.dumps(S,ensure_ascii=False,indent=2))
