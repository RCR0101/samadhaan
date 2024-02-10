# Samadhaan

## Introduction
Samadhaan is an AI/ML-driven grievance management system designed to facilitate the auto-categorization of grievance reports and assist citizens with common queries via a ministry-specific chatbot. This system aims to streamline the grievance handling process by providing an efficient way to categorize, track, and respond to grievances.

## Problem Statements
- **Problem Statement 1:** Develop an AI/ML-driven system for topic clustering/modelling to enable auto-categorisation of received grievance reports.
- **Problem Statement 2:** Develop an AI/ML-driven Chatbot to assist citizens with filing grievances on the CPGRAMS portal.

## Workflow Overview
1. **Samadhaan App:** Users sign in, enter grievances in their preferred language, and post them.
2. **Samadhaan Server:** Processes grievances, utilizing AI models for department prediction, severity assessment, and summarization.
3. **Samadhaan E-portal:** AI-enhanced grievances are made available to the respective departments for action.
4. **Samadhaan App:** Users receive notifications upon responses to their grievances.

## REST API Endpoints
- **Complaint Management:** Endpoints for retrieving, creating, and updating complaints.
- **User & Department Management:** Endpoints for user and department details retrieval and creation.

### Detailed Endpoints
(Include a concise list of endpoints with brief descriptions, methods, and response formats.)### REST API Endpoints Documentation

#### 1. Get All Complaints
- **Endpoint:** `/Complaints`
- **Method:** `GET`
- **Description:** Retrieves a list of all complaints in the system.
- **Request Parameters:** None
- **Response:** Returns a JSON array of complaints.

#### 2. Get Complaint by ID
- **Endpoint:** `/Complaints/<path:id>`
- **Method:** `GET`
- **Description:** Fetches a specific complaint by its unique ID.
- **Request Parameters:** `id` - The unique identifier of the complaint.
- **Response:** Returns a JSON object of the complaint details.

#### 3. Get Complaints by User Code
- **Endpoint:** `/Complaints/User/<user_code>`
- **Method:** `GET`
- **Description:** Retrieves all complaints associated with a specific user, identified by a unique user code.
- **Request Parameters:** `user_code` - The unique code of the user.
- **Response:** Returns a JSON array of complaints linked to the specified user.

#### 4. Get All Departments
- **Endpoint:** `/Departments`
- **Method:** `GET`
- **Description:** Fetches a list of all departments registered in the system.
- **Request Parameters:** None
- **Response:** Returns a JSON array of departments.

#### 5. Get All Users
- **Endpoint:** `/Users`
- **Method:** `GET`
- **Description:** Retrieves a list of all users in the system.
- **Request Parameters:** None
- **Response:** Returns a JSON array of users.

#### 6. Create a New User
- **Endpoint:** `/Users`
- **Method:** `POST`
- **Description:** Registers a new user in the system.
- **Request Parameters:** JSON object containing user details (e.g., name, email, user_code).
- **Response:** Returns a confirmation of the user creation with the user's details.

#### 7. Get Department by ID
- **Endpoint:** `/Departments/<int:id>`
- **Method:** `GET`
- **Description:** Fetches details of a specific department by its unique ID.
- **Request Parameters:** `id` - The unique identifier of the department.
- **Response:** Returns a JSON object of the department's details.

#### 8. Get User by ID
- **Endpoint:** `/Users/<id>`
- **Method:** `GET`
- **Description:** Retrieves details of a specific user by their unique ID.
- **Request Parameters:** `id` - The unique identifier of the user.
- **Response:** Returns a JSON object of the user's details.

#### 9. Create or Update a Complaint
- **Endpoint:** `/Complaints`
- **Method:** `POST`, `PUT`
- **Description:** Allows for the creation of a new complaint or updating an existing one. Use `POST` for creating and `PUT` for updating.
- **Request Parameters:** JSON object containing complaint details. For `PUT`, include the complaint ID to update.
- **Response:** Returns a confirmation of the complaint creation or update with the complaint's details.

### Notes:
- All `GET` requests might support query parameters for filtering, sorting, or pagination, which are not specified here.
- The `POST` and `PUT` methods expect requests to be made with a content type of `application/json` and the body of the request to contain a valid JSON object according to the endpoint's requirements.
- For the `POST` method on `/Users` and `/Complaints`, the server returns the created object with an assigned unique ID.
- Authentication and authorization mechanisms are not covered in this documentation but are essential for protecting sensitive endpoints and data.
  
## Software Used
- **App:** Flutter
- **Server:** Python
- **E-Portal:** React Typescript and React Admin

## Installation Instructions
### App
- Prerequisites: Install Flutter and Dart

### Server
- Prerequisites: Install Conda, Python, and Langchain

### E-portal
- Prerequisites: Install React Typescript, React Admin, Node.js, and npm

## Running the Application
### App
- Launch Simulator (iOS and Android) and run the application.

### E-Portal
- Execute `npm run dev` to start the E-Portal.

### Server
- For Windows: Use `start_samadhaan_server.bat` script.
- For Mac: Activate `conda` environment and run `samadhaan-server.py` and `grievance_enhancer.py`.

## Contributing
We welcome contributions! Please read our contributing guide to learn how you can help improve Samadhaan.

## License
MIT

