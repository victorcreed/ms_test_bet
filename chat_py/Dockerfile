FROM python:3.9-slim

ENV APP /usr/src/app
RUN mkdir $APP
WORKDIR $APP
COPY requirements.txt $APP/

RUN pip install -r requirements.txt
COPY . $APP/

CMD ["python", "app.py"]