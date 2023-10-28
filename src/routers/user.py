from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

from database.schema import schemas
from database.basic.main import DataBaseInstance
from database.service.user_service import insert_user
import logging

_ = DataBaseInstance()
router = APIRouter(prefix='/user')


@router.post("/create-user")
async def create_user(new_user: schemas.User) -> JSONResponse:
    logging.info('event={} message="{}"'
                .format('create-new-user',
                        'Create new user'))
    insert_user(new_user)
    return JSONResponse(content={'result': new_user.dict()}, status_code=200)
