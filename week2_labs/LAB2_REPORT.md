# Lab 2 Documentation 
# Lab 2 Report: Git Version Control & Flet GUI Development

**Student Information:**

*   **Name:** Divino Al D. Ricafort
*   **Student ID:** 231002032
*   **Section:** BSCS-3A
*   **Date:** September 3, 2025

---

## I. Git Version Control

This section details the implementation and demonstration of Git version control practices throughout the lab.

### A. Repository Setup and Configuration

*   **GitHub Repository:** [\[Divino's Github Repository\]](https://github.com/thebaynal/cccs106-projects)
*   **Local Repository:** Successfully initialized and linked to the remote repository.
*   **Commit History:**
    *   **Total Commits:** `9`
    *   **Commit Descriptions:** All commits feature clear, descriptive messages following best practices.

### B. Git Skills Demonstrated

The following Git functionalities were actively utilized and demonstrated:

*   ✅ **Initialization & Configuration:** `git init`, `git config`
*   ✅ **Basic Workflow:** `git add`, `git commit`, `git push`
*   ✅ **Branching & Merging:** `git branch`, `git checkout`, `git merge`
*   ✅ **Remote Management:** `git clone`, `git remote add`, `git pull`

---

## II. Flet GUI Applications

This section provides an overview of the Flet GUI applications developed for this lab.

### A. `hello_flet.py`

*   **Status:** ✅ **Completed**
*   **Key Features:**
    *   Interactive greeting message.
    *   Dynamic display of student information.
    *   Implementation of modal dialog boxes for user feedback/interaction.
*   **UI Components Utilized:** `Text`, `TextField`, `Button`, `Dialog`, `Container`.
*   **Notes/Observations:**
    *   [Briefly describe any challenges faced, e.g., "Struggled initially with dialog box positioning, resolved by understanding `barrier_dismissible`."]
    *   [Mention any interesting discoveries or optimizations.]

### B. `personal_info_gui.py`

*   **Status:** ✅ **Completed**
*   **Key Features:**
    *   Comprehensive form for capturing personal details.
    *   Utilized various input controls: `TextField`, `Dropdown`, `RadioGroup`.
    *   Generated a dynamic profile display based on user input.
    *   Incorporated scrolling for content overflow management.
*   **Error Handling:**
    *   Implemented input validation to ensure data integrity.
    *   Provided clear user feedback for invalid inputs.
*   **Notes/Observations:**
    *   [Briefly describe any challenges faced, e.g., "Ensuring seamless data transfer between form fields and the profile display required careful state management."]
    *   [Mention any design choices or improvements.]

---

## III. Technical Skills Developed

### A. Git Version Control

*   Deepened understanding of repository structure and lifecycle.
*   Mastered the fundamental Git workflow for tracking and managing code changes.
*   Gained proficiency in branching strategies for feature development and merging code.
*   Acquired practical skills in interacting with remote repositories for collaboration and backup.

### B. Flet GUI Development

*   **Flet Version:** 0.28.3
*   **Core Concepts:**
    *   Effective use of Flet's declarative UI syntax.
    *   Efficient page configuration and layout management (`Row`, `Column`, `Container`).
    *   Robust event handling for interactive user experiences.
    *   Application of modern UI design principles for intuitive interfaces.

---

## IV. Challenges and Solutions

This section outlines the primary technical hurdles encountered during the lab and the strategies employed to overcome them.

*   **Challenge 1:** Errors in the initial code given.
    *   **Solution:** Updated the code so it'll run properly.
*   **Challenge 2:** The proper flow of using the Git command in the CMD.
    *   **Solution:** Recognized and familiarized the proper flow of updating the version in using git. 

---

## V. Learning Outcomes

This lab provided significant insights into both version control and GUI development.

*   **Version Control:** I now have a solid understanding of how Git facilitates efficient code management, collaboration, and history tracking. The importance of descriptive commit messages and branching strategies for project organization has become clear.
*   **GUI Development:** Flet offers a powerful and intuitive way to build cross-platform desktop applications. I learned to structure layouts, manage UI components, and create interactive user experiences.
*   **Integration:** The lab highlighted the synergy between robust version control practices and iterative development of functional applications.

---

## VI. Screenshots (Placeholder)

### A. Git Repository Snapshot

*   **GitHub Repository:** A screenshot of the GitHub repository showcasing the project files, README, and commit history.
    *   ![\[Divino's Github Repository\]](lab2_screenshots\github_repo_ss.png)

    * [\[Divino's Github Repository\]](https://github.com/thebaynal/cccs106-projects)

*   **Local Git Log:** A visual representation of the local commit history obtained via `git log`.

    *   ![\[Divino's Github Repository\]](lab2_screenshots\git_log.png)

### B. GUI Applications Showcase

*   **`hello_flet.py` in Action:** A screenshot demonstrating the interactive greeting, student info display, and an active dialog box.

    *   ![\[Student Info Display\]](lab2_screenshots\hello_flet.png)

    *   ![\[Student Info Display\]](lab2_screenshots\info.png)

*   **`personal_info_gui.py` - Form & Profile:** A screenshot showing the filled personal information form and the generated profile display.

    *   ![\[Student Info Display\]](lab2_screenshots\student_info.png)
    
    * ![\[Student Info Display\]](lab2_screenshots\student_info_w.png)

---

## VII. Future Enhancements

*   **`hello_flet.py`:**
    *   Add a button to clear the input field.
    *   Implement a simple animation for the greeting.
    *   Added comments to further the readability of the code. 
*   **`personal_info_gui.py`:**
    *   Add more complex form elements (e.g., DatePicker, CheckboxGroup).
    *   Implement saving the generated profile to a file (e.g., TXT, JSON).
    *   Explore Flet's theming capabilities for a more polished look.
*   **General:**
    *   Create a new branch for each feature to practice Git workflow more rigorously.
    *   Experiment with different Flet layout widgets to optimize responsiveness.