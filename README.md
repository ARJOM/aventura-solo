# Aventura Solo

Esse projeto implementa o conceito de aventura solo a uma página web utilizando Django.

Jogue agora "O Guerreiro e o Dragão"


Para executar esse projeto siga os seguintes passos:

- Clone este repositório
```
git clone https://github.com/ARJOM/aventura-solo.git
```
- Crie um ambiente virtual
```
python3 -m venv venv
```
- Inicie o seu ambiente virtual executando:
```
source venv/bin/activate
```
- Atualize o pip
```
python -m pip install --upgrade pip
```
- Instale o Django
```
pip install -r requirements.txt
```
- Execute as migrações
```
python manage.py makemigrations solo
python manage.py migrate
```
- Carregue as fixtures para o banco
```
python manage.py loaddata solo/fixtures/aventura1.json
```
- Execute o projeto
```
python manage.py runserver
```
