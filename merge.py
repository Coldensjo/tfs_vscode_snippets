import json

def load_json(filename):
    """Load a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def merge_snippets(snippets1, snippets2):
    """Merge two snippet dictionaries."""
    merged = snippets1.copy()

    for key, value in snippets2.items():
        if key not in merged:
            merged[key] = value
        elif merged[key] != value:
            merged[key] = value

    return merged

def save_json(data, filename):
    """Save data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    # Load the JSON files
    file1 = "lua.json"
    file2 = "lua2.json"
    
    snippets1 = load_json(file1)
    snippets2 = load_json(file2)

    # Merge the snippets
    merged_snippets = merge_snippets(snippets1, snippets2)

    # Save the merged snippets to a new file
    merged_file = "merged_lua.json"
    save_json(merged_snippets, merged_file)
    print(f"Snippets merged and saved to {merged_file}")

if __name__ == "__main__":
    main()
