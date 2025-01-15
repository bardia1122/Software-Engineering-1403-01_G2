# Text Optimization Microservice

This Django-based microservice is designed to process text inputs by normalizing them, removing unnecessary spaces, and fixing issues with parentheses, brackets, and other delimiters. It uses **Hazm**, a powerful library for Persian text processing, and includes enhancements for handling delimiters. A responsive client-side interface built with **React** is used for interacting with the service.

---

## Features

### Core Functionalities

1. **Text Normalization**:

   - Removes extra spaces.
   - Fixes incorrect half-spaces (نیم فاصله) using **Hazm**.

2. **Delimiter Handling**:

   - Corrects unbalanced parentheses `()`, curly braces `{}`, and square brackets `[]`.

3. **Suggestions**:

   - Generates a list of suggestions for the changes made during optimization.
   - Highlights portions of text that were altered for user review.

4. **Persistence**:
   - Saves the original and optimized texts in the database for future reference.
   - Also saves start, end and suggestion from the input text in cloud database.

### Client-Side

- **Responsive UI**: Built with **React** to provide a seamless user experience.
- Interacts with the Django backend through a RESTful API.

---

## Technical Details

### Libraries and Frameworks

- **Backend**: Django + Django REST Framework.
- **Text Processing**: Hazm library for Persian text normalization.
- **Frontend**: React for a modern, responsive user interface.

### Code Structure

- `logic.py`: Handles text normalization and delimiter correction.
- `parse.py`: Generates suggestions based on differences between input and output text.
- `models.py`: Defines the database schema for storing text optimizations.
- `views.py`: Contains API endpoints for processing text and managing suggestions.
- `serializers.py`: Defines data serialization and deserialization for API responses.
- `tests.py`: Run tests for every component.

---

## Setup and Installation

### Prerequisites

1. Python 3.8 or higher.
2. Django 5.1.5.
3. Node.js (for React frontend).
4. Hazm library.
5. Virtual environment tools like `venv` or `virtualenv`.

### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up Backend**:

   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Linux/MacOS
     venv\Scripts\activate     # Windows
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```
   - Run the development server:
     ```bash
     python manage.py runserver
     ```

3. **Set Up Frontend**:
   - Navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the development server:
     ```bash
     npm start
     ```

---

## Testing

- **Automated Tests**:
  - 29 automated tests cover core functionalities of the service.
  - To run the tests:
    ```bash
    python manage.py test
    ```

---

## Future Enhancements

- Add support for additional delimiter types.
- Improve the suggestion algorithm to handle complex cases.
- Implement more detailed logging for debugging.

---

## Contributors

- Group 3
  - Special thanks to all contributors (Bardia Sabbagh Kermani, Roza Ganjipour, Mahsa Kashani and Hossein Goodarzi Mojarrad) who helped design, develop, and test this service.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to reach out with any questions or feedback about the project!
