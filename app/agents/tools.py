# app/agents/tools.py

from langchain.tools import tool
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from app.db.database import SessionLocal
from app.db.models import (
    Region, Product, Sale, InventoryItem, 
    FinanceRecord, Department, Employee
)

# Helper to safely get a DB session
def get_db_session() -> Session:
    return SessionLocal()

# ------------------------------
# Sales Tools
# ------------------------------
@tool
def get_total_revenue() -> float:
    """Return the total revenue across all time."""
    db = get_db_session()
    try:
        result = db.query(func.sum(Sale.revenue)).scalar()
        return float(result) if result else 0.0
    finally:
        db.close()

@tool
def get_sales_by_region() -> Dict[str, float]:
    """Return revenue breakdown by region."""
    db = get_db_session()
    try:
        sales_by_region = (
            db.query(Region.name, func.sum(Sale.revenue))
            .join(Sale, Region.id == Sale.region_id)
            .group_by(Region.name)
            .all()
        )
        return {region: float(revenue) for region, revenue in sales_by_region}
    finally:
        db.close()

@tool
def get_top_products(n: int = 5) -> Dict[str, float]:
    """Return top N products by revenue."""
    db = get_db_session()
    try:
        top_products = (
            db.query(Product.name, func.sum(Sale.revenue))
            .join(Sale, Product.id == Sale.product_id)
            .group_by(Product.name)
            .order_by(func.sum(Sale.revenue).desc())
            .limit(n)
            .all()
        )
        return {product: float(revenue) for product, revenue in top_products}
    finally:
        db.close()

@tool
def get_monthly_sales_trend() -> List[Dict[str, Any]]:
    """Return monthly sales trend as list of {date, revenue}."""
    db = get_db_session()
    try:
        monthly = (
            db.query(Sale.date, func.sum(Sale.revenue))
            .group_by(Sale.date)
            .order_by(Sale.date)
            .all()
        )
        return [{"date": str(date), "revenue": float(revenue)} for date, revenue in monthly]
    finally:
        db.close()

# ------------------------------
# Inventory Tools
# ------------------------------
@tool
def get_inventory_value() -> float:
    """Return total inventory value."""
    db = get_db_session()
    try:
        result = db.query(func.sum(InventoryItem.stock_qty * InventoryItem.unit_cost)).scalar()
        return float(result) if result else 0.0
    finally:
        db.close()

@tool
def get_low_stock_items() -> List[Dict[str, Any]]:
    """Return list of items below reorder level."""
    db = get_db_session()
    try:
        low_stock = (
            db.query(InventoryItem)
            .filter(InventoryItem.stock_qty < InventoryItem.reorder_level)
            .all()
        )
        return [
            {
                "sku": item.sku,
                "product_name": item.product_name,
                "stock_qty": item.stock_qty,
                "reorder_level": item.reorder_level,
                "inventory_value": item.stock_qty * item.unit_cost
            }
            for item in low_stock
        ]
    finally:
        db.close()

@tool
def get_inventory_by_category() -> Dict[str, float]:
    """Return inventory value grouped by category."""
    db = get_db_session()
    try:
        inv_by_cat = (
            db.query(
                InventoryItem.category,
                func.sum(InventoryItem.stock_qty * InventoryItem.unit_cost)
            )
            .group_by(InventoryItem.category)
            .all()
        )
        return {category: float(value) for category, value in inv_by_cat}
    finally:
        db.close()

# ------------------------------
# Finance Tools
# ------------------------------
@tool
def get_current_finance_summary() -> Dict[str, float]:
    """Return latest month's finance summary (revenue, expenses, profit, cash flow)."""
    db = get_db_session()
    try:
        latest = db.query(FinanceRecord).order_by(FinanceRecord.month.desc()).first()
        if latest:
            return {
                "month": str(latest.month),
                "revenue": float(latest.revenue),
                "expenses": float(latest.expenses),
                "profit": float(latest.profit),
                "cash_flow": float(latest.cash_flow)
            }
        return {}
    finally:
        db.close()

@tool
def get_monthly_finance_trend() -> List[Dict[str, Any]]:
    """Return monthly finance trend for revenue, expenses, profit."""
    db = get_db_session()
    try:
        records = db.query(FinanceRecord).order_by(FinanceRecord.month).all()
        return [
            {
                "month": str(r.month),
                "revenue": float(r.revenue),
                "expenses": float(r.expenses),
                "profit": float(r.profit),
                "cash_flow": float(r.cash_flow)
            }
            for r in records
        ]
    finally:
        db.close()

# ------------------------------
# HR Tools
# ------------------------------
@tool
def get_employee_count() -> int:
    """Return total number of employees."""
    db = get_db_session()
    try:
        return db.query(func.count(Employee.id)).scalar() or 0
    finally:
        db.close()

@tool
def get_headcount_by_department() -> Dict[str, int]:
    """Return headcount per department."""
    db = get_db_session()
    try:
        headcounts = (
            db.query(Department.name, func.count(Employee.id))
            .join(Employee, Department.id == Employee.department_id)
            .group_by(Department.name)
            .all()
        )
        return {dept: count for dept, count in headcounts}
    finally:
        db.close()

@tool
def get_department_details() -> List[Dict[str, Any]]:
    """Return detailed HR metrics per department."""
    db = get_db_session()
    try:
        depts = db.query(Department).all()
        result = []
        for dept in depts:
            emp_count = len(dept.employees)
            avg_salary = (
                db.query(func.avg(Employee.salary))
                .filter(Employee.department_id == dept.id)
                .scalar()
            ) if emp_count > 0 else 0.0
            result.append({
                "department": dept.name,
                "headcount": emp_count,
                "avg_salary": float(avg_salary) if avg_salary else 0.0
            })
        return result
    finally:
        db.close()

# ------------------------------
# Global Tools
# ------------------------------
@tool
def get_active_deals() -> int:
    """
    Return number of active sales deals.
    Note: Since we don't have a deals table yet, this returns a placeholder.
    For production, you should add a Deals model and query it.
    """
    # Placeholder – you can replace with real logic later
    return 25