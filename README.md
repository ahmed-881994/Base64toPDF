# Base64 to PDF converter
----------
This is a web based utility that accepts Base64 strings and converts them to PDF documents.

----
## Installing dependencies

To install dependencies please make sure you have Python installed and use

`pip install flask`

`pip install flask-cors`

to install **Flask** and all **Flask-CORS**

---
## Running the app using Uvicorn

navigate into the project directory and run

`python app.py -p 8000 `

this will spin up a dev server on port `8000` feel free to change the port

---
## Docker

To use the app in docker
1. run `docker build -t base64topdf .` to build the image
2. run `docker run -it --rm --name base64topdf -p 8000:8000  base64topdf` to start a container with the address `127.0.0.1:8000`
