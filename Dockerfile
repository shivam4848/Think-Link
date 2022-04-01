FROM python:3.8
LABEL maintainer="Shivam D Sahu<shivam4848@gmail.com>"
WORKDIR /code
COPY . .
RUN apt update && apt install -y apt-transport-https ca-certificates sqlite3
RUN python3 -m pip install -r requirements.txt
RUN python manage.py db upgrade
CMD make run