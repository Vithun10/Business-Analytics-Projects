from sqlalchemy.orm import Session

from app.models.db_models import UploadBatch


class UploadBatchRepository:

    def create(
        self,
        db: Session,
        file_name: str
    ):

        batch = UploadBatch(
            file_name=file_name,
            status="PROCESSING"
        )

        db.add(batch)

        db.commit()

        db.refresh(batch)

        return batch

    def update_status(
        self,
        db: Session,
        batch_id: int,
        status: str,
        total_records: int,
        processed_records: int
    ):

        batch = (
            db.query(UploadBatch)
            .filter(
                UploadBatch.id == batch_id
            )
            .first()
        )

        if batch:

            batch.status = status

            batch.total_records = (
                total_records
            )

            batch.processed_records = (
                processed_records
            )

            db.commit()

        return batch

    def get_batch(
        self,
        db: Session,
        batch_id: int
    ):

        return (
            db.query(UploadBatch)
            .filter(
                UploadBatch.id == batch_id
            )
            .first()
        )