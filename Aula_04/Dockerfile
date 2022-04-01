
# estabelecendo a versão do python
FROM python:3.7-slim

#instala o flasck
RUN pip install flask

#copia o arquivo local para o container
COPY app.py /app.py

#executa o arquivo python
CMD ["python","app.py"]
