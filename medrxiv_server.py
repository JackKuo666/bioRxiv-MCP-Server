from typing import Any, List, Dict
import asyncio
import logging
from mcp.server.fastmcp import FastMCP
from medrxiv_web_search import search_medrxiv

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize FastMCP server
mcp = FastMCP("medrxiv")

@mcp.tool()
async def search_medrxiv_articles(query: str, num_results: int = 10) -> List[Dict[str, Any]]:
    logging.info(f"Searching for articles with query: {query}, num_results: {num_results}")
    """
    Search for articles on medRxiv.

    Args:
        query: Search query string
        num_results: Number of results to return (default: 10)

    Returns:
        List of dictionaries containing article information
    """
    try:
        results = await asyncio.to_thread(search_medrxiv, query, num_results)
        return results
    except Exception as e:
        return [{"error": f"An error occurred while searching: {str(e)}"}]

if __name__ == "__main__":
    logging.info("Starting MedRxiv MCP server")
    # Initialize and run the server
    mcp.run(transport='stdio')
