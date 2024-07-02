
# MVP Arquitetura Backend

Este repositório contém a API backend desenvolvida em Python, utilizando Flask e SQLAlchemy, para a aplicação MVP Arquitetura.

## Sumário

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Docker](#docker)

## Instalação

### Pré-requisitos

- Python 3.8+
- Virtualenv

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/DDFaller/MVP_Arquitetura_Back.git
cd MVP_Arquitetura_Back
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # Para Windows, use `venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto e configure as seguintes variáveis:

```env
AWS_ACCESS_KEY_ID='AKIATHRQUE3TJXG7QPPQ'
AWS_SECRET_ACCESS_KEY='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'
AWS_REGION='us-east-1'
S3_BUCKET_NAME='mvp-s3'
THIRD_PARTY_API_URL='http://python-backend:5000/'
PORT=3003
HOST=0.0.0.0
```

## Uso

### Iniciar a Aplicação

Inicie o servidor Flask:

```bash
flask run
```

A API estará disponível em `http://localhost:5000`.

## Endpoints

### POST /cloth

Adiciona um novo agendamento à base de dados.

**Corpo da Requisição**:

```json
{
  "user_id": 1,
  "model_name": "nome do modelo",
  "model_bytes": "bytes do modelo"
}
```

**Resposta**:

```json
{
  "id": 1,
  "user_id": 1,
  "model_name": "nome do modelo"
}
```

### DELETE /cloth/<id>

Deleta um modelo da base de dados.

**Resposta**:

```json
{
  "message": "Deleted successfully"
}
```

### PUT /cloth/<id>

Atualiza o nome do modelo na base de dados.

**Corpo da Requisição**:

```json
{
  "id": "1",
  "model_name": "Novo Nome"
}
```

**Resposta**:

```json
{
  "id": 1,
  "user_id": 1,
  "model_name": "Novo Nome"
}
```

## Docker

### Construir a Imagem

```bash
docker build -t mvp_arquitetura_back .
```

### Executar o Container

```bash
docker run -p 5000:5000 --env-file .env mvp_arquitetura_back
```