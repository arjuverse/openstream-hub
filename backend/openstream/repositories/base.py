from typing import Generic, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    def get(self, db: Session, object_id: int) -> ModelType | None:
        return db.get(self.model, object_id)

    def get_all(self, db: Session) -> list[ModelType]:
        return db.query(self.model).all()

    def create(self, db: Session, obj: ModelType) -> ModelType:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, obj: ModelType) -> None:
        db.delete(obj)
        db.commit()

    def count(self, db: Session) -> int:
        return db.query(self.model).count()

    def exists(self, db: Session, object_id: int) -> bool:
        return db.get(self.model, object_id) is not None
