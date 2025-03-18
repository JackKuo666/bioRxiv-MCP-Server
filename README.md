# medRxiv MCP Server

🔍 Enable AI assistants to search and access medRxiv papers through a simple MCP interface.

The medRxiv MCP Server provides a bridge between AI assistants and medRxiv's preprint repository through the Model Context Protocol (MCP). It allows AI models to search for health sciences preprints and access their content in a programmatic way.

🤝 Contribute • 📝 Report Bug

## ✨ Core Features
- 🔎 Paper Search: Query medRxiv papers with custom search strings ✅
- 🚀 Efficient Retrieval: Fast access to paper metadata ✅
- 📄 Paper Access: Download and read paper content 📝
- 📋 Paper Listing: View all downloaded papers 📝
- 🗃️ Local Storage: Papers are saved locally for faster access 📝
- 📝 Research Prompts: A set of specialized prompts for paper analysis 📝
- 📊 Research Support: Facilitate health sciences research and analysis 📝

## 🚀 Quick Start

### Installing via Smithery

To install medRxiv Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/arxiv-mcp-server):

```bash
npx -y @smithery/cli install medrxiv-mcp-server --client claude
```

### Installing Manually
Install using uv:

```bash
uv tool install medRxiv-mcp-server
```

For development:

```bash
# Clone and set up development environment
git clone https://github.com/JackKuo666/medRxiv-MCP-Server.git
cd medRxiv-MCP-Server

# Create and activate virtual environment
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## 📊 Usage

Start the MCP server:

```bash
python medrxiv_server.py
```

## 🛠 MCP Tools

## Usage with Claude Desktop

Add this configuration to your `claude_desktop_config.json`:

(Mac OS)

```json
{
  "mcpServers": {
    "biorxiv": {
      "command": "python",
      "args": ["-m", "medrxiv-mcp-server"]
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
        "medrxiv-mcp-server"
      ]
    }
  }
}
```
Using with Cline
```json
{
  "mcpServers": {
    "medrxiv": {
      "command": "bash",
      "args": [
        "-c",
        "source /home/YOUR/PATH/mcp-server-bioRxiv/.venv/bin/activate && python /home/YOUR/PATH/mcp-server-bioRxiv/medrxiv_server.py"
      ],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

After restarting Claude Desktop, the following capabilities will be available:

### Searching Papers

You can ask Claude to search for papers using queries like:
```
Can you search bioRxiv for recent papers about genomics?
```

The search will return basic information about matching papers including:

• Paper title

• Authors

• DOI


### Getting Paper Details

Once you have a DOI, you can ask for more details:
```
Can you show me the details for paper 10.1101/003541?
```

This will return:

• Full paper title

• Authors

• Publication date

• Paper abstract

• Links to available formats (PDF/HTML)



## 📝 TODO

### download_paper

Download a paper and save it locally.

### read_paper

Read the content of a downloaded paper.

### list_papers

List all downloaded papers.

### 📝 Research Prompts

The server offers specialized prompts to help analyze academic papers:

#### Paper Analysis Prompt

A comprehensive workflow for analyzing academic papers that only requires a paper ID:

```python
result = await call_prompt("deep-paper-analysis", {
    "paper_id": "2401.12345"
})
```

This prompt includes:

- Detailed instructions for using available tools (list_papers, download_paper, read_paper, search_papers)
- A systematic workflow for paper analysis
- Comprehensive analysis structure covering:
  - Executive summary
  - Research context
  - Methodology analysis
  - Results evaluation
  - Practical and theoretical implications
  - Future research directions
  - Broader impacts

## 📁 Project Structure

- `medrxiv_server.py`: The main MCP server implementation using FastMCP
- `medrxiv_web_search.py`: Contains the web scraping logic for searching medRxiv

## 🔧 Dependencies

- Python 3.10+
- mcp[cli]>=1.4.1
- requests>=2.25.1
- beautifulsoup4>=4.9.3

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

This project is inspired by and built upon the work done in the [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) project.

## ⚠️ Disclaimer

This tool is for research purposes only. Please respect medRxiv's terms of service and use this tool responsibly.
