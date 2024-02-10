from fastapi import Depends, APIRouter
from fastapi import status
import schemas, database, OAuth2
from sqlalchemy.orm import Session
from repository import blog


get_db = database.get_db
router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.create(request, db)
    
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.get_all(db)

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.show(id, db)