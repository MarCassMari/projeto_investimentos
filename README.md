# Projeto Django

Bem-vindo ao projeto de Investimento! Este projeto é uma aplicação web desenvolvida utilizando o framework Django, com base nas aulas do curso: DevAprender

## Descrição

Este projeto tem como objetivo deixar as pessoas, que se cadastram na plataforma, fazer investimentos. O sistema inclui funcionalidades como o CRUD base - Editar, Excluir e Visualizar as informações internas dos investimentos.

## Estrutura do Projeto
- Cada aplicação/app criado dentro da base do projeto representa uma "ação" para facilitar manutenção e escalabilidade:

- `templates/`: Templates HTML do projeto.
- `manage.py`: Script de gerenciamento do Django.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd projeto_django
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
2. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
3. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:8000/
    ```
