FROM python:3

WORKDIR /code

COPY ./requiriments.txt /code / requiriments.txt

RUN pip install --no-cache-dir --upgrade -r /code/requiriments.txt

EXPOSE 80
COPY . .
CMD ["fastapi", "run", "main.py", "--port", "80"]