# APIRestFlask - NExT Ford

## Desenvolvimento uma API com Flask em Python para cadastro de Pratos em um Restaurante delivery

---
<h3 align="center">
  Challenge: API REST RestauranteNEXT
</h3>
<br>
<p align="center">

  <a href="https://allmach.github.io/">
    <img alt="Made by Allan" src="https://img.shields.io/badge/made%20by-AllanASM-blueviolet">
  </a>

  <img alt="License" src="https://img.shields.io/github/license/GersonRS/Challenge-React-Native?color=blueviolet&logo=asa&logoColor=blue">

## :rocket: Sobre o desafio

Nesse desafio, foi desenvolvido uma API REST, que atende a um Restaurante. Foram aplicados conhecimentos aprendidos no modulo de Back-End do NExT com Python e Flask, para criar uma pequena API para cadastro de pratos de comida.

Essa API receberá requisições de um aplicativo movel, e retornará os pratos de comida cadastrados na API e permitirá a criação, edição e deleção de novos pedidos.

## Configuração do Projeto

Python 3.10.1, Flask, pip para gerenciamento de dependências, SQLite e MySQL Database para banco de dados.

Antes de tudo, neste projeto não defini os requisitos do sistema, ficou ao cargo dos meus pensamentos para praticar as funcionalidades.

Ao se ter a base de dados, foi criada uma aplicação Flask e as suas rotas, onde retornaram seus devidos dados:

## Funcionalidades da API

Agora que você já está com o template instalado e pronto para continuar, você deve verificar os arquivos da pasta e completar o código para atingir os objetivos do projeto.

- **`Listar os pratos de comida da API`**: API é capaz de retornar uma listagem de pratos de comidas cadastrados na API.

- **`Cadastrar um prato de comida na API`**: API é capaz de cadastrar um novo produto.

- **`Buscar pratos de comida ou categorias por id ou com filtros personalizados`**: A API é capaz de fazer uma busca na API de acordo com o parametro enviado na sua requisição.

- **`Listar os pedidos da sua API`**: Sua API deve ser capaz de retornar uma listagem, com as informações dos produtos pedidos, de todos os pedidos que estão cadastrados na sua API.

### Rtas da API:
  
  - **Rota `/login`**: Realiza o login de usuários cadastrados na API

  - **Rota `/new`**: Realiza o cadastro de novos produtos na API

  - **Rota `/edit/:id`**: Edita um produto cadastrado na API baseado no `id`

  - **Rota `/delete`**: Deleta produtos cadastrados que foram cadastrados na API

Para executar esse servidor foi necessário configurar as variáveis do flask(FLASK_APP e FLASK_ENV) e executar o seguinte comando:

```
  flask run
```

## :rocket: Expandindo os horizontes

Essa é uma aplicação totalmente escalável, isso significa que além das específicações, após finalizado o desafio, é totalmente possível implementar mais funcionalidades a essa aplicação, e essa será uma ótima maneira para fixar os conhecimentos.

Você pode implementar desde funcionalidades simples que não foram específicadas nos testes, como a finalização completa de um pedido, ou uma página que irá mostrar dados do pedido realizado.

## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
