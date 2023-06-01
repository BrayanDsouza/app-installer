import tkinter as tk
import requests
import subprocess
import os

def install_applications():
    for app in applications:
        if app["selected"].get():
            url = app["url"]
            install_command = app["install_command"]

            # Download the application using requests library
            response = requests.get(url)
            with open(app['name'] + '.exe', 'wb') as file:
                file.write(response.content)

            # Execute the installation command
            install_path = os.path.abspath(app['name'] + '.exe')
            install_dir = os.path.dirname(install_path)
            os.chdir(install_dir)
            subprocess.run(install_command, shell=True)

            print(f"{app['name']} installed successfully!")

    print("All selected applications installed.")

# Define the list of applications to download
applications = [
    {
        "name": "7zip",
        "url": "https://www.7-zip.org/a/7z2300-x64.exe",
        "install_command": "7zip.exe"
    },
    {
        "name": "anydesk",
        "url": "https://download.anydesk.com/AnyDesk.exe",
        "install_command": "anydesk.exe"
    }
]

# Create the GUI
root = tk.Tk()
root.title("Application Installer")

# Create checkboxes for each application
for app in applications:
    app["selected"] = tk.BooleanVar()
    checkbox = tk.Checkbutton(root, text=app["name"], variable=app["selected"])
    checkbox.pack(anchor=tk.W)

# Create install button
install_button = tk.Button(root, text="Install Selected Applications", command=install_applications)
install_button.pack()

# Run the GUI event loop
root.mainloop()