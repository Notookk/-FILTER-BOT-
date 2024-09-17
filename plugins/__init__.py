# Don't Remove Credit @xazoc
# Subscribe YouTube Channel For Amazing Bot @ll_about_ari_ll
# Ask Doubt on telegram @xazoc

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
