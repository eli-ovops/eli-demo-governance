import functools
import http.server
import json
from pathlib import Path

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass

root = Path(__file__).resolve().parent
handler = functools.partial(QuietHandler, directory=str(root))
server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
print(json.dumps({"address": "127.0.0.1", "port": server.server_port}), flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
