## Como executar

### Pré-requisitos

Instale o newman para automatização de testes de API Rest

```bash
    npm install newman
    npm install newman-reporter-htmlextra
```

### Execução

Estando dentro da pasta "Lista API", execute o seguinte comando:

```bash
    newman run LISTA.postman_collection.json -e LISTA.postman_environment.json -r htmlextra
```
