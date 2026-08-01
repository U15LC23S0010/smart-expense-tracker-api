# AI_NOTES.md

## AI Usage Summary

This project was developed primarily by me with assistance from ChatGPT. AI was used as a learning aid for understanding Flask concepts, debugging issues, improving code quality, and preparing project documentation. All AI-generated suggestions were reviewed, modified where necessary, tested thoroughly, and verified before being included in the final project.

### AI-Assisted

AI helped with:
- Explaining Flask concepts and REST API implementation.
- Providing the initial REST API structure and endpoint suggestions.
- Implementing category-wise filtering logic.
- Fixing implementation issues and verifying the application.
- Debugging Flask routes and JSON handling issues.
- Reviewing parts of the application code and suggesting improvements.
- Assisting in preparing the README.md and AI_NOTES.md documentation.

### Written and Completed by Me

Tasks done for this project, including:
- Planning the overall project structure.
- Setting up the Flask application.
- Implementing and modifying all REST API endpoints.
- Implementing CRUD operations.
- Implementing expense summary and category-wise total endpoints.
- Managing JSON-based expense storage.
- Fixing implementation issues and verifying the application.
- Testing every API endpoint manually using Postman.
- Running automated tests using Pytest and verifying all tests passed.
- Reviewing, understanding, and modifying AI-generated suggestions before using them.
- Preparing the final project for submission.

## What I validated, tested, or changed in the AI output

I did not use AI-generated code directly without verification. Every suggestion was reviewed and tested before being included in the project.

The changes I made include:

- Fixed bugs in the delete functionality.
- Corrected expense ID generation logic.
- Fixed total expense calculations.
- Improved error handling for invalid requests.
- Modified API responses to match the assignment requirements.
- Verified all CRUD operations using Postman.
- Executed automated tests using `python -m pytest` and confirmed all tests passed.
- Ensured that testing data was stored separately from the application's actual data.

## AI suggestions I decided not to use

I chose not to include the following AI suggestions because they were beyond the scope of the assignment:

- Docker containerization(optional as mentioned in the given task).
- Database integration (SQLite/MySQL).
- User authentication and authorization.
- Advanced logging utilities.
- Additional utility modules that were not required.
- Search and reporting features.

These features were intentionally excluded to keep the project focused on the assignment requirements.

## Testing
The application was tested manually using Postman and automatically using Pytest.

Automated tests were executed using:

python -m pytest
All tests completed successfully.

## Reflection

AI acted as a coding assistant and learning resource throughout the development process. However, the implementation, debugging, testing, validation, project organization, and final verification were completed by me. Working on this project improved my understanding of Flask, REST APIs, JSON data handling, API testing, debugging, and software development best practices.