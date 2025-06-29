# server.py
from mcp.server.fastmcp import FastMCP
from tools import add, subtract, multiply, divide, say_hello
from resources import get_greeting

# Create an MCP server
mcp = FastMCP("Demo")

# Register tools
mcp.tool()(add)
mcp.tool()(subtract)
mcp.tool()(multiply)
mcp.tool()(divide)
mcp.tool()(say_hello)

# Register resources
mcp.resource("greeting://{name}")(get_greeting)