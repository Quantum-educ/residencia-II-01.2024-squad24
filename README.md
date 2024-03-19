# Squad 24
## Primeiros passos
 1. Instale o <a href="https://git-scm.com/downloads" target="_blank">GIT</a>
 
 2. Clone o repositório em sua máquina local: 
 </br>`$ git clone 'https://github.com/Quantum-educ/residenciaII-01.2024-squad24'`

 3. Instale o <a href="https://www.python.org/downloads/" target="_blank">Python</a>

 4. Crie um ambiente virtual python: `$ python -m venv NOME_DO_AMBIENTE`
 > obs: o comando "python" pode mudar a depender de como foi instalado, se "python" nao funcionar tente "py" ou "python3"

 5. Entre no ambiente virtual: </br>
| Sistema operacional  | Comando |
| ------------- | ------------- |
| Linux  | `$ . NOME_DO_AMBIENTE/bin/activate` |
| Windows  | `$ .\NOME_DO_AMBIENTE\Scripts\activate`  |
 
 6. Instale o django no ambiente virtual: `$ pip install Django`

 7. Crie uma aplicacao django: `$ django-admin startproject NOME_DO_PROJETO`

 8. Entre no projeto: `$ cd NOME_DO_PROJETO`

 9. Rode o projeto: `$ python manage.py runserver`
 
 10. Verifique que na sua porta 8000 estará rodando o django, basta acessar: <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>
 
