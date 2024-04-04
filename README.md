# Squad 24

## Instalação e Execução

1. Instale o <a href="https://git-scm.com/downloads" target="_blank">Git</a>

2. Clone o repositório em sua máquina local:</br>
    `git clone https://github.com/Quantum-educ/residenciaII-01.2024-squad24`

3. Acesse a pasta do projeto: `cd residenciaII-01.2024-squad24`

4. Instale o <a href="https://www.python.org/downloads/" target="_blank">Python</a>

5. Crie um ambiente virtual Python: `python -m venv venv`
    > obs: o comando "python" pode mudar a depender de como foi instalado, se "python" nao funcionar tente "py" ou "python3".

6. Ative o ambiente virtual:
    | Sistema operacional | Comando |
    | ------------- | ------------- |
    | Linux | `source venv/bin/activate` |
    | Windows | `venv/Scripts/activate` |

7. Instale as dependências do projeto:<br>
    `pip install -r requirements.txt`

8. Realize as migrações do banco de dados:<br>
    `python escola_ez/manage.py makemigrations home --empty`<br>
    `python escola_ez/manage.py makemigrations users --empty`<br>
    `python escola_ez/manage.py makemigrations`<br>
    `python escola_ez/manage.py migrate`

9. Crie um super usuário:<br>
    `python escola_ez/manage.py createsuperuser`
    > obs: você será solicitado a inserir um nome de usuário, email e senha.

10. Execute o aplicativo:<br>
    `python escola_ez/manage.py runserver`

11. Acesse o localhost do aplicativo:
    <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>

<!-- ## Primeiros Passos
 1. Instale o <a href="https://git-scm.com/downloads" target="_blank">GIT</a>
 
 2. Clone o repositório em sua máquina local: 
 </br>`$ git clone 'https://github.com/Quantum-educ/residenciaII-01.2024-squad24'`
 </br></br>logo após isso, entre no projeto clonado:
 </br>`$ cd residenciaII-01.2024-squad24`

 3. Instale o <a href="https://www.python.org/downloads/" target="_blank">Python</a>

 4. Crie um ambiente virtual Python: `$ python -m venv NOME_DO_AMBIENTE`
     > obs: o comando "python" pode mudar a depender de como foi instalado, se "python" nao funcionar tente "py" ou "python3"

 5. Entre no ambiente virtual: </br>
    | Sistema operacional  | Comando |
    | ------------- | ------------- |
    | Linux  | `$ . NOME_DO_AMBIENTE/bin/activate` |
    | Windows  | `$ .\NOME_DO_AMBIENTE\Scripts\activate`  |
 
 6. Instale o django no ambiente virtual: `$ pip install Django`

 7. Crie uma aplicação Django: `$ django-admin startproject NOME_DO_PROJETO`

 8. Entre no projeto: `$ cd NOME_DO_PROJETO`

 9. Rode o projeto: `$ python manage.py runserver`
 
 10. Verifique que na sua porta 8000 estará rodando o Django, basta acessar: <a href="http://localhost:8000" target="_blank">http://localhost:8000</a> -->

## Documentação Inicial

Este é um trecho do nosso diagrama de classes UML.

![Diagrama](https://i.postimg.cc/25mKQwbW/Captura-de-tela-de-2024-03-25-16-37-33.png)

> ainda incompleto, onde a tabela de "perfil" será preenchida

</br>

Aqui está um exemplo de model:

```{.python}
from django.db import models


class ModelDeExemplo(models.Model):
  """
 Documentação do Model...
  
  
 Atributos
 ----------
 Guarda um valor para um campo:: 

   campo_teste: tipo
  

 Métodos
 -------
 Aqui uma breve descrição do metodo::

   metodo(parametros): str
  ...
  """
  
  campo_teste = models.TipoDoCampo(
   ...
  )
  
  # Outros campos...
  
 
  def metodo(argumentos: tipo) -> tipo:
    ...
   

  # Outros métodos...
  
```

![Codigo](https://i.postimg.cc/cLCwXfmr/carbon.png)
