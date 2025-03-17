# Weather MCP Server

This is a Model Context Protocol (MCP) server that provides weather information using the National Weather Service (NWS) API.

## Features

- Get weather alerts for a US state
- Get weather forecast for a specific location (using latitude and longitude)

## Requirements

- Python 3.7+
- FastMCP
- httpx

## Installation

1. Clone this repository
2. Set up a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
3. Install the required packages using uv:
   ```
   uv add "mcp[cli]" httpx
   ```

## Configuration

The server uses a configuration file `config.py` with the following settings:

- `NWS_API_BASE`: The base URL for the National Weather Service API
- `USER_AGENT`: The User-Agent string used when making requests to the NWS API
- `LOG_LEVEL`: The logging level (e.g., "INFO", "DEBUG")
- `LOG_FORMAT`: The format string for log messages
- `REQUEST_TIMEOUT`: The timeout for API requests in seconds

You can modify these settings in the `config.py` file to customize the server behavior.

## Usage

### Running the server standalone

To run the server standalone:

1. Activate the virtual environment if not already activated:
   ```
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
2. Run the server:
   ```
   python weather.py
   ```

### Using with Cline

The Weather MCP Server has been added to the Cline configuration. To use it within Cline:

1. Ensure that Cline is properly set up and running.
2. The Weather MCP Server will be available as a tool named "weather".
3. You can use the following tools within Cline:

   a. `get_alerts(state: str)`: Get weather alerts for a US state (use two-letter state code, e.g., "CA" for California)
   b. `get_forecast(latitude: float, longitude: float)`: Get weather forecast for a specific location

Example usage in Cline:

```
# Get alerts for California
result = await mcp.call_tool("weather.get_alerts", state="CA")
print(result)

# Get forecast for San Francisco (approximate coordinates)
result = await mcp.call_tool("weather.get_forecast", latitude=37.7749, longitude=-122.4194)
print(result)
```

Note: The exact syntax for calling MCP tools may vary depending on your Cline setup. Refer to Cline documentation for the most up-to-date usage instructions.

## Error Handling and Logging

The server includes improved error handling for API requests and logging. If an error occurs during a request, the server will log the error and return an appropriate error message. Logs are printed to the console with the configured log level and format.

## Testing

### Unit Tests

To run the unit tests:

```
python -m unittest test_weather.py
```

These tests cover the basic functionality of the `get_alerts` and `get_forecast` tools.

### Manual Testing

To manually test the server, you can use the MCP client to call the provided tools. Here are some example commands:

```python
# Get alerts for California
result = await mcp.call_tool("get_alerts", state="CA")
print(result)

# Get forecast for San Francisco (approximate coordinates)
result = await mcp.call_tool("get_forecast", latitude=37.7749, longitude=-122.4194)
print(result)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
