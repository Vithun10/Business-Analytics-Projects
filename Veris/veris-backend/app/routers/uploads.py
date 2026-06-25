from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

import pandas as pd
import traceback

from sqlalchemy.orm import Session

from app.database import get_db

from app.services.upload_validation_service import (
    UploadValidationService
)

from app.services.schema_mapping_service import (
    SchemaMappingService
)

from app.services.scoring_pipeline_service import (
    ScoringPipelineService
)

from app.services.batch_service import (
    BatchService
)

from app.services.persistence_service import (
    PersistenceService
)

from app.services.batch_service import (
    BatchService
)

from app.services.role_service import (
    require_role
)

router = APIRouter()


@router.post("/uploads")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    role=Depends(require_role("upload"))
):
    try:
        df = pd.read_csv(file.file)

        validation = UploadValidationService().validate(df)

        if not validation["valid"]:
            return validation

        batch = BatchService().create_batch(db, file.filename)

        mapped_df = SchemaMappingService().transform(df)

        scored_df = ScoringPipelineService().score(mapped_df)

        saved = PersistenceService().save_transactions(
            db,
            scored_df
        )

        BatchService().update_batch(
            db=db,
            batch_id=batch.id,
            status="COMPLETED",
            total_records=len(df),
            processed_records=saved
        )

        return {
            "batch_id": batch.id,
            "status": "COMPLETED",
            "records_processed": saved
        }

    except Exception as e:
        print("=" * 80)
        traceback.print_exc()
        print("=" * 80)
        raise

@router.get(
    "/uploads/{batch_id}/status"
)
def batch_status(
    batch_id: int,
    db: Session = Depends(get_db)
):

    batch = (
        BatchService()
        .get_batch(
            db,
            batch_id
        )
    )

    if not batch:

        return {

            "message":
            "Batch not found"
        }

    return {

        "batch_id":
            batch.id,

        "status":
            batch.status,

        "total_records":
            batch.total_records,

        "processed_records":
            batch.processed_records
    }

