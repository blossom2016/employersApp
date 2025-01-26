# CI/CD Pipeline Project

This is a preject that is a full-stack application with automated CI/CD pipeline using GitHub Actions and Docker.
carried out using GitHub Actions and Docker. The project consists of a frontend React application and a backend Flask application.

## Project Structure

## Features

- Frontend React application running on port 3000
- Backend Flask application running on port 5000
- Docker containerization for both services
- GitHub Actions for automated CI/CD
- Docker Hub integration for container registry
- Prometus for monitoring and alerting
- Grafana for monitoring and alerting

## Prerequisites

- Docker and Docker Compose
- Node.js
- Python
- GitHub account
- Docker Hub account

## Getting Started

1. Clone the repository:

git clone https://github.com/yourusername/cicdpipelineProject.git
cd cicdpipelineProject


2. Build and run the containers:

docker-compose up --build


3. Access the applications:
   - Frontend: http://localhost:3000
   - Backend: http://localhost:5000

## Development

### Frontend

The frontend is a React application located in the `nodeapp/frontend` directory.

To run the frontend locally:


cd nodeapp/frontend
npm install
npm start


### Backend

The backend is a Flask application located in the `backend` directory.

To run the backend locally:


cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python app.py


## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment. The workflow is defined in `.github/workflows/main.yml`.

The pipeline performs the following steps:
1. Builds the Docker images
2. Runs tests
3. Pushes the images to Docker Hub
4. Deploys the application (if applicable)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Ebube Williams - chidiebube.willie@gmail.com

Project Link: [https://github.com/blossom2016/cicdpipelineProject](https://github.com/blossom2016/cicdpipelineProject)
