# Lab 1 Report: Environment Setup and Python Basics

**Student Name:** Divino Al D. Ricafort\
**Student ID:** 231002032\
**Section:** BSCS-3A\
**Date:** August 26, 2025

---

# Environment Setup

### Python Installation

* **Python Version:** 3.113.5
* **Installation Issues:** None encountered.
* **Virtual Environment Created:** `cccs106_env_lastname`

### VS Code Configuration

* **Python Extension:** Installed and configured
* **Interpreter:** Set to `cccs106_env_lastname/Scripts/python.exe`

### Package Installation

* **Flet Version:** 0.28.3
* **Other Packages:**

  * `tkinter` (for GUI calculator)
  * `math` (standard library, for advanced functions)

---

# Automatic Environment Activation

To automate activation of the virtual environment, I created a **batch file**:

```bat
@echo off
CALL "C:\Users\thebaynal\Documents\Code\BSCS3A\App Development\workspace_ricafort\cccs106-projects\cccs106_env_ricafort\Scripts\activate.bat"
cmd /k
```

**Features:**

* Activates the virtual environment automatically.
* Navigates to the project directory.
* Keeps the terminal open for further commands.

---

# Programs Created

### 1. `hello_world.py`

* **Status:**   <span style="color:green">✅ Completed</span>
* **Features:** Displays student information, calculates age, shows system info.
* **Notes:** Reinforced Python basics (print, variables, system modules).

---

### 2. `basic_calculator.py`

* **Status:**   <span style="color:green">✅ Completed</span>
* **Features:** Performs basic arithmetic (+, -, ×, ÷), error handling, min/max calculation.
* **Notes:** Learned input validation and exception handling.

---

### 3. `advanced_calculator.py` (Tkinter GUI)

* **Status:** ✅ Completed
* **Features:**

  * Graphical calculator using Tkinter.
  * Buttons for numbers, operators, and advanced functions.
  * Clear button (`C`) and error handling.
* **Notes:** Learned about GUI development in Python with Tkinter widgets.

---

# Challenges and Solutions

* **Issue:** Virtual environment not recognized in VS Code.

  * **Solution:** Manually set the Python interpreter to the environment’s `Scripts/python.exe`.

* **Issue:** Path error in batch file due to spaces in folder names.

  * **Solution:** Enclosed the path in quotation marks (`" "`).



---

# Learning Outcomes

* Understood how to properly set up a **Python development environment** with virtual environments and VS Code.
* Understood how to automatically **set the environment** in the `cmd` with just one click by utilizing a `batch` file. 
* Learned how to build both **command-line and GUI applications** in Python.
* Strengthened problem-solving skills by troubleshooting environment issues.
* Understood the proper file organization in projects such as this.
* Learned various shortcuts and commands to build a project.
---

# Screenshots

* **ENVIRONMENT SETUP**
![ENVIRONMENT SETUP](lab1_screenshots\environment_setup.png)

* **VSCODE SETUP**
![VSCODE SETUP](lab1_screenshots\vscode_setup.png)

* **`hello.world.py` OUTPUT**
![Hello World Output](lab1_screenshots\hello_world_output.png)

* **BASIC CALCULATOR**
![Basic Calculator Output](lab1_screenshots\basic_calculator_output.png)

* **ADVANCE CALCULATOR**
![advance calculator](lab1_screenshots\advance_calculator_output.png)

---
# the end.