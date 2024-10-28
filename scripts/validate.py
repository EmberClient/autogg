#!/usr/bin/env python3

import json
import os
from jsonschema import validate
import sys


def load_schema():
    with open('schema.json', 'r') as f:
        return json.load(f)


def validate_config(schema, config_path):
    with open(config_path, 'r') as f:
        try:
            config = json.load(f)
            validate(instance=config, schema=schema)
            return True
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {config_path}")
            print(f"Details: {str(e)}")
            return False
        except Exception as e:
            print(f"Error: Validation failed for {config_path}")
            print(f"Details: {str(e)}")
            return False


def main():
    schema = load_schema()
    servers_dir = 'servers'
    success = True

    # Check that servers directory exists
    if not os.path.isdir(servers_dir):
        print("Error: 'servers' directory not found")
        sys.exit(1)

    # Validate each configuration file
    for filename in os.listdir(servers_dir):
        if not filename.endswith('.json'):
            continue

        config_path = os.path.join(servers_dir, filename)
        print(f"Validating {filename}...")

        if not validate_config(schema, config_path):
            success = False

    if not success:
        print("\nValidation failed!")
        sys.exit(1)

    print("\nAll configurations are valid!")


if __name__ == '__main__':
    main()
