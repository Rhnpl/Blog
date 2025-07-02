
# Blog Coxinhas - Projeto Base em Flask

Este é um projeto simples de blog feito em Flask com SQLite, onde você pode criar usuários, fazer login e criar, editar e deletar posts (matérias).  

> **Atenção:**  
> Este projeto é uma base para aprendizado e ainda está em desenvolvimento.  
> Não é seguro para uso em produção, pois não possui práticas adequadas de segurança (ex: senhas armazenadas em texto plano).  
> Se você quiser criar outro usuario tera alterar as propriedas manualmente, mas isso será melhorado.
> Estou aprendendo Flask e desenvolvimento web, e este projeto serve para estudo e prática.

---

## Usuário para Login

Para acessar o sistema e usar as funcionalidades protegidas, utilize o seguinte usuário:
Acessando `http://127.0.0.1:5000/login`

- **Usuário:** `Rhnpl`  
- **Senha:** `123456`

Somente com esse usuário você conseguirá fazer login e criar posts.

---

## Como instalar e rodar o projeto

### 1. Clone o repositório

```bash
git clone git@github.com:Rhnpl/Blog.git
cd Blog
```

### 2. Crie e ative um ambiente virtual (recomendado)

```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux / Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto

```bash
python run.py
```

O servidor vai iniciar em `http://127.0.0.1:5000`. Acesse pelo navegador.

---

## Arquivo requirements.txt

O arquivo `requirements.txt` contém as dependências básicas para rodar o projeto:

```
Flask==2.3.2
Flask-SQLAlchemy==3.0.3
```

---

## Sobre o projeto

- Banco de dados SQLite local (`dados.db`)
- Usuários podem se cadastrar e fazer login (com as limitações mencionadas)
- Criar, editar, visualizar e deletar matérias/posts
- Uso de sessões para controle básico de login
- Projeto com foco em aprendizado e aprimoramento em Flask e banco de dados

---

## Próximos passos

- Implementar hash de senha para segurança
- Validar formulários para evitar dados inválidos
- Melhorar controle de sessão e autenticação
- Adicionar controle de permissões por usuário

---

Se quiser ajuda para continuar melhorando, me avise!

---

**Autor:** Rhaniel Henrique  
**Data:** Julho de 2025
