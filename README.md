# TaskManager

TaskManager is a simple Flask web application that allows users to register, log in, and manage their tasks. The application uses SQLite for the database, SQLAlchemy for ORM, and Alembic for database migrations. It also incorporates Bootstrap for styling and jQuery for interactivity, including an autocomplete user search feature.

## Features

- User registration, login, and logout functionalities
- User profile page with dynamic routing
- SQLite database with SQLAlchemy and Alembic for migrations
- Bootstrap for responsive design and styling
- jQuery for frontend interactivity
- Autocomplete user search with jQuery UI
- Navbar with user-specific links and search functionality

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/taskmanager.git
    cd taskmanager
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root and add the following content:
    ```plaintext
    SECRET_KEY=your_secret_key
    DATABASE_URL=sqlite:///app.db
    ```

5. **Run database migrations**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the Flask application**:
    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Usage

- **Register a new user**:
    Go to `http://127.0.0.1:5000/register` and create a new account.
  
- **Log in**:
    Go to `http://127.0.0.1:5000/login` and log in with your credentials.

- **User profile**:
    Access your profile at `http://127.0.0.1:5000/@<username>`.

- **Autocomplete user search**:
    Use the search bar in the navbar to find users by their username.

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
