from __future__ import annotations

from app.state import AgentState


async def strategy_node(state: AgentState) -> AgentState:
    steps = list(state.get("steps", []))
    steps.append("strategy")
    planner_notes = state.get("planner_notes", "")
    state["strategy_notes"] = f"Strategia bozza derivata da planner: {planner_notes}"
    state["steps"] = steps
    return state
