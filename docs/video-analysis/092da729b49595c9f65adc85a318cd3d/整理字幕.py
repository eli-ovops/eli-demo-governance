import json, re, difflib
from pathlib import Path
P = Path(__file__).resolve().parent
full = json.loads((P/'ocr.json').read_text())
bottom = [json.loads(x) for x in (P/'captions_1s.jsonl').read_text().splitlines()]

def background(t):
    return bool(re.fullmatch(r'.{0,3}(?:抖音|排音|拌音|料音|搾音)', t) or
                re.search(r'抖音号：|木子不写代码|创作.{0,2}大会|創作.{0,2}大会',t) or
                re.fullmatch(r'.{0,2}(?:maono|maona|naono|aono|maol|ODU|OUODU|COno|COnO|COnC).{0,4}',t,re.I) or
                re.fullmatch(r'.{0,3}(?:视频|视築|契频|槊频|钢频|郷频|视郷|契频|契频|契频).{0,3}(?:客|寄|吝)',t) or
                re.fullmatch(r'.{0,2}(?:获持|扶持|保持|天持|祆持)计划',t) or
                re.fullmatch(r'(?:Doy|Dog|Dou|Day|Doe|Dop|Dae|Dse|Dege|Dour|Doar|Dye).{0,30}',t))

def clean(ts):
    return [t for t in ts if not background(t)]

rows=[]
last_b=None
for r in bottom:
    n=int(r['time']); b=clean(r['text']); fr=full[n//2] if n%2==0 else None
    near=[t for rr in bottom[max(0,n-1):n+2] for t in clean(rr['text'])]
    f=[]
    if fr:
        for t in clean(fr['text']):
            if t in near: continue
            if any(difflib.SequenceMatcher(None,t,s).ratio()>=0.87 for s in near): continue
            f.append(t)
    if b!=last_b or f:
        rows.append({'time':n,'B':b,'F':f})
    last_b=b
(P/'合并候选.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
for start in range(0,6000,300):
    selected=[r for r in rows if start<=r['time']<start+300]
    lines=[]
    for r in selected:
        n=r['time']; stamp=f'{n//3600:02}:{n//60%60:02}:{n%60:02}'
        if r['B']: lines.append(stamp+' B '+' / '.join(r['B']))
        if r['F']: lines.append(stamp+' F '+' / '.join(r['F']))
    (P/f'阅读批次_{start:04}.txt').write_text('\n'.join(lines))
print('merged rows',len(rows),'batches',20)
