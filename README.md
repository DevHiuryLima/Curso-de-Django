# Curso-de-Django


<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/DevHiuryLima/Curso-de-Django?color=6666FF">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/DevHiuryLima/Curso-de-Django?color=6666FF">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/DevHiuryLima/Curso-de-Django?color=6666FF">

  <img alt="Github issues" src="https://img.shields.io/github/issues/DevHiuryLima/Curso-de-Django?color=6666FF" />

  <img alt="Github forks" src="https://img.shields.io/github/forks/DevHiuryLima/Curso-de-Django?color=6666FF" />

  <img alt="Github stars" src="https://img.shields.io/github/stars/DevHiuryLima/Curso-de-Django?color=6666FF" />
</p>

&#xa0;

## 📖 Sobre
Este é um projeto To Do foi feito durante o curso de Django do canal <a href="https://www.youtube.com/c/MatheusBattisti" target="_blank">Matheus Battisti - Hora de Codar</a>. O objetivo do curso é que através deste projeto os alunos aprendam os conceito do Django.

&#xa0;

## :computer: Tecnologias

#### **Web** 
  - **[Django][django]**
  - **[Python 3][python]**
 
  \* Veja o arquivo <kbd>[requirements.txt](https://github.com/DevHiuryLima/Curso-de-Django/blob/main/requirements.txt)</kbd>
  
#### **Server** 
  
  - **[SQLite][sqlite3]**
  
#### **Utilitários**

  - IDE: **[PyCharm][pycharm]**
  - Ícones: **[Markdown Emoji][markdown_emoji]**

&#xa0;

## 🎨 Layout

Essas são as telas do sistema Web.
<div align="center">
    <img src="https://user-images.githubusercontent.com/69491885/221944038-4761ceea-8c66-4640-b87d-1e724da547dd.png" width="500px" height="280px" title="Tela de login." alt="Tela de login.">
    <img src="https://user-images.githubusercontent.com/69491885/221946448-87b602f4-a3ef-4779-bfa1-5edf885217d6.png" width="500px" height="280px" title="Tela de registro de usuário." alt="Tela de registro de usuário.">
    <img src="https://user-images.githubusercontent.com/69491885/221947638-110e1f19-0d09-44c4-a554-bec73075b2c5.png" width="500px" height="280px" title="Tela de listagem de tarefas juntamente com uma dashboard." alt="Tela de listagem de tarefas juntamente com uma dashboard.">
    <img src="https://user-images.githubusercontent.com/69491885/221948445-181da8d4-f329-4ce4-acba-c3d53dd19778.png" width="500px" height="280px" title="Tela de criação de um usuário." alt="Tela de criação de um usuário.">
    <img src="https://user-images.githubusercontent.com/69491885/221948761-2319277e-3fe9-4f7a-9c0c-4bf52fd42d60.png" width="500px" height="280px" title="Tela de edição de um usuário." alt="Tela de edição de um usuário.">
</div>

&#xa0;

## 🚀 Como executar o projeto

#### Pré-requisitos
  - É **essencial** possuir o **[Python 3][python]** instalado na máquina.
  - É **nescessário** ter o `pipenv` instalado.

&#xa0;

1. Faça um clone :

```sh
  $ git clone https://github.com/DevHiuryLima/Curso-de-Django.git
```

&#xa0;

2. Instale as dependências:

  - **No Linux:**
```
  $ python -m venv venv
```

```
  $ source venv/Scripts/activate
``` 

```
  $ ./activate
```

  Volte a pasta `todo` e execute o comando:
```
  $ pip install -r requirements.txt
```

&#xa0;

  - **No windows**
```
  $ python -m venv venv
```

```
  $ cd venv\Scripts
```

```
  $ ./activate
```

  Volte a pasta `todo` e execute o comando:
```
  $ pip install -r requirements.txt
```

&#xa0;

  :warning: OBS: Somente se faltar o Django no arquivo `requirements.txt`, (dentro da pasta `todo`) execute o comando:
```
  $ pip install Django (Somente se faltar o Django no arquivo requirements.txt)
```

&#xa0;

3. Crie as migrations e execute-as:

```
  $ python manage.py makemigrations
```

```
  $ python manage.py migrate
```

&#xa0;

4. Crie um super user:

```
  $ python manage.py createsuperuser
```

&#xa0;

5. Execute a aplicação 

 Pelo terminal entre na pasta `todo` e execute o comando.
```
  $ python manage.py runserver
```

&#xa0;

## :octocat: Como contribuir

1. Faça um **fork** do projeto.
1. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
1. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
1. Envie as suas alterações: `git push origin my-feature`
> Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](https://github.com/firstcontributions/first-contributions)

&#xa0;

[Voltar para o topo](https://github.com/DevHiuryLima/Curso-de-Django#top)



<!-- Techs Web -->

[django]: https://www.djangoproject.com/
[python]: https://www.python.org/



<!-- Techs Server -->

[sqlite3]: https://github.com/mapbox/node-sqlite3



<!-- Techs Utilitárias -->

[pycharm]: https://www.jetbrains.com/pt-br/pycharm/
[markdown_emoji]: https://github.com/ikatyang/emoji-cheat-sheet
