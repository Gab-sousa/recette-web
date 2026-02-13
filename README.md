# Recette — Plataforma Web de Receitas com IA

---

Este é um projeto de uma plataforma web para geração e compartilhamento de receitas desenvolvido como Trabalho de Conclusão de Curso. O sistema utiliza inteligência artificial para criar receitas personalizadas com base nos ingredientes informados pelo usuário, além de permitir cadastro colaborativo, favoritos e avaliações. O foco do projeto é ajudar pessoas a decidir o que cozinhar com o que já possuem e reduzir o desperdício de alimentos.

---

## Funcionalidades

- **Geração de Receitas com IA**: Criação automática de receitas a partir dos ingredientes selecionados.
- **Cadastro de Receitas**: Usuários podem criar e publicar receitas próprias.
- **Sistema Colaborativo**: Compartilhamento de receitas entre usuários.
- **Favoritos**: Permite salvar receitas preferidas.
- **Avaliações**: Usuários podem avaliar receitas.
- **Perfil de Usuário**: Área com dados e estatísticas de uso.
- **Upload de Imagens**: Cadastro de imagens das receitas.
- **Busca e Filtro**: Pesquisa de receitas por nome e ingredientes.

---

## Tecnologias Utilizadas

- **Backend**: Django
- **Autenticação**: Django Allauth
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **IA**: Groq API com modelo Llama
- **Banco de Dados (desenvolvimento)**: SQLite
- **Banco de Dados (produção)**: PostgreSQL via Supabase
- **Túnel de teste externo**: Ngrok

---

## Banco de Dados

O projeto utiliza SQLite durante o desenvolvimento local e PostgreSQL hospedado no Supabase para ambiente de produção.  
A conexão é feita via variável de ambiente utilizando dj-database-url.

---

## Requisitos

- Python 3.11+
- pip
- Git
- Conta no Supabase
- Chave de API Groq

---

## Instalação

Clone o repositório:

```
git clone https://github.com/Gab-sousa/recette-web
cd recette-web
```

Crie o ambiente virtual:

```
python -m venv .venv
```

Ative o ambiente virtual:

Windows:

```
.venv\Scripts\activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```
SECRET_KEY=sua_secret_key
DEBUG=True
DATABASE_URL=sua_string_postgresql_supabase
GROQ_API_KEY=sua_chave_api
SUPABASE_URL=sua_url
SUPABASE_KEY=sua_key
```

---

## Migrações

```
python manage.py migrate
```

Criar superusuário:

```
python manage.py createsuperuser
```

---

## Execução

```
python manage.py runserver
```

---

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch: `git checkout -b minha-branch`.
3. Faça commit das alterações: `git commit -m 'Minha contribuição'`.
4. Envie para o repositório remoto: `git push origin minha-branch`.
5. Abra um Pull Request.

---

## Licença

Projeto desenvolvido para fins acadêmicos (TCC). Uso livre para estudo e adaptação.
