python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

python escola_ez/manage.py makemigrations home --empty
python escola_ez/manage.py makemigrations users --empty
python escola_ez/manage.py makemigrations
python escola_ez/manage.py migrate

echo -e "\nCriar super usuário:"
python escola_ez/manage.py createsuperuser

python escola_ez/manage.py runserver