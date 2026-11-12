import https from 'node:https';

const started = Date.now();
const outcome = await new Promise(resolve => {
  let done = false;
  const finish = value => {
    if (done) return;
    done = true;
    resolve({...value, elapsedMs: Date.now() - started});
  };
  const req = https.request('https://ab.chatgpt.com/', {method: 'HEAD'}, res => {
    finish({connected: true, tlsAuthorized: res.socket.authorized,
            httpStatus: res.statusCode});
    res.resume();
  });
  const deadline = setTimeout(() => req.destroy(new Error('PROBE_DEADLINE_5000MS')), 5000);
  req.once('close', () => clearTimeout(deadline));
  req.once('error', error => finish({connected: false,
                                   error: error.code || error.message}));
  req.end();
});
process.stdout.write(JSON.stringify(outcome) + '\n');
