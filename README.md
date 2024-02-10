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
(Include a concise list of endpoints with brief descriptions, methods, and response formats.)

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

