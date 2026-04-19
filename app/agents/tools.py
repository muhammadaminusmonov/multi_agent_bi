from langchain.tools import tool
from typing import List, Dict
import app.data.mock_data as data

# ------------------------------
# Sales Tools
# ------------------------------
@tool
def get_total_revenue() -> float:
    """Return the total revenue across all time."""
    return data.get_total_revenue()

@tool
def get_sales_by_region() -> Dict[str, float]:
    """Return revenue breakdown by region."""
    return data.get_sales_by_region()

@tool
def get_top_products(n: int = 5) -> Dict[str, float]:
    """Return top N products by revenue."""
    return data.get_top_products(n)

@tool
def get_monthly_sales_trend() -> List[Dict]:
    """Return monthly sales trend as list of {date, revenue}."""
    return data.get_monthly_sales()

# ------------------------------
# Inventory Tools
# ------------------------------
@tool
def get_inventory_value() -> float:
    """Return total inventory value."""
    return data.get_inventory_value()

@tool
def get_low_stock_items() -> List[Dict]:
    """Return list of items below reorder level."""
    return data.get_low_stock_items()

@tool
def get_inventory_by_category() -> Dict[str, float]:
    """Return inventory value grouped by category."""
    return data.get_inventory_by_category()

# ------------------------------
# Finance Tools
# ------------------------------
@tool
def get_current_finance_summary() -> Dict:
    """Return latest month's finance summary (revenue, expenses, profit, cash flow)."""
    return data.get_finance_summary()

@tool
def get_monthly_finance_trend() -> List[Dict]:
    """Return monthly finance trend for revenue, expenses, profit."""
    records = data.df_finance.to_dict(orient='records')
    for r in records:
        r['month'] = r['month'].strftime('%Y-%m')
    return records

# ------------------------------
# HR Tools
# ------------------------------
@tool
def get_employee_count() -> int:
    """Return total number of employees."""
    return data.get_employee_count()

@tool
def get_headcount_by_department() -> Dict[str, int]:
    """Return headcount per department."""
    return data.get_headcount_by_dept()

@tool
def get_department_details() -> List[Dict]:
    """Return detailed HR metrics per department."""
    return data.df_hr.to_dict(orient='records')

# ------------------------------
# Global Tools
# ------------------------------
@tool
def get_active_deals() -> int:
    """Return number of active sales deals."""
    return data.get_active_deals()