# 在该文件中可以自定义State，目前项目中使用的是AgentState
"""
AgentState有3个字段：
1.messages:Required[Annotated[list[AnyMessage], add_messages]]
    其中list[AnyMessage]可以是HumanMessage、AIMessage、SystemMessage等类型
    add_messages节点返回新消息时自动追加到列表末尾，而不是覆盖整个列表
    节点只需要返回增量消息，不用自己拼接

    def chatbot(state):
      response = llm.invoke(state["messages"])
      return {"messages": [response]}  # add_messages 自动追加


2.jump_to:NotRequired[Annotated[JumpTo | None, EphemeralValue, PrivateStateAttr]]
  - NotRequired：可选字段
  - EphemeralValue：临时值，用完即清（不会累积）
  - PrivateStateAttr：内部用的，节点间传递但不会暴露给外部
- 允许在 Graph 中动态跳转到指定节点，比如循环重试或提前结束


3.structured_response:NotRequired[Annotated[ResponseT, OmitFromInput]]
  - Generic[ResponseT]：泛型参数，可以指定返回类型
  - OmitFromInput：调用时不需要传这个字段，它只在执行过程中由 agent 写入
- 用于让 agent 返回 Pydantic model 等结构化数据，而不只是纯文本


"""