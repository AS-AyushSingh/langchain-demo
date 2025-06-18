# Python Workspace

This repository contains a simple Python project structure.

## Files and Directories

- **main.py**  
  The main entry point of the application.

- **constants.py**  
  Contains constant values used throughout the project.

- **requirements.txt**  
  Lists the Python dependencies required to run the project.

- **myenv/**  
  Python virtual environment directory (auto-generated, should not be edited manually).

- **__pycache__/**  
  Directory for Python bytecode cache files (auto-generated).

## Getting Started

1. **Clone the repository**

2. **Create a virtual environment**  
   (Skip if `myenv/` already exists)
   ```sh
   python -m venv myenv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```sh
     myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source myenv/bin/activate
     ```

4. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```sh
   python main.py
   ```

## Notes

- Do not edit files in `myenv/` or `__pycache__/`.
- Add new dependencies to
