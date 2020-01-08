# Instalação

## Criando e Ativando Virtualenv
```
virtualenv -p python3 env
source env/bin/activate
```

## Instalando dependências
```
pip install -r requirements.txt
python contrib/enc-gen.py
```

## Executando
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```