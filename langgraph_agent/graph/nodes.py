from langchain_core.messages import SystemMessage

from langgraph_agent.llm.model import llm
from langgraph_agent.prompts.system_prompt import SYSTEM_PROMPT
from langgraph_agent.tools.calculator import calculator

# 初始化工具列表
tools = [calculator]

# 绑定工具到llm
llm_with_tools = llm.bind_tools(tools)

# chatbot 节点
def chatbot(state):
    # 在消息列表前添加系统消息
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]

    response = llm_with_tools.invoke(messages)
    return {
        "messages": state["messages"] + [response]
    }

# =========================
# tool 节点
# =========================

def tool_node(state):

    last_message = state["messages"][-1]

    tool_calls = last_message.tool_calls

    outputs = []

    for tool_call in tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        if tool_name == "calculator":

            result = calculator.invoke(tool_args)

            outputs.append(
                {
                    "role": "tool",
                    "content": result,
                    "tool_call_id": tool_call["id"]
                }
            )

    return {
        "messages": state["messages"] + outputs
    }

# =========================
# 路由函数
# =========================

def router(state):

    last_message = state["messages"][-1]

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tool"

    return "__end__"