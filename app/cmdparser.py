import shlex

def tokenize(inp: str) -> list[str]:
    """Break the input into tokens"""
    return shlex.split(inp)

def join(tokens: list[str]) -> str:
    return shlex.join(tokens)
