"""
Add composite index on (category_id, brand_id) to products table
Revision ID: abcdef123456
Revises: <prev_revision_id>
Create Date: 2024-06-20 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'abcdef123456'
down_revision = '<prev_revision_id>'  # Replace with the previous migration's revision id
table_name = 'products'
index_name = 'ix_products_category_id_brand_id'

def upgrade():
    op.create_index(index_name, table_name, ['category_id', 'brand_id'])

def downgrade():
    op.drop_index(index_name, table_name)
