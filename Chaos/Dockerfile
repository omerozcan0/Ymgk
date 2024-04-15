# Base image olarak Python 3.12 alınacak
FROM python:3.12

# Uygulama kodunu /app klasörüne kopyala
COPY . /app

# Çalışma dizinini /app olarak ayarla
WORKDIR /app

# Gerekli Python paketlerini yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı çalıştır
CMD ["python", "app.py"]
