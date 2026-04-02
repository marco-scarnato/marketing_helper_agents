from __future__ import annotations

from app.state import AgentState


async def copy_node(state: AgentState) -> AgentState:
    steps = list(state.get("steps", []))
    steps.append("copy")
    objective = state.get("objective", "")
    brand_notes = state.get("brand_notes", "")
    state["copy_notes"] = f"Bozza copy per obiettivo '{objective}'"
    state["final_output"] = f"[MVP] Output generato. Brand notes: {brand_notes}"
    state["steps"] = steps
    return state
