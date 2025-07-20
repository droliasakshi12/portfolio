import os

# Define the path to the .streamlit directory in the user's home folder
config_dir = os.path.join(os.path.expanduser("~"), ".streamlit")
os.makedirs(config_dir, exist_ok=True)

# Define the path to the config.toml file
config_file = os.path.join(config_dir, "config.toml")

# Define the custom theme content
config_content = """

[theme]
base="light"
primaryColor="#010202"
backgroundColor="#9e45c3"
secondaryBackgroundColor="#439fc1"


"""

# Write the content to the config.toml file
with open(config_file, "w") as f:
    f.write(config_content.strip())

print(f"Custom Streamlit theme written to: {config_file}")