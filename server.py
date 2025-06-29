from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Demo",
    host="0.0.0.0",
    port=8050
)

if __name__ == "__main__":
    transport = "stdio"
    if transport == "stdio":
        print("Running MCP server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running MCP server with SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Invalid transport: {transport}")