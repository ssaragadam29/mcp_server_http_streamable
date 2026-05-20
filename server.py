import os
import sys

from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", sys.argv[1] if len(sys.argv) > 1 else 8080))
    uvicorn.run(
        mcp.streamable_http_app(),
        host="0.0.0.0",
        port=port,
    )