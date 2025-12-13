# TODO CLI

A simple, interactive command-line tool for managing your daily tasks.

## Features

- **Add, Update, and Delete Tasks**: Easily manage your tasks with simple commands.
- **View All Tasks**: Get a clear overview of all your tasks in a clean, organized table.
- **Persistent Storage**: Your tasks are saved to a `tasks.json` file, so you won't lose them.
- **Interactive and User-Friendly**: The app guides you through the available options.
- **Colored and Formatted Output**: Utilizes the `rich` library to provide a visually appealing and easy-to-read interface.

## How to Run the App

1.  **Prerequisites**: Make sure you have Python 3 installed on your system.
2.  **Install Dependencies**: This project uses the `rich` library. You can install it using pip:
    ```bash
    pip install rich
    ```
3.  **Run the Application**: Execute the `main.py` file from your terminal:
    ```bash
    python main.py
    ```

## Bonus Features Implemented

### File-Based Storage

This application uses a file-based storage system. All your tasks are saved in a `tasks.json` file in the root directory of the project. This means your tasks are persistent across sessions. If the file doesn't exist, it will be created automatically when you add your first task.

### Color and Sleek Output

To enhance the user experience, the application uses the `rich` library to provide colored and well-formatted output. This includes:

- **Styled Menus**: The main menu and other prompts are styled for clarity.
- **Task Table**: Tasks are displayed in a beautifully formatted table with colors to indicate priority and status, making it easy to get a quick overview of your to-do list.
- **Informative Messages**: Success, error, and warning messages are color-coded to quickly draw your attention.

### SQLite for Persistent Storage

This application supports SQLite as a configurable persistent storage option. By default, tasks are stored in a `tasks.json` file, but you can easily switch to using a SQLite database for more robust and scalable task management. When enabled, tasks are stored in a `tasks.db` file, providing a more structured and efficient way to handle your to-do list. This feature makes the application more flexible and powerful, catering to different user needs and preferences.

## Refactoring with Gemini CLI

I used the Gemini CLI to refactor the codebase. Gemini was able to help me refactor the code one by one, without adding any new files to the project, keeping the structure clean and concise.