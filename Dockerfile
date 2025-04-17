FROM python:3

WORKDIR /usr/src/app

COPY requiriments.txt ./

RUN pip install --no-cache-dir -r requiriments.txt


COPY . .

EXPOSE 80
CMD ["fastapi", "run", "main.py", "--port", "80"]

