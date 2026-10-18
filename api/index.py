"""
Vercel serverless entrypoint for KEY MD Bot (webhook mode).
Preserves all original Rose/KEY MD modules and functions.
"""
import os
import sys
import json
import logging
from http.server import BaseHTTPRequestHandler

# Project root
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

# Force environment for Vercel
os.environ.setdefault("ENV", "ANYTHING")
os.environ.setdefault("WEBHOOK", "True")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
LOGGER = logging.getLogger("keymd")

# Lazy import to avoid cold-start issues as much as possible
_dispatcher = None

def get_dispatcher():
    global _dispatcher
    if _dispatcher is None:
        from tg_bot import dispatcher
        _dispatcher = dispatcher
        # Import all modules so handlers are registered
        import tg_bot.__main__  # noqa: F401 – side-effect: loads modules
    return _dispatcher


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "status": "ok",
            "bot": "KEY MD",
            "message": "KEY MD Bot webhook is alive. Set Telegram webhook to this URL."
        }).encode())

    def do_POST(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode("utf-8"))

            from telegram import Update
            dispatcher = get_dispatcher()
            update = Update.de_json(data, dispatcher.bot)
            dispatcher.process_update(update)

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")
        except Exception as e:
            LOGGER.exception("Failed to process update")
            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(str(e).encode())

    def log_message(self, format, *args):
        LOGGER.info("%s - %s", self.address_string(), format % args)
