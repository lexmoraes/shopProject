# Projeto Django para Exercício Prático 2 de Git

Este projeto é um sistema básico em Django que inclui funcionalidades CRUD para as entidades **Cliente**, **Produto** e **Venda**. Ele foi criado como um exercício prático para aprender e praticar o uso de Git.

## Requisitos

- Python 3.13
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado para isolamento do ambiente)

## Configuração do Ambiente

### 1. Clone o Repositório

Primeiro, clone o repositório para a sua máquina local:

git clone https://github.com/saviotom/shopProject.git
cd shopProject

### 2. Crie e Ative um Ambiente Virtual

python -m venv venv

venv\Scripts\activate

### 3. Instale as Dependências do Projeto

pip install django

### 4. Configure o Banco de Dados

python manage.py migrate

### 6. Inicie o Servidor

python manage.py runserver

Acesse o projeto no navegador em http://127.0.0.1:8000/

## Equipe:

1. [Alef Monteiro](https://github.com/alef-monteiro);
2. [Alexsandro Moraes](https://github.com/lexmoraes);
3. [Antônio Santos](https://github.com/antonio-pss);
4. [Ithauana Silva](https://github.com/Ithauana);

## Atribuições:

- Código ORD-001 (ALEX) - Adicione o nome da equipe no README.md, definindo o papel de
cada membro e implementar backend de funcionário (models, views, forms, urls).

- Código ORD-002 (ALEF) - Completar a implementação do backend de cadastro de produto (views, forms, urls).

- Código ORD-003 (ANTÔNIO) - Implementar a página de vendas (views, forms, urls, templates HTML).

- Código ORD-002 (ITHAUANA) - Implementar template de cadastro de funcionário e produto (templates HTML).
