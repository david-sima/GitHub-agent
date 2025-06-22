#!/usr/bin/env python3
"""
Basic MCP Usage Example

This example demonstrates how to use the Model Context Protocol
implementation to connect to data sources and execute queries.
"""

import asyncio
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mcp import MCPServer
from mcp.data_source import DataSourceConfig, DatabaseDataSource, APIDataSource


async def main():
    """Main example function."""
    print("🚀 Starting MCP Basic Usage Example")
    
    # Create MCP server
    server = MCPServer(host="localhost", port=8000)
    
    # Create data source configurations
    db_config = DataSourceConfig(
        name="example_database",
        type="database",
        connection_string="sqlite:///example.db"
    )
    
    api_config = DataSourceConfig(
        name="example_api",
        type="api",
        endpoint="https://api.example.com",
        timeout=30
    )
    
    # Create data sources
    db_source = DatabaseDataSource(db_config)
    api_source = APIDataSource(api_config)
    
    # Register data sources with the server
    server.register_source("database", db_source)
    server.register_source("api", api_source)
    
    # Connect to data sources
    print("📡 Connecting to data sources...")
    await db_source.connect()
    await api_source.connect()
    
    # Execute some example queries
    print("🔍 Executing example queries...")
    
    # Database query
    db_result = await db_source.query("SELECT * FROM users LIMIT 5")
    print(f"Database query result: {db_result.data}")
    
    # API query
    api_result = await api_source.query("GET /users", {"limit": 5})
    print(f"API query result: {api_result.data}")
    
    # Get server status
    status = server.get_status()
    print(f"Server status: {status}")
    
    # Disconnect from data sources
    await db_source.disconnect()
    await api_source.disconnect()
    
    print("✅ Example completed successfully!")


if __name__ == "__main__":
    asyncio.run(main()) 
