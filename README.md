# Customer Accounts Microservice

[![Build Status](https://github.com/YOUR_USERNAME/customer-accounts/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/YOUR_USERNAME/customer-accounts/actions/workflows/ci-build.yaml)

## Project Description

Customer Accounts is a RESTful microservice developed as part of the DevOps Capstone Project.

The application provides APIs to manage customer account information and demonstrates software development, testing, continuous integration, security, containerization, and Kubernetes deployment.

## Features

* Create a customer account
* Read a customer account
* List all customer accounts
* Update a customer account
* Delete a customer account
* RESTful API endpoints
* Automated unit testing
* Code linting and quality checks
* Continuous Integration using GitHub Actions
* Security headers and CORS policies
* Docker containerization
* Kubernetes deployment
* Continuous Delivery pipeline using Tekton

## Technologies Used

* Python
* Flask
* REST API
* SQLAlchemy
* PostgreSQL
* Nosetests
* Coverage
* Flake8
* Pylint
* GitHub Actions
* Docker
* Kubernetes
* Tekton

## REST API Operations

The service supports the following operations:

| Operation | HTTP Method | Description                         |
| --------- | ----------- | ----------------------------------- |
| Create    | POST        | Create a new customer account       |
| Read      | GET         | Retrieve a customer account         |
| List      | GET         | Retrieve all customer accounts      |
| Update    | PUT         | Update an existing customer account |
| Delete    | DELETE      | Delete a customer account           |

## Continuous Integration

GitHub Actions is configured to automatically:

1. Check out the source code.
2. Install project dependencies.
3. Run code linting.
4. Execute unit tests using nosetests.
5. Generate test coverage information.

## Security

The application implements security-related configurations including:

* Security headers using Talisman
* CORS policies
* Automated security and application tests

## Docker

The application is containerized using Docker.

The Docker image contains all required application dependencies and configuration required to run the Customer Accounts microservice.

## Kubernetes

The Dockerized application is deployed to Kubernetes using deployment and service resources.

The Kubernetes deployment provides:

* Application pods
* Replica sets
* Kubernetes service
* Containerized application execution

## Continuous Delivery

A Tekton-based Continuous Delivery pipeline is used to automate the deployment of the application to Kubernetes.

## Project Structure

```text
customer-accounts/
├── service/
├── tests/
├── .github/
│   └── workflows/
│       └── ci-build.yaml
├── Dockerfile
├── setup.cfg
├── requirements.txt
├── __init__.py
└── README.md
```

## Author

DevOps Capstone Project

## License

This project is developed for educational purposes as part of the DevOps Capstone course.
