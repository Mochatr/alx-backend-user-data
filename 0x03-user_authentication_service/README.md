# User Authentication Service

This project is a step-by-step implementation of an authentication system in a Flask application. The goal is to understand the mechanism by building it from scratch, rather than using existing modules or frameworks like Flask-User.

## Ressources
[Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
[Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
[HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## Learning Objectives

By the end of this project, you should be able to:

- Declare API routes in a Flask app.
- Get and set cookies.
- Retrieve request form data.
- Return various HTTP status codes.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Python version: `python3` (version 3.7)
- Code style: `pycodestyle` (version 2.5)
- ORM: `SQLAlchemy` (version 1.3.x)
- Install `bcrypt`: `pip3 install bcrypt`

### Additional Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- Your code should be executable.
- The length of your files will be tested using `wc`.
- All modules should have documentation.
- All classes should have documentation.
- All functions (inside and outside a class) should have documentation.
- Documentation should be a real sentence explaining the purpose of the module, class, or method.
- All functions should be type annotated.
- The Flask app should only interact with `Auth` and never with `DB` directly.
- Only public methods of `Auth` and `DB` should be used outside these classes.

## Setup

To set up the project, you will need to install `bcrypt`:

```sh
pip3 install bcrypt
