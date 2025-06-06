# docker-fast-api

This project demonstrates how to containerize a FastAPI application using Docker. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. It is part of the [YouTube Docker Crash Course on my channel](https://youtu.be/s7fnNNV-CM4).

## Features

- FastAPI for building APIs
- Docker for containerization
- Simple and easy-to-understand project structure

## Requirements

- Python 3.9 or higher
- Docker

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/rishabkumar7/docker-fast-api.git
    cd docker-fast-api
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the FastAPI application locally without Docker.
```sh
fastapi dev app/main.py
```

## API Endpoints

`GET /`: Returns a welcome message.
`GET /items/{item_id}`: Returns the item details for the given item_id.


## Docker

To build and run the Docker container:

1. Build the Docker image:
``` sh
docker build -t docker-fast-api .
```

2. Run the Docker container:
``` sh
docker run -d -p 80:80 docker-fast-api
```

## Author

- Twitter: [@rishabincloud](https://x.com/rishabincloud)
- LinkedIn: [@rishabkumar7](https://linkedin.com/in/rishabkumar7)
