# Fibobank
## Django x Docker x AWS
Criamos uma simulação de um Banco. Com nginx, uma aplicação Django, duas aplicações Django Rest API, uma para o usuário fazer seu login e salvar os dados do seu usuário, outra para o usuário com seus dados entrar com na sua conta.

Utilizamos a arquitetura de microseviços, conforme a imagem:

![Imagem da aplicação](https://i.imgur.com/4IxyYV0.png)

Como pode ser visto, essa aplicação está sendo hospedada num EC2 da AWS, onde pode ser acessada caso esteja rodando pelo link: [Fibobank](https://www.google.com "Fibobank")

Mas em caso de não conseguir acessar a aplicação pela AWS segue instruções de como usar instalar localmente.
***
## Instalar
Nesta seção explicaremos como subir a aplicação pelo localhost.

Baixe o repositório, o Docker, e entre na pasta raíz dele pelo seu terminal.

### Docker
Primeiramente, você precisará buildar os containers.

Para buildar, use esse comando na pasta do microservice-WEB2:

- **docker-compose up --build**

Aplicação demora cerca de uns 2 minutos para subir, depois de buildado.

### Acessar

Após buildado e rodando, você pode abrir seu navegador e acessar o endereço localhost na porta 80.
[localhost](http://ec2-3-238-121-62.compute-1.amazonaws.com "Fibobank localhost")

***
## Estudantes
- Alex Emanuel
- Gabriel Lima
- William Teles
