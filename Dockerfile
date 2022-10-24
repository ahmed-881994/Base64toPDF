# start by pulling the python image
FROM python:3

# switch working directory
WORKDIR /

# copy the requirements file into the image
COPY ./requirements.txt /requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# copy every content from the local file to the image
COPY . /

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD ["app.py", "--port", "8000"]

# docker build -t base64topdf .
# docker run -it --rm --name base64topdf -p 8000:8000  base64topdf