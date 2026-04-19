import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from app.agents.tools import (
    get_total_revenue, get_sales_by_region, get_top_products, get_monthly_sales_trend,
    get_inventory_value, get_low_stock_items, get_inventory_by_category,
    get_current_finance_summary, get_monthly_finance_trend,
    get_employee_count, get_headcount_by_department, get_department_details,
    get_active_deals
)

def create_orchestrator_agent():
    """Create a LangChain agent with all domain tools."""
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    tools = [
        get_total_revenue,
        get_sales_by_region,
        get_top_products,
        get_monthly_sales_trend,
        get_inventory_value,
        get_low_stock_items,
        get_inventory_by_category,
        get_current_finance_summary,
        get_monthly_finance_trend,
        get_employee_count,
        get_headcount_by_department,
        get_department_details,
        get_active_deals
    ]

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful business intelligence assistant with access to company data.
        You can answer questions about sales, inventory, finance, and HR.
        Use the available tools to fetch accurate data, then provide a concise, insightful answer.
        If you don't have the necessary data, say so politely."""),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])

    agent = create_openai_tools_agent(llm, tools, prompt)
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        return_intermediate_steps=True
    )
    return executor