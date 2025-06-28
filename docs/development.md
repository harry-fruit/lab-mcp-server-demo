# Development Guide

This guide explains how to set up and run the MCP server demo project.

## Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-server-demo
```

2. Install dependencies using uv:
```bash
uv sync
```

Or if you prefer pip:
```bash
pip install -r requirements.txt
```

## Running the Server

### Development Mode (Recommended)

Start the server in development mode with the MCP Inspector for testing:

```bash
uv run mcp dev server.py
```

This will:
- Start your MCP server
- Open the MCP Inspector in your browser
- Allow you to test tools and resources interactively

### Production Mode

To run the server for production use:

```bash
uv run python server.py
```

## Project Structure

```
mcp-server-demo/
├── server.py          # Main server file
├── tools.py           # Tool functions
├── resources.py       # Resource functions
├── pyproject.toml     # Project configuration
└── docs/
    └── development.md # This file
```

## Available Tools

- `add(a: int, b: int)` - Add two numbers
- `subtract(a: int, b: int)` - Subtract two numbers  
- `say_hello(name: str)` - Say hello to a person

## Available Resources

- `greeting://{name}` - Get a personalized greeting

## Testing

Use the MCP Inspector (available in development mode) to test your tools and resources interactively.

## Next Steps

- Add more tools and resources to `tools.py` and `resources.py`
- Implement error handling and validation
- Add configuration management
- Set up logging and monitoring 