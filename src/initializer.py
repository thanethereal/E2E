class IncludeAPIRouter(object):
    def __new__(cls):
        from routers.health_check import router as router_health_check
        from fastapi.routing import APIRouter


        router = APIRouter()

        router.include_router(router_health_check, tags=['Health Check'])

        return router
