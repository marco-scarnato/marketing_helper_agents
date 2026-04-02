from __future__ import annotations

from app.state import AgentState


async def planner_node(state: AgentState) -> AgentState:
    steps = list(state.get("steps", []))
    steps.append("planner")
    objective = state.get("objective", "")
    state["planner_notes"] = f"Piano iniziale creato per: {objective}"
    state["steps"] = steps
    return state
