# Imagine de bază Python
FROM python:3.10-slim

# Setăm directorul de lucru
WORKDIR /app

# Copiem fișierele proiectului în container
COPY . /app

# Instalăm pachetele necesare
RUN pip install --no-cache-dir -r requirements.txt

# Expunem portul pe care rulează aplicația
EXPOSE 5000

# Comanda pentru a rula aplicația
CMD ["python3", "run.py"]
