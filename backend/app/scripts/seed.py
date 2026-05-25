import argparse
from typing import List

from app.core.database import SessionLocal
from app.models.product import Product


def seed_products(session, products: List[dict], force: bool = False):
    if force:
        session.query(Product).delete()
    # only insert if empty or force
    if force or not session.query(Product).first():
        objs = [Product(**p) for p in products]
        session.add_all(objs)
        session.commit()


DEFAULT_PRODUCTS = [
    {"model_no": "ABC-100", "name": "測試產品 A", "brand": "BrandX", "spec": "100mm"},
    {"model_no": "ABC-200", "name": "測試產品 B", "brand": "BrandX", "spec": "200mm"},
    {"model_no": "XYZ-001", "name": "相容型號", "brand": "BrandY", "spec": "Standard"},
]


def main():
    parser = argparse.ArgumentParser(description="Seed products into DB")
    parser.add_argument("--force", action="store_true", help="Delete existing products before seeding")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        seed_products(db, DEFAULT_PRODUCTS, force=args.force)
        print("Seed complete")
    finally:
        db.close()


if __name__ == "__main__":
    main()
