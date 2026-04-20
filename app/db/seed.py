from datetime import datetime, timedelta
import random
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.database import SessionLocal, engine
from app.db.models import Base, Region, Product, Sale, InventoryItem, FinanceRecord, Department, Employee

def seed_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Regions
    regions = ["North", "South", "East", "West"]
    region_objs = [Region(name=r) for r in regions]
    db.add_all(region_objs)
    db.commit()

    # Products
    products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
    categories = ["Electronics", "Furniture", "Apparel", "Electronics", "Furniture"]
    product_objs = [Product(name=p, category=c) for p, c in zip(products, categories)]
    db.add_all(product_objs)
    db.commit()

    # Sales (12 months)
    start_date = datetime.today().replace(day=1) - timedelta(days=365)
    for i in range(12):
        month = start_date + timedelta(days=30 * i)
        for region in region_objs:
            for product in product_objs:
                sale = Sale(
                    date=month.date(),
                    region_id=region.id,
                    product_id=product.id,
                    revenue=random.randint(5000, 50000),
                    units_sold=random.randint(10, 200)
                )
                db.add(sale)
    db.commit()

    # Inventory
    inventory_items = [
        InventoryItem(sku="A100", product_name="Product A", category="Electronics", stock_qty=450, reorder_level=100, unit_cost=120.0),
        InventoryItem(sku="B200", product_name="Product B", category="Electronics", stock_qty=80, reorder_level=150, unit_cost=85.0),
        InventoryItem(sku="C300", product_name="Product C", category="Furniture", stock_qty=200, reorder_level=75, unit_cost=350.0),
        InventoryItem(sku="D400", product_name="Product D", category="Furniture", stock_qty=30, reorder_level=60, unit_cost=500.0),
        InventoryItem(sku="E500", product_name="Product E", category="Apparel", stock_qty=600, reorder_level=200, unit_cost=25.0),
    ]
    db.add_all(inventory_items)
    db.commit()

    # Finance (monthly aggregates from sales)
    monthly_sales = db.query(Sale.date, func.sum(Sale.revenue).label("revenue")).group_by(Sale.date).all()
    for date, revenue in monthly_sales:
        expenses = revenue * random.uniform(0.5, 0.8)
        profit = revenue - expenses
        finance = FinanceRecord(
            month=date,
            revenue=revenue,
            expenses=expenses,
            profit=profit,
            cash_flow=profit * random.uniform(0.8, 1.2)
        )
        db.add(finance)
    db.commit()

    # Departments and Employees
    dept_names = ["Engineering", "Sales", "Marketing", "HR", "Finance"]
    dept_objs = [Department(name=d) for d in dept_names]
    db.add_all(dept_objs)
    db.commit()

    for dept in dept_objs:
        for _ in range(random.randint(5, 50)):
            emp = Employee(
                name=f"Employee {random.randint(1000, 9999)}",
                department_id=dept.id,
                hire_date=datetime.today() - timedelta(days=random.randint(30, 2000)),
                salary=random.randint(50000, 150000)
            )
            db.add(emp)
    db.commit()

    db.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()