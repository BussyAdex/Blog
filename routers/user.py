from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import schemas, database
from repository import user


get_db = database.get_db
router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', status_code= status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', status_code= status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)