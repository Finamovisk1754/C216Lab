<<<<<<< HEAD
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
=======
FROM python:3.11.1

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
>>>>>>> 34152862fc04255e2af29f6b53e70a9774cb9cf9
