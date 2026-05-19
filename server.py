from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Expose the FastMCP app via uvicorn
    uvicorn.run(mcp.app, host="0.0.0.0", port=8000)
