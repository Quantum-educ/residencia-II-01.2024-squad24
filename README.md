# Squad 24
## Primeiros passos
 1. Instale o <a href="https://git-scm.com/downloads" target="_blank">GIT</a>
 
 2. Clone o repositório em sua máquina local: 
 </br>`$ git clone 'https://github.com/Quantum-educ/residenciaII-01.2024-squad24'`
 </br></br>logo após isso, entre no projeto clonado:
 </br>`$ cd residenciaII-01.2024-squad24`

 4. Instale o <a href="https://www.python.org/downloads/" target="_blank">Python</a>

 5. Crie um ambiente virtual python: `$ python -m venv NOME_DO_AMBIENTE`
     > obs: o comando "python" pode mudar a depender de como foi instalado, se "python" nao funcionar tente "py" ou "python3"

 6. Entre no ambiente virtual: </br>
    | Sistema operacional  | Comando |
    | ------------- | ------------- |
    | Linux  | `$ . NOME_DO_AMBIENTE/bin/activate` |
    | Windows  | `$ .\NOME_DO_AMBIENTE\Scripts\activate`  |
 
 7. Instale o django no ambiente virtual: `$ pip install Django`

 8. Crie uma aplicacao django: `$ django-admin startproject NOME_DO_PROJETO`

 9. Entre no projeto: `$ cd NOME_DO_PROJETO`

 10. Rode o projeto: `$ python manage.py runserver`
 
 11. Verifique que na sua porta 8000 estará rodando o django, basta acessar: <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>
 
