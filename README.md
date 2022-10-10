# ToDoList CarFord

Este repositório foi criado para a apresentação de um case onde a ideia é desenvolver uma aplicação utilizando Flask e Docker, onde uma loja de carros chamada de CarFord pode gerenciar seus clientes e veículos.

Desenvolvi ela também utilizando o Framework Streamlit para desenvolver uma interface Front-end mais amigável.

O software também conta com uma **API** com todas as funcionalidades de um **CRUD**, além de autenticação **JWT** que pode ser testada com o *Postman* ou *Insomnia*, basta acessar o endpoint /api.

## Pré-requisitos

É necessário ter o **Docker** e **Docker Compose** instalados na máquina para que o sistema funcione corretamente.

Caso queira acompanhar a criação das tabelas no banco de dados, tenha um Client **SQL** como o *DBeaver* instalado na máquina.

## Instalação

Clone o **repositório** em sua máquina

```bash
git clone https://github.com/juniorcostin/Case-TodoList-CarFord.git
```
Navegue até o diretório criado

```bash
cd Case-TodoList-CarFord
```
Utilize o docker compose para realizar a instalação

```bash
docker compose up
```

Após isso aguarde até obter o retorno dos 3 **containers** no terminal:
**carford-postgresql**
**carford-web**
**carford-api**

Após receber o retorno dos 3 sua aplicação já está instalada!

## Uso do sistema

#### WEB:
Para utilizar o front-end da aplicação basta acessar em seu navegador **http://localhost**

Assim você será redirecionado para a tela inicial do sistema, não se assuste pois por padrão a ferramenta não trás nenhum dado, portanto as tabelas estarão vazias.

Basta navegar pelos menus para acessar as funcionalidades.

#### Importante:
Ao acessar as telas de funcionalidades, você perceberá que **não** haverá botão de **login** ao informar email e senha, não se preocupe basta apertar o Enter após informar a senha que será possível acessar.

Por padrão o sistema virá com um usuário admin.

email:
```bash
admin@admin.com
```
senha:
```bash
admin
```

Não se preocupe, após o primeiro uso você pode alterar a senha normalmente!

#### APIs:

Para utilizar as APIs basta você utilizar um client como o Postman e acessar os endpoints, por padrão eles estão nomeados como:

```bash
http://localhost:5000/api
```

Lembre-se que apenas usuários admins do sistema podem utilizar os endpoints de remoção e edição!

#### Endpoints:
#### Login:
Antes de realizar qualquer consulta você deve se logar, para isso é necessário utilizar a rota: **/login** informando um body:

```json
{
"email": "email do usuario cadastrado no sistema",
"senha": "senha do usuario cadastrado no sistema"
}
```
Após isso a **API** retornara um **JWT** que você utilizará para acessar todos os outros endpoints.
#### Usuários:
GET - lista todos os usuários
```json
/api/usuarios
```
GET - lista apenas um usuário
```json
/api/usuarios/<ID DO USUARIO>
```
POST - Cadastra um usuário
```json
/api/usuarios
```
```json
{
"nome": "Nome",
"email": "E-mail",
"senha": "Senha",
"admin": true ou false
}
```
PUT - Atualiza um usuário
```json
/api/usuarios/<ID DO USUARIO>
```
Os todos os parâmetros são opcionais
```json
{
"nome": "Nome",
"email": "E-mail",
"senha": "Senha",
"admin": true ou false
}
```
DELETE - Deleta um usuário
```json
/api/usuarios/<ID DO USUARIO>
```


#### Carros:
GET - lista todos os carros
```json
/api/carros
```
GET - lista apenas um carro
```json
/api/carros/<ID DO CARRO>
```
POST - Cadastra um carro
```json
/api/carros
```
```json
{
"modelo": "Modelo",
"cor": "Cor",
"id_proprietario": id
}
```
PUT - Atualiza um carro
```json
/api/carros/<ID DO CARRO>
```
Os todos os parâmetros são opcionais
```json
{
"modelo": "Modelo",
"Cor": "cor"
}
```
DELETE - Deleta um carro
```json
/api/carros/<ID DO CARRO>
```


#### Proprietários:
GET - lista todos os proprietários
```json
/api/proprietarios
```
GET - lista apenas um proprietário
```json
/api/proprietarios/<ID DO PROPRIETARIO>
```
POST - Cadastra um proprietário
```json
/api/proprietarios
```
```json
{
"nome": "Nome",
"email": "E-mail"
}
```
PUT - Atualiza um proprietário
```json
/api/proprietarios/<ID DO PROPRIETARIO>
```
Os todos os parâmetros são opcionais
```json
{
"nome": "Nome",
"email": "E-mail"
}
```
DELETE - Deleta um proprietário
```json
/api/proprietarios/<ID DO PROPRIETARIO>
```
