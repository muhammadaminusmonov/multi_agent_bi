from fastapi import APIRouter
from app.models.schemas import DashboardKPIs
from app.data.mock_data import (
    get_total_revenue,
    get_active_deals,
    get_inventory_value,
    get_employee_count
)

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])

@router.get("/kpis", response_model=DashboardKPIs)
async def get_kpis():
    """Return the four main KPIs for the overview dashboard."""
    return DashboardKPIs(
        total_revenue=get_total_revenue(),
        active_deals=get_active_deals(),
        inventory_value=get_inventory_value(),
        employee_count=get_employee_count()
    )