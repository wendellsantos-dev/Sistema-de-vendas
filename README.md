# Sistema de Vendas 📊

Sistema web interativo para cadastro, gerenciamento e análise de vendas desenvolvido em Python. 

🔗 **[https://sistemadevendasws.streamlit.app/]**

## 🚀 Funcionalidades
- **Formulário de Cadastro:** Registro rápido de novas vendas via barra lateral (sidebar).
- **Validação Inteligente:** Bloqueio de seleção de datas futuras, garantindo a consistência dos dados.
- **Base de Dados Persistente:** Armazenamento automático e leitura direta em arquivo `.csv`.
- **Tabela Interativa:** Visualização completa e dinâmica do histórico de vendas direto na interface.
- **Dashboard Analítico:** 
  - Cálculo automático de faturamento total.
  - Gráfico interativo de barras empilhadas cruzando dados de vendedores e produtos.
  - Gráfico de rosca (donut chart) para análise de faturamento por produto.

## 🛠️ Tecnologias Utilizadas
- **[Python](https://www.python.org/)**
- **[Streamlit](https://streamlit.io/)** (Interface Web e Deploy)
- **[Pandas](https://pandas.pydata.org/)** (Manipulação e leitura de Dados)
- **[Plotly](https://plotly.com/python/)** (Gráficos Interativos)

## 📦 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto no seu computador:

1. Clone este repositório:
   ```bash
   git clone https://github.com/wendellsantos-dev/Sistema-de-vendas.git
   ```

2. Entre na pasta do projeto:
   ```bash
   cd Sistema-de-vendas
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

4. Instale as dependências listadas no projeto:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:
   ```bash
   streamlit run main.py
   ```

## 📂 Estrutura de Arquivos
- `main.py`: Arquivo principal contendo toda a lógica e interface da aplicação.
- `vendas.csv`: Banco de dados local onde os registros são armazenados.
- `requirements.txt`: Lista de dependências (bibliotecas) necessárias para rodar o projeto.
- `.gitignore`: Arquivo de configuração do Git para ignorar pastas de cache e ambiente virtual.