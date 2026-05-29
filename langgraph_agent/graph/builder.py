from langgraph.graph import StateGraph, END

from langgraph_agent.graph.nodes import chatbot, tool_node, router
from langgraph_agent.graph.state import AgentState

# 创建图
graph = StateGraph(AgentState)

# 添加节点
graph.add_node("chatbot", chatbot)
graph.add_node("tool", tool_node)

# 设置入口
graph.set_entry_point("chatbot")

# 条件边
graph.add_conditional_edges(
    "chatbot",
    router,
    {
        "tool": "tool",
        "__end__": END
    }
)

# tool执行后返回chatbot
graph.add_edge("tool", "chatbot")

# 编译
app = graph.compile()