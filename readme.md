# Avaliação Técnica - Desenvolvedor de Sistemas | GNTech

API RESTful desenvolvida com FastAPI que consome dados meteorológicos da API pública **Meteomatics**, armazena em banco de dados **PostgreSQL**, e expõe os dados de forma remota. Toda a aplicação está conteinerizada utilizando **Docker** e organizada com boas práticas de código e versionamento com Git.


## 🧠 Visão Geral

- 🔄 Consulta de dados climáticos (temperatura máxima) por coordenadas
- 💾 Armazenamento das informações em banco relacional (PostgreSQL)
- 🌐 Disponibilização dos dados via API RESTful
- 📦 Conteinerização completa com Docker e Docker Compose
- 🧪 Documentação automática com Swagger e Redoc
- 🛠️ Organização modular com FastAPI, SQLAlchemy e Pydantic


## 🧱 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Meteomatics API](https://www.meteomatics.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)


## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone git@github.com:ThiagoCostaD/GN-Tech.git
cd seu-repositorio
```

### 2. Crie um arquivo .env

#### Baseie-se no modelo abaixo e salve como .env:

``` bash
METEOMATICS_USERNAME=seu_usuario_meteomatics
METEOMATICS_PASSWORD=sua_senha_meteomatics
METEOMATICS_BASE_URL=https://api.meteomatics.com
DATABASE_URL=postgresql://user:password@postgres_weather/weather_db
```

### 3. Suba os containers com Docker

```bash
docker-compose up --build -d
```

#### Ou de forma simplificada, com make:

```bash
make build
```

### 🛠️ Comandos Make Disponíveis

Para facilitar o uso com Docker, você pode utilizar os comandos abaixo com `make`:

| Comando         | Descrição                                               |
|-----------------|---------------------------------------------------------|
| `make build`    | Constrói os containers Docker                           |
| `make start`    | Inicia os containers da aplicação                       |
| `make stop`     | Para os containers da aplicação                         |
| `make restart`  | Reinicia os containers da aplicação                     |
| `make logs`     | Exibe os logs do container principal                    |
| `make shell`    | Abre um terminal dentro do container da aplicação       |
| `make db-shell` | Abre o terminal do PostgreSQL no container do banco     |

### 🔍 Acessando a API

- **Swagger UI:** [`http://localhost:8000/docs`](http://localhost:8000/docs)  
- **Redoc:** [`http://localhost:8000/redoc`](http://localhost:8000/redoc)


### 🛰️ Exemplo de Requisição

```bash
curl -X GET http://localhost:8000/weather/-27.59548/-48.5480
```

### 🔁 Retorno esperado

``` json
{
  "city": "-27.59548,-48.548",
  "temperature": 26.0,
  "weather": "Temperatura máxima: 26.0°C",
  "id": 1
}
```

### 🔗 Endpoints Disponíveis

| Método | Rota                                 | Descrição                                              |
|--------|--------------------------------------|--------------------------------------------------------|
| GET    | `/weather/{latitude}/{longitude}`    | Consulta e armazena a temperatura de uma localização  |


### 🗺️ Coordenadas Úteis para Teste

| Estado | Cidade              | Latitude   | Longitude  |
|--------|----------------------|------------|------------|
| SC     | Florianópolis        | -27.5954   | -48.5480   |
| SP     | São Paulo            | -23.5505   | -46.6333   |
| RJ     | Rio de Janeiro       | -22.9068   | -43.1729   |
| MG     | Belo Horizonte       | -19.9167   | -43.9345   |
| RS     | Porto Alegre         | -30.0346   | -51.2177   |
| BA     | Salvador             | -12.9714   | -38.5014   |
| PE     | Recife               | -8.0476    | -34.8770   |
| CE     | Fortaleza            | -3.7172    | -38.5433   |
| AM     | Manaus               | -3.1190    | -60.0217   |
| DF     | Brasília             | -15.7939   | -47.8828   |
| PR     | Curitiba             | -25.4284   | -49.2733   |

### 📜 Licença

Este projeto está sob a licença **MIT**.  
Sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo conforme necessário.


### 📫 Contato

Em caso de dúvidas ou sugestões, entre em contato:  
📧 **thiagoocdiniz@gmail.com**
