## Tools

Tools are loaded when the program initializes.

These tools are implemented in separate Python files within the `tools/` directory. Each file provides specific functionalities that the agent can use to interact with the local environment or perform specific tasks.

To expose a function to the agent for use, it should be listed in the `__all__` variable at the bottom of the respective tool file.

The available tools are:
- `finance_reporting.py`: Contains markets related functions.
- `geo.py`: Contains geolocation related functions.
- `mail.py`: Contains a function for sending email notifications.
- `read.py`: Contains a function for reading local files.
- `search.py`: Contains functions for web searching.
- `write.py`: Contains a function for writing data to local files.
