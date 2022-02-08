# Desafio Aula 16 - NExT-Ford

## Desenvolvimento uma API com Flask em Python para um restaurante delivery

---
<h3 align="center">
  Challenge: API REST RestauranteNEXT
</h3>
<br>
<p align="center">

  <a href="https://allmach.github.io/">
    <img alt="Made by Allan" src="https://img.shields.io/badge/made%20by-GersonRS-blueviolet">
  </a>

  <img alt="License" src="https://img.shields.io/github/license/GersonRS/Challenge-React-Native?color=blueviolet&logo=asa&logoColor=blue">

  <a href="https://github.com/GersonRS/Challenge-React-Native/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/GersonRS/Challenge-React-Native?style=social">
  </a>
</p>

## :rocket: Sobre o desafio

Nesse desafio, você irá desenvolver uma API REST, que atende a um Restaurante. Foram aplicados conhecimentos aprenddidos no modulo de Back-End do NExT com Python e Flask, para criar uma pequena API para cadastro de pratos de comida.

Essa API receberá requisições de um aplicativo movel, e retornará os pratos de comida cadastrados na API e permitirá a criação, edição e deleção de novos pedidos.

## Configuração do Projeto

Python 3.8.13, Flask, pip para gerenciamento de dependências, SQLite e MySQL Database para banco de dados.

Antes de tudo, neste projeto não definirei os requisitos do sistema, fica a cargo de cada um fazer o que acha conveniente.

Para que vocês tenham os dados para exibir em tela, vocês deverão criar alguns registros no seu banco de dados para te prover esses dados.

Ao se ter a base de dados, vocês deverão criar a aplicação Flask e as suas rotas, onde retornaram seus devidos dados:

## Funcionalidades da API

Agora que você já está com o template instalado e pronto para continuar, você deve verificar os arquivos da pasta e completar o código para atingir os objetivos do projeto.

- **`Listar os pratos de comida da sua API`**: Sua API deve ser capaz de retornar uma listagem, de uma parte de todos os pratos de comida que estão cadastrados na sua API.

- **`Cadastrar um prato de comida na sua API`**: Sua API deve ser capaz de cadastrar um novo produto na sua API.

- **`Listar as categorias da sua API`**: Sua API deve ser capaz de retornar uma listagem, de todas as categorias que estão cadastrados na sua API.

- **`Buscar pratos de comida ou categorias por id ou com filtros personalizados`**: Em sua API deverá ser capaz de fazer uma busca na API de acordo com o parametro enviado na sua requisição.

- **`Listar os pedidos da sua API`**: Sua API deve ser capaz de retornar uma listagem, com as informações dos produtos pedidos, de todos os pedidos que estão cadastrados na sua API.

**Dica**: Por se tratar de um desafio simples sem autenticação e de não possuir usuários, não será necessário cadastrar o campo `user_id`, considere que deve ser listados todos os pedidos da API como se fossem os seus pedidos.

- **`Listar os pratos favoritos da sua API`**: Sua API deve ser capaz de retornar uma listagem, com os campos e as informações dos produtos favoritados, de todos os favoritos que estão cadastrados na sua API.

**Dica**: Por se tratar de desafio simples sem autenticação e de não possuir usuários, não será necessário cadastrar o campo `user_id`, considere que deve ser listados todos os favoritos da API como se fossem os seus favoritos.

### Exemplo de rotas da API

  - **Rota `/produtos`**: Retorna todos os produtos cadastrados na API

  - **Rota `/produto/:id`**: Retorna um produto cadastrado na API baseado no `id`

  - **Rota `/categorias`**: Retorna todas as categorias cadastradas na API

  - **Rota `/pedidos`**: Retorna todas os pedidos que foram cadastrados na API

  - **Rota `/favoritos`**: Retorna todas as comidas favoritas que foram cadastrados na API

Para executar esse servidor você deve configuras as variaveis do flask(FLASK_APP e FLASK_ENV) e executar o seguinte comando:

```
  flask run
```

## :rocket: Expandindo os horizontes

Essa é uma aplicação totalmente escalável, isso significa que além das específicações, após finalizado o desafio, é totalmente possível implementar mais funcionalidades a essa aplicação, e essa será uma ótima maneira para fixar os conhecimentos.

Você pode implementar desde funcionalidades simples que não foram específicadas nos testes, como a finalização completa de um pedido, ou uma página que irá mostrar dados do pedido realizado.

Faça um post no Linkedin ou Instagram e postar o código do Github é uma boa forma de demonstrar seus conhecimentos e esforços para evoluir na sua carreira para oportunidades futuras.

Além disso, use sua criatividade para testar novas coisas, existem muitas possibilidades de aprendizado!

## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com 💜 by GersonRS