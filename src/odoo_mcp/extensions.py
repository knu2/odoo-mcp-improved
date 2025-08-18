"""
Integration of all modules in the main MCP server
"""

from mcp.server.fastmcp import FastMCP

from .prompts import register_all_prompts
from .resources import register_all_resources
from .tools_sales import register_sales_tools
from .tools_purchase import register_purchase_tools
from .tools_inventory import register_inventory_tools
from .tools_accounting import register_accounting_tools

def register_all_extensions(mcp: FastMCP) -> None:
    """
    Registers all extensions (prompts, resources, and tools)
    in the MCP server
    """
    # Register prompts
    register_all_prompts(mcp)
    
    # Register resources
    register_all_resources(mcp)
    
    # Register tools
    register_sales_tools(mcp)
    register_purchase_tools(mcp)
    register_inventory_tools(mcp)
    register_accounting_tools(mcp)
