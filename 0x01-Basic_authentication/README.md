# Basic Authentication Project

## Background Context
In this project, you will learn what the authentication process means and implement Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that does it for you (like in Python-Flask: Flask-HTTPAuth). Here, for learning purposes, we will walk through each step of this mechanism to understand it by doing.

## Resources
Read or watch:
- [REST API Authentication Mechanisms](https://www.restapitutorial.com/lessons/authentication.html)
- [Base64 in Python](https://docs.python.org/3/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://flask.palletsprojects.com/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Requirements

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Project Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Mochatr/alx-backend-user-data.git
    cd 0x01-Basic_authentication
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application:
```bash
./app.py