FROM python:3.12

RUN apt-get update
RUN apt-get install -y libmariadb-dev-compat python3 python3-pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python escola_ez/manage.py makemigrations --noinput
RUN python escola_ez/manage.py migrate --noinput
RUN python escola_ez/manage.py collectstatic --noinput

CMD ["python", "escola_ez/manage.py", "runserver", "0.0.0.0:8000"]