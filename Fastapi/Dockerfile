FROM python:3.9


WORKDIR /todo


COPY . /todo/


RUN pip install --no-cache-dir --upgrade -r /todo/requirements.txt


CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
