# Automated Application Installer
This Automated Application Installer is a Python script designed to simplify the process of installing multiple applications on Windows machines. It provides a user-friendly interface that allows users to select the applications they want to install, automatically downloads them, and executes the installation commands.

## Features
- Graphical user interface (GUI) for easy application selection.
- Downloads applications from provided URLs.
- Executes installation commands for the selected applications.
- Provides feedback on successful installations.

# Usage
1. Clone or download the repository to your local machine.
2. Make sure you have Python installed (version 3.6 or above).
3. Install the required Python packages:
   ```
    pip install -r requirements.txt
   ```

4. Modify the `applications.json` file:
Add your desired applications, including their names, URLs, and installation commands.
5. Run the script:
```
python installer.py
```
6. The GUI will appear with checkboxes for each application. Select the desired applications to install.

7. Click the "Install" button to start the installation process. The script will download the selected applications and execute the installation commands.

8. Monitor the console output for the progress and confirmation of successful installations.

9. Once the installation is complete, the selected applications will be installed on your system.

## Limitations
- Currently supports Windows machines only.
- Ensure that the provided URLs are valid and accessible to download the application installers.
- Verify that the installation commands are correct and compatible with the applications you intend to install.

_This project was created using ChatGPT, a powerful language model developed by OpenAI._