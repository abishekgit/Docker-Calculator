# Docker Calculator

Docker Calculator is a simple calculator application built using Python and Docker. It allows you to perform basic arithmetic operations such as addition, subtraction, multiplication, and division from the command line.

## Requirements

To use Docker Calculator, you will need the following software installed on your machine:

- Docker
- Python 3.9

## Installation

To install Docker Calculator, follow these steps:

1. Clone this repository to your local machine using the following command:

git clone https://github.com/abishekgit/Docker-Calculator.git


2. Change into the project directory:

cd Docker-Calculator


3. Build the Docker image using the following command:

docker build -t calculator .


This will create a Docker image named "calculator" based on the Python 3.9-slim-buster base image.

## Usage

To use Docker Calculator, run the Docker container using the following command:

docker run -it calculator <operation> <operand1> <operand2>


Replace `<operation>` with the arithmetic operation you want to perform (add, subtract, multiply, or divide), `<operand1>` with the first operand, and `<operand2>` with the second operand.

For example, to add two numbers, you can use the following command:

docker run -it calculator add 2 3



This will output the result of the addition operation, which in this case is 5.

## License

Docker Calculator is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

If you would like to contribute to Docker Calculator, feel free to submit a pull request or open an issue. We welcome contributions from the community!
