from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.database import get_db
from app.db.models import Sale, InventoryItem, Employee
from app.models.schemas import DashboardKPIs

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])

@router.get("/kpis", response_model=DashboardKPIs)
async def get_kpis(db: Session = Depends(get_db)):
    total_revenue = db.query(func.sum(Sale.revenue)).scalar() or 0.0
    active_deals = 25  # Placeholder – you could add a Deals table later
    inventory_value = db.query(func.sum(InventoryItem.stock_qty * InventoryItem.unit_cost)).scalar() or 0.0
    employee_count = db.query(func.count(Employee.id)).scalar() or 0

    return DashboardKPIs(
        total_revenue=total_revenue,
        active_deals=active_deals,
        inventory_value=inventory_value,
        employee_count=employee_count
    )