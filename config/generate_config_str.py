import json
import sys


def generate_config_str(config_file) -> str:
    """
    Generate a string from the JSON configuration file.

    Returns:
    - config_str: str

    """
    # Load the JSON configuration
    with open(f"{config_file}", "r") as file:
        config_data = json.load(file)

    # Convert to string
    config_str = json.dumps(config_data)
    return config_str


def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_config_file> [output_env_file]")
        sys.exit(1)
    config_file_path = sys.argv[1]
    output_file = (
        sys.argv[2] if len(sys.argv) > 2 else ".env"
    )  # Default to .env if no second argument is provided

    config_str = generate_config_str(config_file_path)

    # Write the serialized config to an .env file
    with open(output_file, "w") as file:
        file.write(f"COMMISSION_CONFIG='{config_str}'\n")

    print(f"Configuration written to {output_file} successfully.")


if __name__ == "__main__":
    main()
