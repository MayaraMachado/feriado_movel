## Verifica Feriado

Uma api para calcular feriados móveis de acordo com um ano recebido na requisição. Essa é uma API desenvolvida para teste da integração Django + Travis CI + Heroku.

##### Executar

1. Clone o repositório
2. Execute no shell

```sh
$ make run
```
A aplicação estará rodando na porta 8000

##### Rota

- GET: localhost:8000/carnaval/<<int:ano>>