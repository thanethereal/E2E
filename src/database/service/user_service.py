from typing import Optional

from database.models.user import User
from database.schema import schemas
from database.common.base import session_factory


def get_all_user() -> Optional[list]:
    list_users = []
    session = session_factory()
    users = session.query(User).all()
    session.close()

    if users:
        for user in users:
            list_users.append(
                {
                    'user_id': user.user_id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'phone_number': user.phone_number,
                    'passcode': user.passcode,
                    'is_active': user.is_active,
                }
            )
        return list_users
    return None


def get_user_by_id(user_id: int) -> Optional[User]:
    session = session_factory()
    query_user = session.query(User).filter(User.user_id == user_id).first()
    session.close()
    return query_user


def get_user_by_phone_number(phone_number: str) -> Optional[User]:
    session = session_factory()
    query_user = session.query(User).filter(User.phone_number == phone_number).first()
    session.close()
    return query_user


def insert_user(object_user: schemas.User) -> None:
    session = session_factory()
    object_user = User(**object_user.dict())
    session.add(object_user)
    session.commit()
    session.refresh(object_user)
    session.close()
