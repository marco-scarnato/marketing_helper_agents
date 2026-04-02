from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.agents.brand_agent import brand_node
from app.agents.copy_agent import copy_node
from app.agents.planner_agent import planner_node
from app.agents.strategy_agent import strategy_node
from app.state import AgentState


def build_graph():
    graph_builder = StateGraph(AgentState)

    graph_builder.add_node("planner", planner_node)
    graph_builder.add_node("strategy", strategy_node)
    graph_builder.add_node("brand", brand_node)
    graph_builder.add_node("copy", copy_node)

    graph_builder.add_edge(START, "planner")
    graph_builder.add_edge("planner", "strategy")
    graph_builder.add_edge("strategy", "brand")
    graph_builder.add_edge("brand", "copy")
    graph_builder.add_edge("copy", END)

    return graph_builder.compile()


async def run_agent_workflow(client_id: str, objective: str, context: dict[str, str]) -> AgentState:
    workflow = build_graph()
    initial_state: AgentState = {
        "client_id": client_id,
        "objective": objective,
        "context": context,
        "steps": [],
    }
    result = await workflow.ainvoke(initial_state)
    return result
