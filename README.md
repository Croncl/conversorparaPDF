,
````markdown
# Conversor de Arquivos para PDF

Projeto web simples para converter arquivos de imagem (JPG, PNG, BMP) e HTML para PDF.  
Construído com Flask e Docker, com pipeline automatizado no GitLab CI/CD para build, testes, criação e publicação de imagem Docker.

---

## Funcionalidades

- Upload via drag & drop ou seleção de arquivo
- Conversão para PDF
- Suporte a formatos JPG, PNG, BMP e HTML
- Interface simples e responsiva
- Pipeline automatizado com testes e Docker no GitLab

---

## Tecnologias usadas

- Python 3.11
- Flask
- Docker
- GitLab CI/CD
- Pytest (para testes)

---

## Como rodar localmente

1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/conversor-pdf.git
cd conversor-pdf
````

2. Crie e ative seu ambiente virtual (venv)

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Execute a aplicação

```bash
python app.py
```

5. Acesse `http://localhost:5000` no seu navegador

---

## Como usar com Docker

1. Construa a imagem Docker

```bash
docker build -t conversor-pdf .
```

2. Rode o container

```bash
docker run -p 5000:5000 conversor-pdf
```

3. Acesse `http://localhost:5000` no navegador

---

## Pipeline CI/CD (GitLab)

O projeto possui um pipeline configurado no arquivo `.gitlab-ci.yml` com as seguintes etapas:

* Build automatizado
* Execução de testes automatizados (pytest)
* Build da imagem Docker
* Push da imagem para o Container Registry do GitLab

Para funcionar, configure as variáveis de ambiente do GitLab para autenticação no Container Registry.

---

## Testes

Os testes estão localizados na pasta `tests/`. Para rodar os testes localmente:

```bash
pytest tests/
```

---

## Estrutura do projeto

```
conversor-pdf/
├── app.py
├── Dockerfile
├── requirements.txt
├── static/
│   ├── style.css
│   └── fundo.png
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
├── .gitignore
└── .gitlab-ci.yml
```

---

## Contato

Para dúvidas ou sugestões, abra uma issue no GitHub ou entre em contato.

---

© 2025 Conversor PDF - Todos os direitos reservados.

```
