from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session

from app.database import get_db

from app.services.export_service import (
    ExportService
)

import io

router = APIRouter()


@router.get(
    "/reports/export/json"
)
def export_json(
    db: Session = Depends(get_db)
):

    return (
        ExportService()
        .export_json(db)
    )


@router.get(
    "/reports/export/csv"
)
def export_csv(
    db: Session = Depends(get_db)
):

    df = (
        ExportService()
        .export_csv(db)
    )

    stream = io.StringIO()

    df.to_csv(
        stream,
        index=False
    )

    response = StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv"
    )

    response.headers[
        "Content-Disposition"
    ] = (
        "attachment; "
        "filename=veris_transactions.csv"
    )

    return response