from fastapi import APIRouter, HTTPException
from app.models.schemas import DomainResponse, MetricCard, ChartData
from app.data import mock_data

router = APIRouter(prefix="/api/domain", tags=["Domain Analytics"])

@router.get("/{domain}/metrics", response_model=DomainResponse)
async def get_domain_metrics(domain: str):
    """
    Returns metrics and charts for a specific business domain.
    domain: 'sales', 'inventory', 'finance', 'hr'
    """
    if domain == "sales":
        # --- Metrics ---
        total_revenue = mock_data.get_total_revenue()
        avg_deal_size = total_revenue / max(mock_data.get_active_deals(), 1)
        metrics = [
            MetricCard(label="Total Revenue", value=total_revenue),
            MetricCard(label="Active Deals", value=mock_data.get_active_deals(), prefix="", suffix=" deals"),
            MetricCard(label="Avg Deal Size", value=avg_deal_size),
        ]
        # --- Charts ---
        sales_by_region = mock_data.get_sales_by_region()
        charts = [
            ChartData(
                chart_type="bar",
                title="Revenue by Region",
                data={"labels": list(sales_by_region.keys()), "values": list(sales_by_region.values())}
            ),
            ChartData(
                chart_type="bar",
                title="Top 5 Products",
                data={"labels": list(mock_data.get_top_products(5).keys()), "values": list(mock_data.get_top_products(5).values())}
            )
        ]
        raw_data = mock_data.get_monthly_sales()

    elif domain == "inventory":
        total_value = mock_data.get_inventory_value()
        low_stock = mock_data.get_low_stock_items()
        metrics = [
            MetricCard(label="Total Inventory Value", value=total_value),
            MetricCard(label="SKU Count", value=len(mock_data.df_inventory), prefix="", suffix=" items"),
            MetricCard(label="Low Stock Items", value=len(low_stock), prefix="", suffix=" SKUs")
        ]
        inv_by_cat = mock_data.get_inventory_by_category()
        charts = [
            ChartData(
                chart_type="pie",
                title="Inventory Value by Category",
                data={"labels": list(inv_by_cat.keys()), "values": list(inv_by_cat.values())}
            )
        ]
        raw_data = low_stock

    elif domain == "finance":
        summary = mock_data.get_finance_summary()
        metrics = [
            MetricCard(label="Revenue (MTD)", value=summary['revenue']),
            MetricCard(label="Expenses (MTD)", value=summary['expenses']),
            MetricCard(label="Net Profit (MTD)", value=summary['profit']),
            MetricCard(label="Cash Flow (MTD)", value=summary['cash_flow'])
        ]
        # Chart: monthly trend
        monthly = mock_data.df_finance.to_dict(orient='records')
        charts = [
            ChartData(
                chart_type="line",
                title="Monthly Revenue vs Expenses",
                data={
                    "labels": [r['month'].strftime('%Y-%m') for r in monthly],
                    "revenue": [r['revenue'] for r in monthly],
                    "expenses": [r['expenses'] for r in monthly]
                },
                x_key="labels",
                y_key="revenue"
            )
        ]
        raw_data = monthly

    elif domain == "hr":
        total_employees = mock_data.get_employee_count()
        headcount_by_dept = mock_data.get_headcount_by_dept()
        metrics = [
            MetricCard(label="Total Employees", value=total_employees, prefix="", suffix=" people"),
            MetricCard(label="Departments", value=len(headcount_by_dept), prefix="", suffix=" depts"),
        ]
        charts = [
            ChartData(
                chart_type="bar",
                title="Headcount by Department",
                data={"labels": list(headcount_by_dept.keys()), "values": list(headcount_by_dept.values())}
            )
        ]
        raw_data = mock_data.df_hr.to_dict(orient='records')

    else:
        raise HTTPException(status_code=404, detail=f"Domain '{domain}' not found")

    return DomainResponse(metrics=metrics, charts=charts, raw_data=raw_data)