# microservice-WEB2
## Django x Docker
Criamos uma simulação de um Banco. Com duas API's, uma para o usuário fazer seu login e receber um token, outra para o usuário entrar com o token na sua conta.

Imgem da arquitetura de microserviços que criamos e os passos:

![Imagem das APIs](https://i.imgur.com/OHxX1Z3.png)

***
## Instalar
Nesta seção explicaremos como preparar as API's.

### Docker
Primeitamente, precisamos buildar os containers e após fazer os migrations das API's Django para os Databases.

Para buildar, usamos esse comando:

- **docker-compose up --build**

Após ele abriremos outro terminal para acessar o shell dos containers das API's.

Primeiro acessaremos o container da API ***account-api***:

1. **docker exec -ti microservice-web2_account-api_1 bash**
    1. **python manage.py makemigrations**
    2. **python manage.py migrate**

Após rodar eles, podemos fechar esse terminal e abrir outro novamente, para acessar o segundo container, da API ***auth-api***:

1. **docker exec -ti microservice-web2_auth-api_1 bash**
    1. **python manage.py makemigrations**
    2. **python manage.py migrate**


### Inserir dados nos databases

Pronto, agora só precisamos inserir um usuário e uma conta nos Databases.

Basta entrar, nos arquivos: `authentication_service\authentication\models.py` e `account_service\account\models.py`, e inserir essas linhas de código, no final de cada arquivo respectivamente.

```
from django.contrib.auth.hashers import make_password
user = User(id=1, password=make_password("microservice"), username="William", is_active=False)
user.save()
```
```
account = Account(id=1, account_number="05846", balance=657, owner_id=1)
account.save()
```
***
## Usar as API's

Primeiramente, precisaremos ter o Postman ou Insomnia ou outro programa de sua preferencia para fazer requisições HTTP.

### auth-api
- Crie uma requisição post, com a url ``http://localhost/auth/login/`` e coloque no body o JSON:

```
{
	"username": "william",
	"password": "microservice"
}
```
- Caso tente enviar a requisição sem inserir *username* ou *password* no JSON, a resposta será um JSON: 
```
{
    "error_message": "Request must contain a username and password"
}
```

- Se você colocar dados que não estão cadastrados, você receberá um JSON: 
```
{
    "error_message": "Username and Password are invalid, User does not exists"
}
```

- A resposta será um JSON com dois tokens, **refresh** e **access**. O token para acessar a conta é o ***access***, o ***refresh*** é para renovar o de ***access***, porque ele tem uma duração de 5 minutos antes de expirar, e o ***refresh*** tem duração de 24h.

### account-api

- Agora com o token de access podemos acessar nossa conta, basta criar uma requisição get para a url ``http://localhost/account/``, sem JSON mas com Autenticação **Bearer Token**. Colocaremos o token de **access** e enviaremos a requisição.

- A resposta será um JSON com os dados da conta:
```
{
  "account_number": "05846",
  "balance": "657.0000000000",
  "owner_id": 1
}
```
***
## Planos futuros

Pretendemos no futuro melhorar esse projeto com a atividade CRUD, adicionando cadastro e outras funcionalidades.
***
## Estudantes
- Alex Emanuel
- Gabriel Lima
- William Teles
