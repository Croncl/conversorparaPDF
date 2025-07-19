# Conversor de Arquivos para PDF - Projeto com CI/CD e Kubernetes

![Badge Status](https://img.shields.io/badge/status-operacional-success) ![Licença](https://img.shields.io/badge/licença-MIT-blue)

## 📌 Visão Geral

Projeto web para conversão de arquivos (JPG, PNG, BMP, HTML) para PDF, com pipeline automatizado de CI/CD no GitLab e implantação em cluster Kubernetes no GKE.

## ✨ Funcionalidades

- **Conversão de arquivos** para PDF
  - Formatos suportados: JPG, PNG, BMP, HTML
- **Interface intuitiva**
  - Upload via drag & drop ou seleção de arquivo
  - Design responsivo
- **Infraestrutura avançada**
  - Pipeline CI/CD automatizado
  - Deploy contínuo no GKE
  - HTTPS com Let's Encrypt
  - Domínio personalizado via DuckDNS

## 🛠️ Tecnologias Utilizadas

| Categoria       | Tecnologias                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Backend         | Python 3.12, Flask                                                         |
| Containerização | Docker                                                                      |
| Infraestrutura  | Kubernetes (GKE), cert-manager, Helm                                        |
| CI/CD           | GitLab CI/CD                                                                |
| Segurança       | Let's Encrypt, HTTPS                                                        |
| DNS             | DuckDNS                                                                     |

## 📂 Estrutura do Projeto

bash
conversorpdf/
├── app.py               # Aplicativo Flask
├── conversor.py         # Lógica de conversão
├── requirements.txt     # Dependências Python
├── Dockerfile           # Configuração da imagem Docker
├── k8s/                 # Configurações Kubernetes
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── pvc.yaml
│   ├── cluster-issuer-staging.yaml
│   └── certificate.yaml
├── tests/               # Testes unitários
├── .gitlab-ci.yml       # Pipeline CI/CD
└── README.md


## 🚀 Implantação

### Pré-requisitos
- Conta no Google Cloud com projeto criado
- Cluster GKE configurado
- Domínio DuckDNS ativo
- Repositório GitLab configurado

### 🔧 Configuração Kubernetes

1. Aplique os recursos:
bash
kubectl apply -f k8s/


2. Verifique o status:
bash
kubectl get all


### 🐳 Docker

bash
# Build da imagem
docker build -t registry.gitlab.com/Croncl/conversorpdf:latest .

# Push para o registry
docker push registry.gitlab.com/Croncl/conversorpdf:latest


## 🔒 Segurança e HTTPS

- **cert-manager** instalado via Helm
- **ClusterIssuer** configurado para Let's Encrypt
- Certificado TLS automático para o domínio

## ⚙️ Pipeline GitLab CI/CD

Estágios principais:
1. **build**: Compilação do projeto
2. **test**: Execução de testes unitários
3. **package**: Build e push da imagem Docker
4. **deploy**: Deploy automatizado no GKE

## 🌐 Acesso

- **Domínio**: devops20251-conversorpdf.duckdns.org
- **Protocolo**: HTTPS habilitado

## 🔐 Variáveis de Ambiente

| Variável            | Descrição                                  |
|---------------------|-------------------------------------------|
| GCLOUD_SERVICE_KEY| Chave da Service Account (base64)         |
| CI_REGISTRY_USER  | Usuário do GitLab Registry                |
| CI_JOB_TOKEN      | Token de autenticação do job              |

## 📞 Contato

**Cristovão Lacerda Cronje**  
📧 Email: [lacerdacris83@gmail.com](mailto:lacerdacris83@gmail.com)

---
