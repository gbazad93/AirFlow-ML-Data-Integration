# Setting Up Your IDE for Airflow Development

In this project, we recommend using **Visual Studio Code (VS Code)** as the integrated development environment (IDE). However, you are free to use any IDE or text editor of your choice. Below are instructions to install and configure VS Code on Ubuntu.

---

## Installing VS Code

Follow one of the methods below to install VS Code on your Ubuntu system:

---

### Method 1: Using Snap (Recommended)

1. **Open Terminal**: Press `Ctrl + Alt + T` to open the terminal.
2. **Install Snap (if not installed)**:
   ```bash
   sudo apt update
   sudo apt install snapd
   ```
3. **Install VS Code using Snap**:
   ```bash
   sudo snap install code --classic
   ```
4. **Launch VS Code**:
   - Run the following command in the terminal:
     ```bash
     code
     ```
   - Alternatively, search for **"Visual Studio Code"** in the applications menu.

### Method 2: Using the Official Microsoft Repository

1. **Update and Install Prerequisites**  
   Update your system and install the required packages:
   ```bash
   sudo apt update
   sudo apt install -y software-properties-common apt-transport-https wget


2. **Import the Microsoft GPG Key**  
   Import the GPG key to verify Microsoft packages:
   ```bash
   wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
   
   sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
   ```

3. **Enable the VS Code Repository**  
   Add the Visual Studio Code repository to your system:
   ```bash
   sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
   ```

4. **Install VS Code**  
   Update your package list and install Visual Studio Code:
   +bash
   sudo apt update
   sudo apt install code
   +bash

5. **Launch VS Code**  
   To open Visual Studio Code:
   - Run the following command in the terminal:
     ```bash
     code
     ```
   - Alternatively, search for **"Visual Studio Code"** in the applications menu.

---

## Adding the Project Folder to VS Code Explorer

Once Visual Studio Code is installed and launched, you can set up your project folder for easier development:

1. **Open the Explorer Sidebar**:  
   On the left-hand menu of VS Code, click the **Explorer** icon (usually the first icon at the top).

2. **Open the Project Folder**:  
   - Click **Open Folder** at the top of the Explorer section or use the menu:  
     **File** → **Open Folder**.
   - Navigate to the Airflow home directory and open it:  
     ```
     /home/username/airflow
     ```
     Replace `username` with your actual Ubuntu username.

3. **Access All Project Files**:  
   After opening the folder, you will have access to all the files and folders needed for this project, such as:
   - **`dags/`**: Contains your DAG definitions.
   - **`helpers/`**: Contains custom scripts or modules used in your workflows.

4. **Create or Edit Files**:  
   You can now directly create or edit `.py` files in their respective paths using VS Code. For example:
   - Add new DAG files in the **`dags/`** folder.
   - Place helper scripts in the **`helpers/`** folder.

---

With this setup, you’re ready to begin developing and managing your Airflow project using Visual Studio Code!
