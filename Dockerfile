FROM python:3.9-slim

# Check if /app directory exists, if not create it
WORKDIR /app

COPY requirements.txt /app
COPY model /app
COPY ./main.py /app

EXPOSE 3000

RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--host", "0.0.0", "--port", "3000"]