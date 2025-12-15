# POC — API IA Full Stack (FastAPI + Pandas + OpenAI)

## Descrição

Prova de conceito desenvolvida para processos seletivos de vagas Full Stack com foco em IA.  
Esta API recebe uma pergunta do usuário, busca o contexto mais relevante em um conjunto de dados estruturados (CSV via Pandas), constrói um prompt dinâmico e consulta um Large Language Model (LLM, OpenAI GPT) para gerar respostas contextuais.

O projeto demonstra:
- Integração de backend Python (FastAPI) com LLMs (OpenAI GPT)
- Manipulação e análise de dados usando Pandas
- Prompt Engineering básico e resposta dinâmica
- Práticas de API REST moderna e fácil testabilidade

## Funcionalidades

- **Busca de contexto:** Localiza o texto mais relevante no dataset a partir da pergunta recebida
- **Prompt dinâmico:** Usa o contexto para construir prompts e consultar o modelo LLM
- **API RESTful:** Endpoint POST `/ask` recebe perguntas e retorna respostas generadas pela IA
- **Testes automatizados:** Cobertura básica usando pytest
- **Pronto para CI/CD:** Estrutura fácil de adaptar para pipelines e deploy em cloud

## Como rodar

1. Clone o repositório e crie o ambiente virtual:
    ```bash
    git clone https://github.com/robertera/poc-ai-fastapi-llm.git
    cd poc-ai-fastapi-llm
    pip install -r requirements.txt
    ```
2. Defina sua chave da OpenAI em um arquivo `.env` na raiz do projeto:
    ```
    OPENAI_API_KEY=xxxxxx
    ou use o modo fake LLM para testes:
    USE_FAKE_LLM=true
    ```
3. Execute a aplicação localmente:
    ```bash
    uvicorn app.main:app --reload
    ```
4. Acesse a documentação da API em `http://127.0.0.1:8000/docs` e faça uma requisição POST para `/ask`:

    Exemplo:
    ```json
    {
      "question": "Como faço login?"
    }
    ```

## Exemplo de resposta

```json
{
  "answer": "Para realizar o login, acesse o formulário no site, insira seu e-mail e senha cadastrados...",
  "context": "O login é feito por e-mail e senha no site, usando o formulário de acesso."
}