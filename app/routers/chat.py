from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.agents.orchestrator import create_orchestrator_agent

router = APIRouter(prefix="/api", tags=["Chat"])

# Global agent instance (created once)
_agent_executor = None


def get_agent():
    global _agent_executor
    if _agent_executor is None:
        _agent_executor = create_orchestrator_agent()
    return _agent_executor


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Process a natural language query and return agent response."""
    try:
        executor = get_agent()
        result = executor.invoke({"input": request.message})

        # Extract intermediate steps (thoughts)
        thoughts = []
        data_sources = []
        if "intermediate_steps" in result:
            for step in result["intermediate_steps"]:
                action, observation = step
                thoughts.append(f"🔧 Used tool: {action.tool}")
                thoughts.append(f"📊 Result: {observation}")
                data_sources.append(action.tool)

        return ChatResponse(
            response=result["output"],
            thoughts=thoughts,
            data_sources=data_sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))