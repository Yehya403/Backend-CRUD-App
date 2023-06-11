# Python CRUD App using Flask

This repository contains the backend code for a CRUD (Create, Read, Update, Delete) application developed using Python and Flask. The application is designed to handle data operations on a specific resource, such as users, products, or any other entity. It is containerized using Docker for easy deployment and scalability.

## Technologies Used

The backend code is implemented using the following technologies and frameworks:

- Python: A widely used programming language known for its simplicity and versatility.
- Flask: A lightweight web framework for building web applications in Python.
- Docker: A platform for containerizing applications.

## Local Setup Instructions

To set up the backend code locally, follow the instructions below:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/Yehya403/backend-crud-app.git
   ```

2. Navigate to the project directory:

   ```
   cd backend-crud-app
   ```

### Running Locally:

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Start the application:

   ```
   python app.py
   ```

### Running with Docker:

3. Build the Docker image:

   ```
   docker build -t backend-crud-app .
   ```

4. Run the Docker container:

   ```
   docker run -d -p 5000:5000 backend-crud-app
   ```

5. The backend server should now be running on `http://localhost:5000`. You can test the API endpoints using a tool like Postman or by integrating with a frontend application.

## API Endpoints

The following API endpoints are available for interacting with the CRUD application:

- `GET /api/persons`: Retrieve all resources.
- `GET /api/persons/{id}`: Retrieve a specific resource by ID.
- `POST /api/persons`: Create a new resource.
- `PUT /api/persons/{id}`: Update an existing resource.
- `DELETE /api/persons/{id}`: Delete a specific resource by ID.

Please refer to the code documentation and comments for more details on the request/response formats and data validations.

## Contribution

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open a pull request or submit an issue.

## License

This project is licensed under the MIT License. Feel free to use and modify the code as per your needs.

## Acknowledgements

This application was built using the Flask web framework. Special thanks to the Flask community for their amazing work.

For more information on Flask, visit the Flask documentation.
