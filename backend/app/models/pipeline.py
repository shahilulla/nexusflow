import uuid

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Pipeline(Base):
    __tablename__ = "pipelines"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    description = Column(
        Text,
        nullable=True,
    )

    pipeline_type = Column(
        String(30),
        nullable=False,
        default="ETL",
    )

    schedule = Column(
        String(100),
        nullable=True,
    )

    version = Column(
        Integer,
        nullable=False,
        default=1,
    )

    status = Column(
        String(20),
        nullable=False,
        default="ACTIVE",
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_by = Column(
        String(100),
        nullable=True,
    )

    updated_by = Column(
        String(100),
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )