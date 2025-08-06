import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)
    price = Column(Numeric, nullable=False)

    __table_args__ = (
        Index('ix_products_category_id_brand_id', 'category_id', 'brand_id'),
    )
