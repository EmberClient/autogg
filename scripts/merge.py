#!/usr/bin/env python3
import json
import os


def merge_configs():
    servers_dir = 'servers'
    configs = []

    for filename in os.listdir(servers_dir):
        if not filename.endswith('.json'):
            continue

        config_path = os.path.join(servers_dir, filename)
        with open(config_path, 'r') as f:
            config = json.load(f)
            # Add the server name from the filename
            config['name'] = os.path.splitext(filename)[0]
            configs.append(config)

    # Sort configs by name for consistency
    configs.sort(key=lambda x: x['name'])

    # Write merged configuration
    with open('merged.json', 'w') as f:
        json.dump(configs, f, separators=(',', ':'))
        f.write('\n')


if __name__ == '__main__':
    merge_configs()
