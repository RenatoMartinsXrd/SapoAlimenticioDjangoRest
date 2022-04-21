# SapoAlimenticioDjangoRest

<p>Api desenvolvida para fornecer dados para SapoAlimenticioReact</p>

## 🎲 Rodando o Back End

### Clone este repositório
git clone https://github.com/RenatoMartinsXrd/SapoAlimenticioDjangoRest/
cd SapoAlimenticioDjangoRest

### Crie seu ambiente virtual ( opcional )
#### Linux
```apt-get install python3-venv```

```python3 -m venv venv```

```source venv/bin/activate```

#### Windows
```pip install virtualenv```

```virtualenv nome_da_virtualenv```

```nome_da_virtualenv/Scripts/Activate```

### Instale as bibliotecas necessárias
```pip install -r requirements.txt```

### Execute as migrations
```python3 manage.py makemigrations```
```python3 manage.py migrate```

### Execute localmente
```python3 manage.py runserver```

## 🎲 Endpoints
http://127.0.0.1:8000/alimentacao
http://127.0.0.1:8000/importAlimentacao

## 🎲 Algumas considerações
A api foi desenvolvida permitindo qualquer host fazer a solicitação http como se fosse uma api publica
