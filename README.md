# Recette-web

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Relational-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](#)

**Recette** é um site de receitas simples, funcional e direto ao ponto. Ao contrário de muitos sites tradicionais (cheios de textos desnecessários e estética de blog), o Recette foca no que realmente importa: **as receitas**.

Conta com uma **IA integrada**, que gera receitas automaticamente com base nos ingredientes que o usuário tem em casa. E o mais legal: **qualquer usuário pode cadastrar, favoritar e avaliar receitas**.

## 🔍 Funcionalidades

- ✅ Cadastro e login de usuários com Django Allauth  
- ✅ CRUD de receitas  
- ✅ Geração de receitas com IA (via Groq API com Llama-3)  
- ✅ Sistema de favoritos  
- ✅ Avaliação de receitas com estrelas  
- ✅ Interface simples e limpa, sem aparência de blog  

## 🧠 Como funciona a IA?

- O usuário seleciona os ingredientes que tem.  
- A IA gera uma receita personalizada com base nesses ingredientes.  
- A receita é salva no banco de dados como se fosse criada por um usuário real.

## 🛠️ Tecnologias Utilizadas

- Python 3.12  
- Django  
- PostgreSQL  
- Tailwind CSS  
- Django Allauth  
- Groq API (Llama-3)

## 🚀 Como rodar localmente

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/recette.git
cd recette
```

2. Crie e ative o ambiente virtual:

```
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Crie um arquivo `.env` com suas credenciais e rode as migrações:

```
python manage.py migrate
```

5. Inicie o servidor:

```
python manage.py runserver
```

## 🎯 Objetivo

Criar uma plataforma simples, prática e acessível onde qualquer pessoa possa encontrar ou gerar receitas com base no que tem em casa, **evitando desperdícios e incentivando a criatividade na cozinha**. A IA é um apoio, mas o foco é a **comunidade** e a **usabilidade**.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

---

Feito com ❤️ por **Gabriel Sousa** e **Samuel Santos**
