FROM public.ecr.aws/lambda/python:3.9
WORKDIR /
COPY . .
RUN pip install flask
COPY . .
CMD ["python", "app.py"]
