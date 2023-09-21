# VSCode LUA Snippets Installation & Merging Guide

This guide will walk you through how to install LUA snippets in VSCode and how to merge different snippets using a Python script.

## How to Install Snippets in VSCode

### 1. Access the Command Palette
- **Windows/Linux**: Press `Ctrl + Shift + P`
- **Mac**: Press `Cmd + Shift + P`

### 2. Find the Snippets Menu
- In the Command Palette, type `Snippets` and select `Configure User Snippets` from the dropdown menu.

### 3. Select LUA Snippets
- From the list of available languages and options, choose `LUA`.

### 4. Add Your Snippets
- Copy and paste your desired snippets into the opened editor.
- Save the changes. No need to restart VSCode.

## Merging Snippets Using the Python Script

### 1. Open a Terminal in a New Folder
- Depending on your OS, use `cmd`, `bash`, or `powershell`.

### 2. Clone the Repository
`git clone https://github.com/Coldensjo/tfs_vscode_luasnippet.git`

### 3. Add Your LUA Snippets
- Copy your LUA snippets file into the cloned folder.

### 4. Rename the Snippets Files
- Rename your snippets files to `lua.json` and `lua2.json`.

### 5. Run the Merging Script
`python merge.py`

### 6. Contribute Back
- Made improvements? Consider creating a pull request!
