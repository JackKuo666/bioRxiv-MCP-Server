# bioRxiv MCP Server

🔍 Enable AI assistants to search and access bioRxiv papers through a simple MCP interface.

The bioRxiv MCP Server provides a bridge between AI assistants and bioRxiv's preprint repository through the Model Context Protocol (MCP). It allows AI models to search for biology preprints and access their metadata in a programmatic way.

🤝 Contribute • 📝 Report Bug

## ✨ Core Features
- 🔎 Paper Search: Query bioRxiv papers with keywords or advanced search ✅
- 🚀 Efficient Retrieval: Fast access to paper metadata ✅
- 📊 Metadata Access: Retrieve detailed metadata for specific papers ✅
- 📊 Research Support: Facilitate biological sciences research and analysis ✅
- 📄 Paper Access: Download and read paper content 📝
- 📋 Paper Listing: View all downloaded papers 📝
- 🗃️ Local Storage: Papers are saved locally for faster access 📝
- 📝 Research Prompts: A set of specialized prompts for paper analysis 📝

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- FastMCP library

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/JackKuo666/bioRxiv-MCP-Server.git
   cd bioRxiv-MCP-Server
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Installing via Smithery

To install bioRxiv Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/biorxiv-mcp-server):

#### claude

```bash
npx -y @smithery/cli@latest install @JackKuo666/biorxiv-mcp-server --client claude --config "{}"
```

#### Cursor

Paste the following into Settings → Cursor Settings → MCP → Add new server: 
- Mac/Linux  
```s
npx -y @smithery/cli@latest run @JackKuo666/biorxiv-mcp-server --client cursor --config "{}" 
```
#### Windsurf
```sh
npx -y @smithery/cli@latest install @JackKuo666/biorxiv-mcp-server --client windsurf --config "{}"
```
#### CLine
```sh
npx -y @smithery/cli@latest install @JackKuo666/biorxiv-mcp-server --client cline --config "{}"
```

#### Usage with Claude Desktop

Add this configuration to your `claude_desktop_config.json`:

(Mac OS)

```json
{
  "mcpServers": {
    "biorxiv": {
      "command": "python",
      "args": ["-m", "biorxiv-mcp-server"]
      }
  }
}
```

(Windows version):

```json
{
  "mcpServers": {
    "biorxiv": {
      "command": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
      "args": [
        "-m",
        "biorxiv-mcp-server"
      ]
    }
  }
}
```
Using with Cline
```json
{
  "mcpServers": {
    "biorxiv": {
      "command": "bash",
      "args": [
        "-c",
        "source /home/YOUR/PATH/mcp-server-bioRxiv/.venv/bin/activate && python /home/YOUR/PATH/mcp-server-bioRxiv/biorxiv_server.py"
      ],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```


## 📊 Usage

Start the MCP server:

```bash
python biorxiv_server.py
```

## 🛠 MCP Tools

The bioRxiv MCP Server provides the following tools:

1. `search_biorxiv_key_words`: Search for articles on bioRxiv using keywords.
2. `search_biorxiv_advanced`: Perform an advanced search for articles on bioRxiv with multiple parameters.
3. `get_biorxiv_metadata`: Fetch metadata for a bioRxiv article using its DOI.

### Searching Papers

You can ask the AI assistant to search for papers using queries like:
```
Can you search bioRxiv for recent papers about genomics?
```

### Getting Paper Details

Once you have a DOI, you can ask for more details:
```
Can you show me the metadata for the paper with DOI 10.1101/123456?
```

## 📁 Project Structure

- `biorxiv_server.py`: The main MCP server implementation using FastMCP
- `biorxiv_web_search.py`: Contains the web scraping logic for searching bioRxiv

## 🔧 Dependencies

- Python 3.10+
- FastMCP
- asyncio
- logging

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This tool is for research purposes only. Please respect bioRxiv's terms of service and use this tool responsibly.
