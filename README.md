# Smart Expense Tracker API

## Project Overview

Smart Expense Tracker API is a RESTful web application built using Python and Flask. It helps users manage their daily expenses through simple API endpoints. The application stores expense data in a JSON file and supports complete CRUD operations along with category-wise filtering and expense summaries.

## Features

- Add a new expense
- View all expenses
- View an expense by ID
- Update an existing expense
- Delete an expense
- Filter expenses by category
- Calculate total expenses
- Calculate total amount by category
- JSON-based data storage
- Automated API testing using Pytest

## Technologies Used

- Python 3
- Flask
- JSON
- Pytest
- Postman

## Project Structure

smart-expense-tracker/
│
├── src/
│   ├── app.py
│   └── expenses.json
│
├── tests/
│   ├── test_api.py
│   └── expenses.json
│
├── .gitignore
├── AI_NOTES.md
├── README.md
├── requirements.txt
│
└── venv/ (not included in GitHub)

## Installation

Clone the repository


git clone <repository-url>


Open the project

cd smart-expense-tracker

Install dependencies

pip install -r requirements.txt

## Running the Application

Move into the source folder
cd src

Run the Flask application
python app.py

The server will start at
http://127.0.0.1:5000

## Running Tests

Run the following command from the project root
cd tests
python -m pytest

Expected output
5 passed

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home |
| POST | /expenses | Add Expense |
| GET | /expenses | Get All Expenses |
| GET | /expenses/<id> | Get Expense by ID |
| PUT | /expenses/<id> | Update Expense |
| DELETE | /expenses/<id> | Delete Expense |
| GET | /expenses/category/<category> | Filter by Category |
| GET | /expenses/total | Total Expenses |
| GET | /expenses/total/<category> | Total by Category |

## Sample Request

json
{
        "id": 1,
        "title": "Laptop Bag",
        "amount": 600.0,
        "category": "Shopping",
        "date": "2026-08-01"
}

## Sample Response

json
{
        "id": 1,
        "title": "Laptop Bag",
        "amount": 600.0,
        "category": "Shopping",
        "date": "2026-08-01"
}

## Testing

The API was tested using
- Postman
- Pytest
All endpoints were successfully verified.


## Future Improvements

- Database integration
- User authentication
- Monthly reports
- Expense search
- Docker support
- Cloud deployment

## Author
Vinayak Kulkarni