# neo4j-graph-play

### Directory 구조
. 
├── README.md
├── config
│   ├── __init__.py
│   └── service.yaml => 생성해야함.
├── data
│   ├── create_query.md
│   └── data.json
├── playground
│   ├── 1_neo4j_create_graph.ipynb
│   └── 2_langchain_neo4j_example.ipynb
├── requirements.txt
└── src
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── neo4j_connector.cpython-312.pyc
    │   └── utils.cpython-312.pyc
    ├── neo4j_connector.py
    └── utils.py

### service.yaml format
```
openai:
  api_key: ...
  llm_model: ...
  llm_max_tokens: ...

azure:
  openai_canada:
    api_version: ...
    api_base: ...
    api_key: ...
    llm_deployment: ...
    llm_model: ...
    llm_max_tokens: ...

neo4j:
  uri: ...
  username: ...
  password: ...
```

### .vscode/settings.json
```
{
    // "terminal.integrated.defaultProfile.linux": "bash",
    // "githubIssues.issueBranchTitle": "feature/${issueNumber}-${sanitizedIssueTitle}",
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "notebook.formatOnSave.enabled": true,
    "jupyter.notebookFileRoot": "${workspaceFolder}",
    "[python]": {
      "editor.formatOnSave": true,
      "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "files.exclude": {
      "**/__pycache__": true
    },
    // "python.analysis.extraPaths": ["/opt/LightRAG"],
    // "python.testing.pytestEnabled": true,
    // "python.testing.pytestArgs": ["-s", "-vv", "tests"],
    "terminal.integrated.env.linux": {
      "PYTHONPATH": "${workspaceFolder}"
    },
    "terminal.integrated.env.osx": {
      "PYTHONPATH": "${workspaceFolder}"
    },
    "terminal.integrated.env.windows": {
      "PYTHONPATH": "${workspaceFolder}"
    },
    "files.eol": "\n",
  }
```