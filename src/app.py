import uvicorn
from fastapi import FastAPI
from initializer import IncludeAPIRouter
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from utils.config_utils import get_common_config
import logging

config = get_common_config("./src/config/default.yml")
api_config = config["api"]
def get_application():
    _app = FastAPI(title=api_config['name'],
                   description=api_config['description'],
                   version=api_config['version'],
                   debug=api_config['debug_mode'])
    _app.include_router(IncludeAPIRouter())

    origins = ["*"]

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app


app = get_application()


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')


@app.on_event("shutdown")
async def app_shutdown():
    # on app shutdown do something probably close some connections or trigger some event
    logging.info('event={} message="{}"'.format('app-shutdown', 'All connections are closed.'))


if __name__ == '__main__':
    uvicorn.run("app:app",
                host=api_config['host'],
                port=api_config['port'],
                )
