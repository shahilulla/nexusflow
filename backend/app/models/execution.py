from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Execution(Base):
    __tablename__ = "executions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    pipeline_id: Mapped[int] = mapped_column(ForeignKey("pipelines.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
