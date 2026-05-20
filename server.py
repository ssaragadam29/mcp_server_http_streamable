import os
import sys
from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP(
    "server",
    host="0.0.0.0",
    port=8080,
)

@mcp.tool()
def greeting(name: str) -> str:
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

app = mcp.streamable_http_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)