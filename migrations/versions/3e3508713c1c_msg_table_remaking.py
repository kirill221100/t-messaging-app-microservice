"""msg table remaking

Revision ID: 3e3508713c1c
Revises: 41b385c282fe
Create Date: 2024-05-06 06:04:50.017468

"""
from typing import Sequence, Union
from sqlalchemy.ext.declarative import declarative_base
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import String, select
from db.models.message import MessageTypes
Base = declarative_base()


# revision identifiers, used by Alembic.
revision: str = '3e3508713c1c'
down_revision: Union[str, None] = '41b385c282fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[MessageTypes] = mapped_column(String(50), nullable=False)
    class_type: Mapped[str]


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('type', sa.String(length=50), nullable=True))
    op.add_column('messages', sa.Column('class_type', sa.String(), nullable=True))
    # ### end Alembic commands ###
    bind = op.get_bind()
    session = Session(bind=bind)
    messages = session.execute(select(Message)).scalars().all()
    for message in messages:
        message.type = MessageTypes.DEFAULT.value
        message.class_type = 'default_messages'

    session.commit()
    op.alter_column('messages', "type", nullable=False)
    op.alter_column('messages', "class_type", nullable=False)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'class_type')
    op.drop_column('messages', 'type')
    # ### end Alembic commands ###
