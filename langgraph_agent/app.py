from langchain_core.messages import HumanMessage
from graph.builder import app

while True:

    user_input = input("用户: ")

    if user_input == "exit":
        break

    print("\nAI: ", end="", flush=True)

    for chunk, metadata in app.stream(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        stream_mode="messages"
    ):

        # 只输出 chatbot 节点
        if metadata["langgraph_node"] != "chatbot":
            continue

        # 输出 token
        if chunk.content:
            print(chunk.content, end="", flush=True)

    print("\n")

