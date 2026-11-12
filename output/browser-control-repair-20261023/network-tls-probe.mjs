import tls from 'node:tls';
import http from 'node:http';
import fs from 'node:fs';
import {performance} from 'node:perf_hooks';

const target='ab.chatgpt.com';
function handshake(route) {
  return new Promise(resolve=>{
    const started=performance.now(); let raw,secured,request,finished=false;
    const finish=(success,errorCode)=>{
      if(finished)return;finished=true;clearTimeout(timer);
      secured?.destroy();raw?.destroy();request?.destroy();
      resolve({route,success,errorCode:errorCode??null,elapsedMs:Math.round(performance.now()-started)});
    };
    const timer=setTimeout(()=>finish(false,'TLS_DEADLINE_5000MS'),5000);
    const wrap=socket=>{
      secured=tls.connect({...(socket?{socket}:{host:target,port:443}),servername:target,rejectUnauthorized:true});
      secured.once('secureConnect',()=>finish(secured.authorized,secured.authorizationError));
      secured.once('error',e=>finish(false,e.code??e.name));
    };
    if(route==='direct')wrap();
    else {
      request=http.request({host:'127.0.0.1',port:7890,method:'CONNECT',path:target+':443'});
      request.once('connect',(response,socket)=>{
        raw=socket;
        if(response.statusCode!==200){finish(false,'CONNECT_'+response.statusCode);return;}
        wrap(socket);
      });
      request.once('error',e=>finish(false,e.code??e.name));request.end();
    }
  });
}
const results=[];
results.push(await handshake('direct'));
results.push(await handshake('existing-system-proxy'));
const receipt={measuredAt:new Date().toISOString(),target,scope:'TLS handshake only; no application HTTP, credentials, or telemetry payload',results};
fs.writeFileSync(new URL('./tls-probe.json',import.meta.url),JSON.stringify(receipt,null,2));
console.log(JSON.stringify(receipt));
