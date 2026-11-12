const {chromium}=require('/Users/USER/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{const b=await chromium.launch({channel:'chrome',headless:true});
for(const [name,url] of [['foundation','https://ysy.ovops.com/'],['lawfirm','https://zj.ovops.com/']]){
 const p=await b.newPage({viewport:{width:1440,height:1000},deviceScaleFactor:2});
 try{await p.goto(url,{waitUntil:'networkidle',timeout:30000});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:`output/pdf/assets/${name}-web-hd.png`,fullPage:true});console.log(name,await p.title(),await p.locator('body').evaluate(e=>({w:e.scrollWidth,h:e.scrollHeight})));}
 catch(e){console.log(name,e.message)}await p.close();}
await b.close();})();
