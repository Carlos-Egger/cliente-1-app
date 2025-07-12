# cliente-1-app

API Flask com SQLite desenvolvida como parte de um desafio técnico sobre integração de pipelines centralizadas com GitHub Actions.

## 🔧 Descrição

Esta aplicação fornece uma rota `/livros` que retorna uma lista de livros armazenada em um banco SQLite local.

Os testes automatizados usam `pytest` e verificam o funcionamento da API.

## ⚙️ Pipelines

Este repositório utiliza templates centralizados a partir de [`empresa-pipelines`](https://github.com/sua-org/empresa-pipelines), via `workflow_call`:

- `pipeline_testes_empresa.yml`: executa os testes automatizados.
- `pipeline_build_empresa.yml`: constrói e publica a imagem Docker da aplicação.

