import os
import json

def update_ff():
    """Run the npm script to update the frontend files."""
    os.system("npm run update-ff:raw")

def get_version(file_path):
    """Retrieve the version from the specified JSON file."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data["version"]["version"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error reading version from {file_path}: {e}")
        return "0.0.0"  # Return a default version in case of error

def update_readme(readme_path, old_version, new_version):
    """Update the README file with the new version number."""
    try:
        with open(readme_path, "r") as f:
            data = f.read()
        updated_data = data.replace(old_version, new_version)
        with open(readme_path, "w") as f:
            f.write(updated_data)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error writing to {readme_path}: {e}")

if __name__ == "__main__":
    surfer_file = "surfer.json"
    readme_file = "README.md"

    last_version = get_version(surfer_file)
    update_ff()
    new_version = get_version(surfer_file)

    if last_version != new_version:
        update_readme(readme_file, last_version, new_version)
        print(f"Updated from version {last_version} to version {new_version}")
    else:
        print("No version change detected.")
