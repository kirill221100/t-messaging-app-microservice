"""delete name and surname in users

Revision ID: 0bcf82f6a8e9
Revises: 27483580f233
Create Date: 2024-06-11 13:26:31.135395

"""
import random
from typing import Sequence, Union
from sqlalchemy.ext.declarative import declarative_base
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import String, select
from db.models.message import MessageTypes
Base = declarative_base()


# revision identifiers, used by Alembic.
revision: str = '0bcf82f6a8e9'
down_revision: Union[str, None] = '27483580f233'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_column('users', 'name')
    op.drop_column('users', 'surname')
    # ### end Alembic commands ###
    bind = op.get_bind()
    session = Session(bind=bind)
    users = session.execute(select(User)).scalars().all()
    for user in users:
        if not user.username:
            user.username = str(random.randint(1000, 100000))

    session.commit()
    op.alter_column('users', 'username',
                    existing_type=sa.VARCHAR(),
                    nullable=False)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
