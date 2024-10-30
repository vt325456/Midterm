# MidTerm - Python Based REPL calculator

[The Video Presentation](https://drive.google.com/file/d/1-3ttbwwZj7A58JzQJQTR9StaOtbAjC2w/view?usp=drive_link)

Welcome to the Python REPL Calculator Project, an extensible calculator showcasing key software engineering principles. Utilizing a modular architecture and the Command Pattern, it supports fundamental arithmetic operations and dynamic plugin integration. The project emphasizes clean code, robust error handling, and detailed logging, while enabling users to track calculations and export history to CSV via Pandas. Designed with scalability in mind, it incorporates CI/CD practices using GitHub Actions and environment variable configuration. A comprehensive test suite built with pytest ensures thorough validation, making this project an excellent resource for both developers and users seeking a versatile calculation tool.

## Branches


1. **master**
    - ***purpose:*** This is the main branch containing the core implementation of the REPL calculator.
    - ***Functionality***:
        - User interface for user interaction.
        - Basic arithmetic operations: addition, subtraction, multiplication, and division.
        - History management using the Pandas library.
        - Plugin system for dynamic command integration.
        - CSV export functionality for calculation history.
        - Logging for tracking operations and errors.
        - Includes the complete test suite to validate core features.

2. **development**: 
    - ***purpose:*** Serves as a staging area for integrating new features or updates before merging them into the master branch.
    - ***Functionality***:
        - Collects and tests code changes from various feature branches (e.g., commands, plugins, history, logging).
        - Ensures stability and compatibility of new functionalities.
        - Helps maintain a clean and reliable master branch while allowing ongoing development.

3. **commands**: 
    - ***Purpose***: Dedicated to implementing the Command Pattern for arithmetic operations.
    - ***Functionality***:
        - Contains command classes such as:
            - *AddCommand*: Handles addition operations.
            - *SubtractCommand*: Handles subtraction operations.
            - *MultiplyCommand*: Handles multiplication operations.
            - *DivideCommand*: Handles division operations.
            - *ExitCommand*: Manages the exit functionality.
            - Facilitates easy management and extension of command-specific code.

4. **plugins**: 
    - ***Purpose***: Manages the plugin architecture of the calculator.
    - ***Functionality***:
        - Handles the dynamic loading of new commands and features.
        - Provides a modular framework for adding and managing plugins.
        - All plugins are stored in the app/plugins/ directory for easy access and organization.

5. **logging**: 
    - ***Purpose***: Focuses on implementing or enhancing the logging system of the calculator.
    - ***Functionality***:
        - Implements detailed log tracking and error monitoring.
        - Configures logging levels and manages log files.
        - May include features like log rotation and more granular logging information to improve traceability.

6. **history**: 
    - ***Purpose:*** Manages the recording and exporting of calculation history.
    - ***Functionality:***
        - Includes a HistoryManager class for tracking operations, operands, and results.
        - Implements a CsvCommand class for exporting calculation history to CSV files.
        - Ensures that each calculation is recorded and allows users to save their session history upon exiting.
        - Contains comprehensive testing for history management and CSV export functionality.

## Features

1. **Basic Arithmetic Operations**  
   The calculator provides essential arithmetic functions, including addition, subtraction, multiplication, and division. Each of these operations is implemented using the Command Pattern, which allows for clean separation and management of individual commands. The design ensures that extending or modifying these operations is straightforward, promoting loose coupling and maintainable code. Additionally, error handling is robust, particularly in scenarios such as division by zero, where the application gracefully alerts the user to input issues without crashing.

2. **History Management & CSV Export**  
   The application automatically tracks all calculations performed during a session. It maintains a detailed record of each operation, including the operation type, operands, and results. This data is managed using the Pandas library, allowing for efficient storage and retrieval. Upon exiting, the user is prompted to save the session history to a CSV file. This feature ensures that calculations can be easily referenced or reused later. The CSV export is flexible, supporting both new file creation and appending to existing files, with a consistent file structure to enhance readability and future data analysis.

3. **Plugin-Based System**  
   The calculator’s architecture is designed with extensibility in mind, leveraging a plugin-based system to support new commands or features. This modular approach enables dynamic loading of plugins stored within a dedicated directory (`app/plugins/`). The plugin architecture ensures that new functionalities can be integrated without modifying the core codebase, allowing for continuous enhancement and scalability. This design demonstrates practical implementation of software engineering principles like loose coupling, inversion of control, and dependency injection, fostering maintainable and easily extendable code.

4. **REPL Interface**  
   The calculator features a Read-Eval-Print Loop (REPL) interface that allows for an interactive and user-friendly experience. It prompts users to select an operation and enter the required numbers, and then displays the results in a clear and concise manner. The REPL interface also offers a menu to guide users through the available commands and provides a simple exit command with optional history saving. This interactive design not only enhances usability but also showcases how REPL implementations can be applied to real-world software projects.

5. **Logging & Debugging**  
   A comprehensive logging system is integrated into the application to track all operations and handle error situations. The logging system is configurable and supports different logging levels for debugging, warnings, and critical issues. This helps in pinpointing problems quickly and monitoring the application’s behavior over time. By implementing strong logging practices, the project emphasizes the importance of tracking the internal state and operational flow, which aids in debugging and long-term maintenance.

## CI/CD Workflow Overview

Our Continuous Integration and Continuous Deployment (CI/CD) github workflow is designed to streamline development and ensure the highest quality of our code. Here’s what it does:

1. **Environment Setup**:
   - The github workflow operates on the latest Ubuntu environment, ensuring a modern and stable foundation for our project.
   - It sets up Python 3.10, providing the necessary runtime for our application.

2. **Dependency Installation**:
   - Automatically upgrades `pip` to the latest version, ensuring that we have the most up-to-date package management tools.
   - Installs essential development tools, including:
     - `flake8`: Enforces coding standards and style guidelines.
     - `pytest`: A robust framework for running our unit tests.
   - Installs all project dependencies specified in `requirements.txt`, ensuring that our environment is fully prepared for development and testing.

3. **Testing**:
   - Executes unit tests using `pytest`, validating that our application behaves as expected.
   - Conducts code quality checks with `pylint`, helping us maintain clean and readable code.
   - Performs test coverage analysis using `pytest` and `coverage`, allowing us to measure how much of our code is tested and identify areas for improvement.

This automated github workflow not only enhances our development efficiency but also ensures that we maintain high standards of code quality and reliability throughout the project lifecycle. By integrating these processes, we can focus on delivering exceptional features while minimizing the risk of bugs and regressions.


## Instructions for setting up:
1. Clone the repository:

    ```bash
    git clone git@github.com:vt325456/Midterm.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Midterm
    ```

3. Checkout the `branchname` to access the latest plugin system implementation:

    ```bash
    git checkout plugins
    git checkout commands
    etc
    ```

4. Install any dependencies (if applicable).
    ```bash
    pip3 install -r requirements.txt
    ```

5. **Run the main Python file:**
    ```bash
    python main.py
    ```

6. **Executing the application:**
    ```bash
    2024-10-29 02:20:26,460 - root - INFO - Logging configured.
    2024-10-29 02:20:26,462 - root - INFO - Environment variables loaded.
    MID TERM 
    Welcome to the Advanced Calculator
    Enter a command to execute 
    Add  Subtract  Multiply  Divide  Exit
    add
    Enter a:4
    Enter b:3
    2024-10-29 02:20:32,267 - root - INFO - Addition Between 4 and 3
    2024-10-29 02:20:32,267 - root - INFO - Result : 7
    2024-10-29 02:20:32,268 - root - INFO - Appended calculation to history - Addition
    Result: 7
    Enter a command to execute 
    Add  Subtract  Multiply  Divide  Exit
    subtract
    Enter a:10
    Enter b:4
    2024-10-29 02:20:42,306 - root - INFO - Subtract Operation Between 10 and 4
    2024-10-29 02:20:42,306 - root - INFO - Result : 6
    2024-10-29 02:20:42,307 - root - INFO - Appended calculation to history - Subtract
    Result: 6
    Enter a command to execute 
    Add  Subtract  Multiply  Divide  Exit
    multiply
    Enter a:42
    Enter b:3
    2024-10-29 02:20:51,506 - root - INFO - Multiplication Operation between 42 and 3
    2024-10-29 02:20:51,506 - root - INFO - Result : 126
    2024-10-29 02:20:51,507 - root - INFO - Appended calculation to history - Multiplication
    Result: 126
    Enter a command to execute 
    Add  Subtract  Multiply  Divide  Exit
    divide
    Enter a:126
    Enter b:42
    2024-10-29 02:21:00,466 - root - INFO - Division Operation Between 126 and 42
    2024-10-29 02:21:00,467 - root - INFO - Result : 3.0
    2024-10-29 02:21:00,467 - root - INFO - Appended calculation to history - Division
    Result: 3.0
    Enter a command to execute 
    Add  Subtract  Multiply  Divide  Exit
    exit
    2024-10-29 02:21:05,331 - root - INFO - Exiting with saving history.
    2024-10-29 02:21:05,332 - root - INFO - 
    [{'Operation': 'Add', 'Operand1': 4, 'Operand2': 3, 'Result': 7}, 
    {'Operation': 'Subtract', 'Operand1': 10, 'Operand2': 4, 'Result': 6}, 
    {'Operation': 'Multiply', 'Operand1': 42, 'Operand2': 3, 'Result': 126}, 
    {'Operation': 'Divide', 'Operand1': 126, 'Operand2': 42, 'Result': 3.0}]
    2024-10-29 02:21:05,350 - root - INFO - History has been exported to data/calculator_history.csv
    2024-10-29 02:21:05,351 - root - INFO - History is added with:
    [{'Operation': 'Add', 'Operand1': 4, 'Operand2': 3, 'Result': 7},
     {'Operation': 'Subtract', 'Operand1': 10, 'Operand2': 4, 'Result': 6}, 
     {'Operation': 'Multiply', 'Operand1': 42, 'Operand2': 3, 'Result': 126}, 
     {'Operation': 'Divide', 'Operand1': 126, 'Operand2': 42, 'Result': 3.0}]
     Exiting...
    ```

## Running Tests Locally

To replicate the CI environment locally, you can run the following commands:

```bash
# Install dependencies
pip install -r requirements.txt
pip install flake8 pytest pytest-pylint pytest-cov

# Run tests
pytest
pytest --pylint
pytest --pylint --cov
```
## Usage

To run the project:
```bash
python main.py
```

## History Management

The calculator maintains a history of all operations in a CSV file format. The history is stored in `data/calculator_history.csv`.

## Data Management

When the application is exited, it checks for the existence of a `data` folder. If the folder does not exist, it will be created automatically. The application will then prompt the user to save the calculation history. 

### Saving History

- If the user chooses to save, the history will be exported to `calculation_history.csv` within the `data` folder.
- This ensures that all calculations performed during the session are preserved for future reference.

## CSV Handling

1. **Exit Command**: When you run the `exit` command, the application will:
   - Check for the `data` folder.
   - Prompt you with a message: "Do you want to save the calculation history? (yes/no)"
   
2. **User Decision**:
   - If you respond with `yes`, the application will create the `data` folder (if it doesn't exist) and save the history to `calculation_history.csv`.
   - If you respond with `no`, the history will not be saved.

## CSV File Structure

The history is stored with the following columns:


|   Operation     |   Operand1   |   Operand2   |   Result   |
|-----------------|---------------|---------------|------------|
|   Add           |   4.0        |   3.0        |   7.0      |
|   Subtract      |   4.0        |   5.0        |   -1.0     |
|   Multiplication |   5.0       |   3.0        |   15.0     |
|   Division      |   50.0       |   2.0        |   25.0     |

Each row in the CSV contains:
- **Operation**: Type of arithmetic operation (Addition, Subtraction, Multiplication, Division)
- **Operand1**: First number in the calculation
- **Operand2**: Second number in the calculation
- **Result**: Final result of the operation

## Most commonly used Git commands in the  project
### Cloning the repository:
```bash
git clone https://github.com/vt325456/Midterm
cd Midterm
```
### Switching to the required branch:
```bash
git checkout main
git checkout <branch_name> # the branch names are mentioned above
```
### Viewing the branches
```bash
git branch -a
```
### Creating a new branch
```bash
git checkout -b new-feature-branch
```
###  Committing changes
```bash
git add .
git commit -m "Description of your changes"
```
### Pushing changes to the remote repository
```bash
git push origin <branch_name>
```
### Pulling changes from the remote repository
```bash
git pull origin <branch_name>
```
### Merging changes from one branch to another
```bash
git checkout main
git merge <branch_name>
```
**Note : Remember to always pull the latest changes before starting to work on a branch** 
```bash
git checkout branch-name
git pull origin branch-name
```
