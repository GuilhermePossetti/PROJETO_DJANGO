# Projeto Django

Repositório de estudos práticos de Django, feito em paralelo com um curso de Python/Django. Aqui vou aplicando cada conceito novo diretamente num projeto próprio, ao invés de só seguir os exercícios do curso.

**Projeto em andamento** — está bem no início, e vai crescer conforme eu avançar no curso.

## Sobre o projeto

Dentro da pasta `blog_django`, estou construindo um blog simples, aplicando os fundamentos do Django: projeto, apps, views e URLs. A ideia é ir evoluindo esse mesmo projeto conforme novos conceitos forem aparecendo no curso (models, banco de dados, templates, etc.).

## O que já foi feito

- Criação do projeto Django (`django-admin startproject`)
- Criação de um app (`manage.py startapp`)
- Primeira view (function based view), usando `HttpRequest` e `HttpResponse`
- Conexão entre URL e view, usando `path()`

## Tecnologias utilizadas

- Python 3
- Django
- SQLite (banco padrão do Django, ainda não customizado)

## Como executar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/GuilhermePossetti/projeto_django.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd projeto_django/blog_django
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate
   ```
4. Instale o Django:
   ```bash
   pip install django
   ```
5. Rode o servidor:
   ```bash
   python manage.py runserver
   ```
6. Acesse `http://127.0.0.1:8000/pagina_inicial/` no navegador.

## Aprendizados

- Diferença entre projeto e app no Django
- Como uma view recebe uma `request` e devolve uma `response`
- Como conectar uma URL a uma função, usando `urlpatterns` e `path()`
- Organização de um projeto Django (settings, urls, apps)

## Próximos passos

- [ ] Criar um Model para os posts do blog
- [ ] Aprender migrações (`makemigrations` / `migrate`)
- [ ] Criar templates HTML para exibir os posts
- [ ] Formulário para criar novos posts

---

Desenvolvido por [Guilherme Possetti](https://github.com/GuilhermePossetti) 
como parte dos meus estudos em Python/Django.