from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# ------------------------------
# Sales Models
# ------------------------------
class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    sales = relationship("Sale", back_populates="region")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String)
    sales = relationship("Sale", back_populates="product")

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    revenue = Column(Float, nullable=False)
    units_sold = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    region = relationship("Region", back_populates="sales")
    product = relationship("Product", back_populates="sales")

# ------------------------------
# Inventory Models
# ------------------------------
class InventoryItem(Base):
    __tablename__ = "inventory_items"
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, nullable=False)
    product_name = Column(String, nullable=False)
    category = Column(String)
    stock_qty = Column(Integer, nullable=False)
    reorder_level = Column(Integer, nullable=False)
    unit_cost = Column(Float, nullable=False)

    @property
    def inventory_value(self):
        return self.stock_qty * self.unit_cost

# ------------------------------
# Finance Models
# ------------------------------
class FinanceRecord(Base):
    __tablename__ = "finance_records"
    id = Column(Integer, primary_key=True, index=True)
    month = Column(Date, unique=True, nullable=False)
    revenue = Column(Float, nullable=False)
    expenses = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)
    cash_flow = Column(Float, nullable=False)

# ------------------------------
# HR Models
# ------------------------------
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    hire_date = Column(Date)
    salary = Column(Float)

    department = relationship("Department", back_populates="employees")