# 🐾 Sistema de Gerenciamento para Clínica Veterinária

Este é um sistema de gerenciamento para uma clínica veterinária, desenvolvido para facilitar o controle de consultas, pacientes e funcionários. O sistema foi projetado exclusivamente para uso interno, garantindo acesso restrito a médicos e funcionários por meio de autenticação segura.

---

## 🚀 Funcionalidades

- **Cadastro e gerenciamento** de médicos, funcionários e pacientes.
- **Agendamento de consultas** com detalhes completos de cada atendimento.
- **Histórico médico**: Registro detalhado das consultas realizadas.
- **Autenticação JWT**: Segurança para acesso ao sistema.
- **Upload de arquivos**: Permite anexar documentos ou imagens a consultas.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework Web:** Flask
- **Banco de Dados:** MySQL
- **Autenticação:** JWT (JSON Web Token)

---

## ⚙️ Configuração do Projeto

### Pré-requisitos

Certifique-se de ter instalado:

- [Python 3.9+](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/)
- Gerenciador de pacotes `pip`

### Passo a passo

1. **Clone o repositório:**
   ```bash
  (https://github.com/softexrecifepe/PI-MASCOT-TURMA-15.1.git)




2. **Crie um ambiente virtual e ative-o:**

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate


3. **Instale as dependências:**

pip install -r requirements.txt

4. **Configure o arquivo config.py:**

Abra o arquivo config.py no diretório raiz.
Edite os campos de conexão com o banco de dados MySQL, como username e password:


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://seu_usuario:sua_senha@localhost/seu_banco'
SECRET_KEY = 'sua_chave_secreta_para_jwt'

5. **Configure o banco de dados:**

Certifique-se de que o banco de dados MySQL esteja rodando.

Crie o banco de dados para o sistema:

CREATE DATABASE nome_do_banco;


6. **Realize as migrações do banco de dados:**

flask db upgrade


7. **Inicie o servidor:**

flask run

===========================================




🚧 Planejamento e Melhorias Futuras
- Relatórios: Implementação de relatórios detalhados de atendimentos e histórico.
- Integração com APIs de pagamento: Facilitar o gerenciamento financeiro da clínica.
- Aprimoramento da segurança: Auditoria de acesso e logs detalhados.

