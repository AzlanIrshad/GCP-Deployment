FROM python:3.11-slim-buster
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
CMD [ "python", "app.py" ]
