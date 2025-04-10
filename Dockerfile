FROM python:3.9-slim
WORKDIR /
COPY . .
RUN pip install flask
COPY . .
CMD ["python", "app.py"]