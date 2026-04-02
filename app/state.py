from __future__ import annotations

from typing import Any, TypedDict


class AgentState(TypedDict, total=False):
    client_id: str
    objective: str
    context: dict[str, str]
    planner_notes: str
    strategy_notes: str
    brand_notes: str
    copy_notes: str
    steps: list[str]
    final_output: str
    metadata: dict[str, Any]
