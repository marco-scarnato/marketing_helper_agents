from __future__ import annotations

from app.state import AgentState


async def brand_node(state: AgentState) -> AgentState:
    steps = list(state.get("steps", []))
    steps.append("brand")
    strategy_notes = state.get("strategy_notes", "")
    state["brand_notes"] = f"Allineamento brand calcolato da strategy: {strategy_notes}"
    state["steps"] = steps
    return state
