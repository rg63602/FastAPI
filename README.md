# FastAPI MongoDB Integration Project

This project is a sample application demonstrating how to integrate a FastAPI backend with a MongoDB database. It includes examples of CRUD operations and uses Jinja2 templates for rendering HTML.

# Installation & Setup Project
Execute below commonds to install required python library.
 ```
 pip install -r requirements.txt
 
```

### MongoDB Setup

This project requires a running MongoDB instance.

The MongoDB connection URI is currently hardcoded in `main.py`. It is highly recommended to move this to an environment variable (e.g., `MONGODB_URI`) for security and flexibility.

Update the `uri` variable in `main.py` to fetch from an environment variable if you choose to do so. For example: `uri = os.getenv("MONGODB_URI", "mongodb+srv://user:pass@cluster.mongodb.net/yourdb")` (ensure `import os` is added).

### Running the Application

To run the FastAPI development server, use the following command: `uvicorn main:app --reload`

## API Endpoints

### GET /

- **Description:** Serves the main HTML page (`index.html`). This page fetches and displays a list of items from the MongoDB `fastapi.item` collection.
- **Request:** No specific request parameters.
- **Response:** HTML content rendered from `templates/index.html`.

## Project Structure

- `main.py`: The core FastAPI application file. It defines routes, connects to MongoDB, and handles application logic.
- `requirements.txt`: A list of all Python dependencies required for this project. Install them using `pip install -r requirements.txt`.
- `static/`: Contains static files, such as CSS (`style.css`) and JavaScript, used by the HTML templates.
- `templates/`: Holds Jinja2 HTML templates. `index.html` is used to display data from the database.
- `Tutorial/`: This directory contains Python scripts (`PythonTypes.py`) that appear to be for learning or example purposes and may not be part of the main application's runtime. Review these scripts for specific examples or utility functions they might offer.
- `.gitignore`: Specifies intentionally untracked files that Git should ignore.
- `README.md`: This file - providing an overview, setup instructions, and documentation for the project.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName` or `bugfix/YourBugFix`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeatureName`).
6. Open a Pull Request.

Please ensure your code adheres to any existing styling and that you provide clear commit messages.

## License

This project is currently not licensed. Please add a license file (e.g., `LICENSE.md`) and update this section if you choose to license it.

Consider common open-source licenses like MIT, Apache 2.0, or GPLv3.