# online_store_analysis

This project is designed to analyze customer orders from an online store. It provides functions to compute revenue by month, by product, and by customer, as well as identify the top customers based on revenue.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)
- [Docker Setup](#docker-setup)

## Project Overview

The project includes a Python script (`main.py`) that reads customer order data from a CSV file and computes various revenue metrics. The results are printed to the console.

## Project Structure

online_store_analysis/
│
├── main.py
├── orders.csv
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── tests/
└── test_main.py

- `main.py`: Contains the main logic for reading data and computing revenue metrics.
- `orders.csv`: Sample dataset of customer orders.
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Docker configuration for the application.
- `docker-compose.yml`: Docker Compose configuration for the application.
- `tests/test_main.py`: Unit tests for the functions in `main.py`.

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- Git
- Docker (optional, for Docker setup)

### Cloning the Repository


git clone https://github.com/ShashankByalla/online_store_analysis.git
cd online_store_analysis

Installing Dependencies

Create a virtual environment and install dependencies:
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
pip install -r requirements.txt

### Usage

Run the main script to compute and print revenue metrics:
python main.py

### Testing

Run the unit tests using pytest:
pytest

### Docker Setup

## Build and run the application using Docker:
docker build -t online_store_analysis .
docker run -it --rm --name online_store_analysis online_store_analysis

## Alternatively, you can use Docker Compose:
docker-compose up --build app
The output of the docker-compose up --build app command contains the result of running the application, including revenue metrics computed from the dataset.

## Running Tests with Docker Compose
To run the tests within the Docker environment, use the following command:
docker-compose run app pytest
The output file will contain the results of these tests, detailing which tests passed or failed.

### Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes.
