from langchain_core.tools import tool

@tool
def calculator(query: str) -> str:
    """执行数学计算"""

    try:
        result = eval(query)
        return f"计算结果: {result}"
    except Exception as e:
        return f"错误: {e}"