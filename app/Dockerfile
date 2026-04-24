<<<<<<< HEAD
FROM python:3.9-slim
=======
FROM python:3.11-slim
>>>>>>> 20f47ac8daf4167191000a3c53c558969a38e227

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
COPY app.py .

EXPOSE 8000

CMD ["python", "app.py"]
=======
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> 20f47ac8daf4167191000a3c53c558969a38e227
