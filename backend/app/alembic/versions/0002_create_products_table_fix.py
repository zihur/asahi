"""create products table (manual fix)

Revision ID: 0002_create_products_table_fix
Revises: d79e58df0425
Create Date: 2026-05-25 13:40:00.000000
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0002_create_products_table_fix'
down_revision = 'd79e58df0425'
branch_labels = None
depends_on = None


def upgrade():
    # Use IF NOT EXISTS to avoid errors if table already present
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER NOT NULL AUTO_INCREMENT,
            model_no VARCHAR(100) NOT NULL,
            name VARCHAR(255) NOT NULL,
            brand VARCHAR(100),
            spec TEXT,
            remark TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
    )
    # Create unique index if not exists (MySQL 8+ supports IF NOT EXISTS for indexes)
    try:
        op.execute("CREATE UNIQUE INDEX IF NOT EXISTS ix_products_model_no ON products (model_no);")
    except Exception:
        # fallback: ignore if index creation not supported
        pass


def downgrade():
    op.execute("DROP INDEX ix_products_model_no ON products")
    op.execute("DROP TABLE IF EXISTS products")
