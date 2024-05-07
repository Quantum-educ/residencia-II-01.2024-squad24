FROM python:3.12

RUN apt-get update
RUN apt-get install -y libmariadb-dev-compat python3 python3-pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x ./release.sh
CMD ["./release.sh"]