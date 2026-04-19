from pydantic import BaseModel
from typing import List, Dict, Optional, Any
from datetime import date

# -------------------------
# Dashboard KPIs
# -------------------------
class DashboardKPIs(BaseModel):
    total_revenue: float
    active_deals: int
    inventory_value: float
    employee_count: int

# -------------------------
# Domain Metrics (generic)
# -------------------------
class MetricCard(BaseModel):
    label: str
    value: float
    delta: Optional[float] = None  # Change vs previous period
    prefix: Optional[str] = "$"
    suffix: Optional[str] = ""

class ChartData(BaseModel):
    chart_type: str  # "line", "bar", "pie"
    title: str
    data: Dict[str, List[Any]]  # { "labels": [...], "values": [...] }
    x_key: str = "labels"
    y_key: str = "values"

class DomainResponse(BaseModel):
    metrics: List[MetricCard]
    charts: List[ChartData]
    raw_data: Optional[List[Dict]] = None  # For table display if needed

# -------------------------
# Chat
# -------------------------
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    thoughts: Optional[List[str]] = []  # ReAct intermediate steps
    data_sources: Optional[List[str]] = []