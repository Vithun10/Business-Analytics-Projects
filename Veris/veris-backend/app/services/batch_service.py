from app.repositories.upload_batch_repository import (
    UploadBatchRepository
)


class BatchService:

    def __init__(self):

        self.repository = (
            UploadBatchRepository()
        )

    def create_batch(
        self,
        db,
        file_name
    ):

        return (
            self.repository.create(
                db,
                file_name
            )
        )

    def update_batch(
        self,
        db,
        batch_id,
        status,
        total_records,
        processed_records
    ):

        return (
            self.repository.update_status(
                db,
                batch_id,
                status,
                total_records,
                processed_records
            )
        )

    def get_batch(
        self,
        db,
        batch_id
    ):

        return (
            self.repository.get_batch(
                db,
                batch_id
            )
        )