import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ------------------------------
# 1. Sales Data
# ------------------------------
np.random.seed(42)
dates = pd.date_range(end=datetime.today(), periods=12, freq='M')
regions = ['North', 'South', 'East', 'West']
products = ['Product A', 'Product B', 'Product C', 'Product D']

sales_records = []
for date in dates:
    for region in regions:
        for product in products:
            revenue = np.random.randint(5000, 50000)
            units = np.random.randint(10, 200)
            sales_records.append({
                'date': date,
                'region': region,
                'product': product,
                'revenue': revenue,
                'units_sold': units
            })

df_sales = pd.DataFrame(sales_records)

# ------------------------------
# 2. Inventory Data
# ------------------------------
inventory_items = [
    {'sku': 'A100', 'product_name': 'Product A', 'category': 'Electronics', 'stock_qty': 450, 'reorder_level': 100, 'unit_cost': 120.0},
    {'sku': 'B200', 'product_name': 'Product B', 'category': 'Electronics', 'stock_qty': 80, 'reorder_level': 150, 'unit_cost': 85.0},
    {'sku': 'C300', 'product_name': 'Product C', 'category': 'Furniture', 'stock_qty': 200, 'reorder_level': 75, 'unit_cost': 350.0},
    {'sku': 'D400', 'product_name': 'Product D', 'category': 'Furniture', 'stock_qty': 30, 'reorder_level': 60, 'unit_cost': 500.0},
    {'sku': 'E500', 'product_name': 'Product E', 'category': 'Apparel', 'stock_qty': 600, 'reorder_level': 200, 'unit_cost': 25.0},
]
df_inventory = pd.DataFrame(inventory_items)
df_inventory['inventory_value'] = df_inventory['stock_qty'] * df_inventory['unit_cost']

# ------------------------------
# 3. Finance Data (monthly)
# ------------------------------
finance_data = []
for i, date in enumerate(dates):
    revenue = df_sales[df_sales['date'] == date]['revenue'].sum()
    expenses = revenue * np.random.uniform(0.5, 0.8)
    profit = revenue - expenses
    finance_data.append({
        'month': date,
        'revenue': revenue,
        'expenses': expenses,
        'profit': profit,
        'cash_flow': profit * np.random.uniform(0.8, 1.2)
    })
df_finance = pd.DataFrame(finance_data)

# ------------------------------
# 4. HR Data
# ------------------------------
departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance']
hr_data = []
for dept in departments:
    headcount = np.random.randint(5, 50)
    hr_data.append({
        'department': dept,
        'headcount': headcount,
        'avg_tenure_years': np.random.uniform(1.5, 8.0),
        'open_positions': np.random.randint(0, 5)
    })
df_hr = pd.DataFrame(hr_data)

# ------------------------------
# Helper functions for agents
# ------------------------------
def get_total_revenue():
    return df_sales['revenue'].sum()

def get_active_deals():
    # Simulated active deals count
    return np.random.randint(15, 40)

def get_inventory_value():
    return df_inventory['inventory_value'].sum()

def get_employee_count():
    return df_hr['headcount'].sum()

def get_sales_by_region():
    return df_sales.groupby('region')['revenue'].sum().to_dict()

def get_top_products(n=5):
    return df_sales.groupby('product')['revenue'].sum().nlargest(n).to_dict()

def get_monthly_sales():
    monthly = df_sales.groupby('date')['revenue'].sum().reset_index()
    monthly['date'] = monthly['date'].dt.strftime('%Y-%m')
    return monthly.to_dict(orient='records')

def get_low_stock_items():
    low = df_inventory[df_inventory['stock_qty'] < df_inventory['reorder_level']]
    return low[['sku', 'product_name', 'stock_qty', 'reorder_level']].to_dict(orient='records')

def get_inventory_by_category():
    return df_inventory.groupby('category')['inventory_value'].sum().to_dict()

def get_finance_summary():
    latest = df_finance.iloc[-1].to_dict()
    return latest

def get_headcount_by_dept():
    return df_hr.set_index('department')['headcount'].to_dict()