class IncludeAPIRouter(object):
    def __new__(cls):
        from routers.health_check import router as router_health_check
        from routers.user import router as router_user
        from fastapi.routing import APIRouter

        router = APIRouter()

        router.include_router(router_health_check, tags=['Health Check'])
        router.include_router(router_user, prefix='/api/v1', tags=['User'])
        return router
