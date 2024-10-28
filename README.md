# AutoGG Server Configurations

Welcome to the Ember Client AutoGG repository! Here, we manage server-specific configurations for AutoGG, defining trigger messages, commands, and validation rules for each Minecraft server.

## Repository Structure

- **`servers/`**: Holds individual server configurations, with each server having its own JSON file (e.g., `hypixel.json`, `mineplex.json`).
- **`schema.json`**: Defines the structure and requirements for each configuration file.
- **`scripts/`**: Python scripts for validation and merging.
  - `validate.py`: Checks each server configuration against the schema.
  - `merge.py`: Combines all configurations into a single JSON file.

## Contributing & Adding a New Server

Want to add a new server or update existing configurations? Follow these steps:

1. Fork this repository and create a new branch for your changes.
2. Add a new JSON file in the `servers` directory, or modify an existing one.
   - Name it `servername.json` (for example, `hypixel.json`).
   - List only the main domain in the `hosts` array — no need to include subdomains. Use this template as a guide:
   ```json
   {
     "hosts": ["hypixel.net"],
     "triggers": ["Winner: ", "Game Over!"],
     "command": "/ac {message}",
     "messageValidation": {
       "startsWith": " ",
       "excludePatterns": []
     }
   }
   ```
3. Open a pull request and wait for the validation checks to pass.

**Note**: The `command` field must include a `{message}` parameter placeholder which will be replaced with the actual message at runtime.

## Deployment

Once changes are merged into the main branch:

1. All configurations go through final validation.
2. Valid files are merged into a single JSON file.
3. The file is uploaded to our CDN.
4. The latest configuration is available at `https://cdn.emberclient.com/autogg/servers.json`.
