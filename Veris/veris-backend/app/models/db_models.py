from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database import Base


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    transaction_id = Column(
        String,
        unique=True,
        index=True
    )

    customer_id = Column(
        String,
        index=True
    )

    transaction_amount = Column(
        Float
    )

    merchant_category = Column(
        String
    )

    device_type = Column(
        String
    )

    email_domain_type = Column(
        String
    )

    previous_transaction_count = Column(
        Integer
    )

    fraud_score = Column(
        Float
    )

    credit_score = Column(
        Float
    )

    credit_risk = Column(
        Float
    )

    unified_risk_score = Column(
        Float
    )

    risk_tier = Column(
        String,
        index=True
    )

    decision = Column(
        String,
        index=True
    )

    review_status = Column(
        String,
        default="PENDING"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    transaction_id = Column(
        String,
        index=True
    )

    action = Column(
        String
    )

    performed_by = Column(
        String
    )

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

class UploadBatch(Base):

    __tablename__ = "upload_batches"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    file_name = Column(
        String
    )

    status = Column(
        String,
        default="PROCESSING"
    )

    total_records = Column(
        Integer,
        default=0
    )

    processed_records = Column(
        Integer,
        default=0
    )