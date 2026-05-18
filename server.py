from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",     
        port=8000
    )
