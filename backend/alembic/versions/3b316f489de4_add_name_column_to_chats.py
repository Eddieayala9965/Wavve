"""Add name column to chats

Revision ID: 3b316f489de4
Revises: 195de10da8f7
Create Date: 2024-11-29 14:49:56.556875

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3b316f489de4'
down_revision: Union[str, None] = '195de10da8f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the "name" column to the "chat" table if it doesn't already exist
    conn = op.get_bind()
    if not column_exists(conn, "chat", "name"):
        op.add_column(
            'chat',
            sa.Column('name', sa.String(), nullable=False, server_default='Unnamed Chat')
        )
    else:
        print("Column 'name' already exists in 'chat'. Skipping addition.")


def downgrade() -> None:
    # Remove the "name" column from the "chat" table
    op.drop_column('chat', 'name')


def column_exists(conn, table_name, column_name):
    """Check if a column exists in a table."""
    result = conn.execute(
        sa.text(
            f"""
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.columns
                WHERE table_name = :table_name AND column_name = :column_name
            )
            """
        ),
        {"table_name": table_name, "column_name": column_name},
    ).scalar()
    return result
