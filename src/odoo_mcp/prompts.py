"""
Prompt implementation for MCP-Odoo
"""

from mcp.server.fastmcp import FastMCP

def register_sales_prompts(mcp: FastMCP) -> None:
    """Registers sales-related prompts"""
    
    @mcp.prompt(
        name="sales_analysis",
        description="Analyzes sales for a specific period and provides key insights"
    )
    def sales_analysis_prompt() -> str:
        return """
        Analyze sales from the last {period} (e.g. 'month', 'quarter', 'year') and provide insights on:
        - Top-selling products (top 5)
        - Key customers (top 5)
        - Sales trends (comparison with previous period if possible)
        - Performance by salesperson (if applicable)
        - Actionable recommendations to improve sales.
        
        Use available tools such as 'search_sales_orders' and 'execute_method' to obtain necessary data from Odoo.
        """

def register_purchase_prompts(mcp: FastMCP) -> None:
    """Registers purchase-related prompts"""
    
    @mcp.prompt(
        name="purchase_analysis",
        description="Analyzes purchase orders and supplier performance"
    )
    def purchase_analysis_prompt() -> str:
        return """
        Analyze purchases made in the last {period} (e.g. 'month', 'quarter', 'year') and provide insights on:
        - Most purchased products (top 5)
        - Key suppliers (top 5 by volume/value)
        - Purchase trends
        - Average delivery times by supplier
        - Recommendations to optimize purchases or negotiate with suppliers.
        
        Use available tools such as 'search_purchase_orders' to obtain necessary data from Odoo.
        """

def register_inventory_prompts(mcp: FastMCP) -> None:
    """Registers inventory-related prompts"""
    
    @mcp.prompt(
        name="inventory_management",
        description="Analyzes inventory status and provides recommendations"
    )
    def inventory_management_prompt() -> str:
        return """
        Analyze the current inventory status and provide information on:
        - Low stock products (below minimum if configured)
        - Excess stock products (above maximum or inactive)
        - Current inventory valuation
        - Inventory turnover for key products
        - Recommendations for adjustments, restocking, or stock liquidation.
        
        Use available tools such as 'check_product_availability' and 'analyze_inventory_turnover' to obtain necessary data from Odoo.
        """

def register_accounting_prompts(mcp: FastMCP) -> None:
    """Registers accounting-related prompts"""
    
    @mcp.prompt(
        name="financial_analysis",
        description="Performs basic financial analysis"
    )
    def financial_analysis_prompt() -> str:
        return """
        Perform financial analysis for the {period} period (e.g. 'last_month', 'last_quarter', 'year_to_date') and provide:
        - Income statement summary (revenue, expenses, profit)
        - Balance sheet summary (assets, liabilities, equity)
        - Key financial ratios (e.g. liquidity, profitability)
        - Comparison with previous period if possible
        - Important observations or alerts.
        
        Use available tools such as 'search_journal_entries' and 'analyze_financial_ratios' to obtain necessary data from Odoo.
        """

def register_all_prompts(mcp: FastMCP) -> None:
    """Registers all available prompts"""
    register_sales_prompts(mcp)
    register_purchase_prompts(mcp)
    register_inventory_prompts(mcp)
    register_accounting_prompts(mcp)
