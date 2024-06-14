# Documentação da API de Cadastro de Produtos

## Sumário

1. [Introdução](#introdução)
2. [Requisitos](#requisitos)
3. [Instalação](#instalação)
4. [Configuração](#configuração)
5. [Endpoints](#endpoints)
    - [Autenticação](#autenticação)
    - [Usuários](#usuários)
    - [Produtos](#produtos)
6. [Tecnologias Utilizadas](#tecnologias-utilizadas)

## Introdução

Esta API foi desenvolvida com o objetivo de praticar a implementação de autenticação, uso de cache com Redis, interação assíncrona com MySQL e uso de async/await em Python. A API permite a criação, leitura, atualização e exclusão (CRUD) de produtos, além de suportar autenticação de usuários com criptografia de senha para segurança. A API foi construída utilizando FastAPI, MySQL Async, SQLAlchemy Core e Redis.

## Requisitos

- Python 3.8+
- MySQL
- Redis

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/hallan-n/pyshop.git
    cd pyshop
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1. Configure o banco de dados MySQL e Redis no arquivo `.env`:

    ```env
    DATABASE_URL=mysql+aiomysql://usuario:senha@localhost:3306/seubanco
    REDIS_URL=redis://localhost
    SECRET_KEY=sua_chave_secreta
    ```


## Endpoints

### Autenticação

#### Registro de Usuário

- **Endpoint:** `/auth/register`
- **Método:** `POST`
- **Descrição:** Registra um novo usuário.
- **Corpo da Requisição:**
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "message": "Usuário registrado com sucesso!"
    }
    ```

#### Login

- **Endpoint:** `/auth/login`
- **Método:** `POST`
- **Descrição:** Autentica um usuário e retorna um token JWT.
- **Corpo da Requisição:**
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "access_token": "string",
        "token_type": "bearer"
    }
    ```

### Usuários

#### Perfil do Usuário

- **Endpoint:** `/users/me`
- **Método:** `GET`
- **Descrição:** Retorna as informações do usuário autenticado.
- **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <token>
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "id": "integer",
        "username": "string"
    }
    ```

### Produtos

#### Listar Produtos

- **Endpoint:** `/products`
- **Método:** `GET`
- **Descrição:** Lista todos os produtos.
- **Resposta de Sucesso:**
    ```json
    [
        {
            "id": "integer",
            "name": "string",
            "description": "string",
            "price": "float"
        }
    ]
    ```

#### Criar Produto

- **Endpoint:** `/products`
- **Método:** `POST`
- **Descrição:** Cria um novo produto.
- **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <token>
    ```
- **Corpo da Requisição:**
    ```json
    {
        "name": "string",
        "description": "string",
        "price": "float"
    }
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "id": "integer",
        "name": "string",
        "description": "string",
        "price": "float"
    }
    ```

#### Atualizar Produto

- **Endpoint:** `/products/{id}`
- **Método:** `PUT`
- **Descrição:** Atualiza as informações de um produto existente.
- **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <token>
    ```
- **Corpo da Requisição:**
    ```json
    {
        "name": "string",
        "description": "string",
        "price": "float"
    }
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "id": "integer",
        "name": "string",
        "description": "string",
        "price": "float"
    }
    ```

#### Deletar Produto

- **Endpoint:** `/products/{id}`
- **Método:** `DELETE`
- **Descrição:** Deleta um produto.
- **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <token>
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "message": "Produto deletado com sucesso!"
    }
    ```

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework moderno, rápido (alta performance) e fácil de usar para construir APIs com Python baseado em padrões.
- **[MySQL Async](https://github.com/encode/databases):** Biblioteca para interação assíncrona com bancos de dados.
- **[SQLAlchemy Core](https://www.sqlalchemy.org/):** ORM (Object Relational Mapper) para mapeamento de objetos em bancos de dados relacionais.
- **[Redis](https://redis.io/):** Banco de dados em memória usado como cache.
- **Criptografia de senha:** Utilização de algoritmos seguros para armazenar senhas de usuários de forma segura.
