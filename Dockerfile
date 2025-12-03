FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirement.txt
EXPOSE 5000
CMD [ "python3","app.py" ]