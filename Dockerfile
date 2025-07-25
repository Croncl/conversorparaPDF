# Use uma imagem base Python
FROM python:3.12-slim

# Defina o diretório de trabalho
WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Copie requirements e instale dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . .

# Exponha a porta que a app usa
EXPOSE 5000

# Comando para rodar a app
CMD ["python", "app.py"]
