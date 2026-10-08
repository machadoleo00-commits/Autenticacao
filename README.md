# Autenticação

Projeto de estudo para aprender, na prática, os conceitos de autenticação e autorização em uma API REST. Construído com Python, Flask e SQLite.

> Projeto em desenvolvimento. Este README é atualizado a cada etapa concluída.

## Objetivo

Construir do zero uma API de usuários com registro, login e rotas protegidas, entendendo o que acontece por trás de cada etapa. Depois, aplicar o que foi aprendido em um projeto existente, o [lista-de-tarefas](https://github.com/machadoleo00-commits/lista-de-tarefas), para que cada usuário veja apenas as próprias tarefas.

## Conceitos estudados

- **Autenticação**: confirmar quem é a pessoa que está fazendo a requisição.
- **Autorização**: decidir o que essa pessoa pode ver ou alterar.
- **Hash de senhas**: por que nunca guardar a senha em texto puro.
- **Salt**: por que senhas iguais precisam gerar hashes diferentes.

## Roteiro

- [x] Conceitos: autenticação x autorização
- [x] Conceitos: senhas, hash e salt
- [ ] Rota de registro, gravando o usuário no SQLite
- [ ] Rota de login, conferindo a senha
- [ ] Tokens para identificar o usuário entre requisições
- [ ] Rotas protegidas
- [ ] Autorização: cada usuário acessa apenas os próprios dados
- [ ] Integração com o projeto lista-de-tarefas

## Como rodar

Ainda não há código executável. Quando houver, as instruções entram aqui.

Preparação do ambiente:

```bash
python -m venv venv
venv\Scripts\activate
pip install flask
```

## Requisitos

- Python 3
- `flask` (`pip install flask`), que já inclui o `werkzeug` usado para o hash das senhas

## Segurança

- Senhas nunca são guardadas em texto puro, apenas o hash com salt.
- Chaves secretas ficam em variáveis de ambiente (arquivo `.env`), que não é versionado.
- O banco de dados (`*.db`) não é versionado.
