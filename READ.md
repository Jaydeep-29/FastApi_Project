# Secure Password Generator and Bitcoin Price API

This project provides a RESTful API developed with FastAPI. It includes two main features:

1. A secure password generator that allows users to request new passwords based on specified criteria.
2. An integration with a third-party API to fetch the current price of Bitcoin in USD.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or newer
- pip

### Installing

First, clone the repository to your local machine:

```bash
git clone https://yourrepositorylink.git

Navigate into the project directory:
    cd Assignment_Fast_API

Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:
    pip install -r requirements.txt

Running the API
Start the FastAPI server with:
    uvicorn app.main:app --reload
    The API will be available at http://localhost:8000

Usage
Generate a Secure Password
To generate a password, send a POST request to /generate-password with the following JSON body:

json
Copy code
{
  "length": 12,
  "include_symbols": true,
  "include_numbers": true,
  "include_lowercase": true,
  "include_uppercase": true
}

Get Bitcoin Price
To fetch the current price of Bitcoin in USD, send a GET request to /bitcoin-price.

This can also be tested with curl, Postman, or directly from the Swagger UI.

Notes:

1. Make sure to replace `https://yourrepositorylink.git` with the actual URL of your GitHub repository and adjust any paths or commands according to your project's structure.
```
