from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.core.config import settings
from app.graph import run_agent_workflow


class AgentInvokeRequest(BaseModel):
    client_id: str = Field(..., description="ID del cliente")
    objective: str = Field(..., description="Obiettivo del task")
    context: dict[str, str] = Field(default_factory=dict, description="Contesto opzionale")


class AgentInvokeResponse(BaseModel):
    client_id: str
    objective: str
    output: str
    steps: list[str]
    model: str


app = FastAPI(
    title=settings.APP_NAME,
    docs_url="/swagger",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get("/agent/health", summary="Health check servizio agent")
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "environment": settings.APP_ENV,
    }


@app.post(
    "/agent/invoke",
    response_model=AgentInvokeResponse,
    summary="Invoca workflow multi-agente",
)
async def invoke_agent(payload: AgentInvokeRequest) -> AgentInvokeResponse:
    state = await run_agent_workflow(
        client_id=payload.client_id,
        objective=payload.objective,
        context=payload.context,
    )
    return AgentInvokeResponse(
        client_id=payload.client_id,
        objective=payload.objective,
        output=state.get("final_output", ""),
        steps=state.get("steps", []),
        model=settings.OLLAMA_MODEL,
    )
