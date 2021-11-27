FROM python:3.7.2

WORKDIR /api

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]