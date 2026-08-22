# Projeto de IA para auxiliar na identificação de tumores

Projeto de tech challenge referente a fase 1 do curso de pós graduação de Inteligencia artificial para desenvolvedores da faculdade FIAP.
Este projeto tem o objetivo de com base em resultados de exames clinicos salvos no aqruivo dados.csv encontrar padrões nos dados e auxiliar o profissional de saúde na identificação da doença em novos exames 


## Autores
Denilson Dominguez: domingues.denilson2014@gmail.com
Lucas da Silva Torres Martins: lucas.hayim@gmail.com
lucas Nascimento lopes: lucaslsantos159@gmail.com
Uriel Alves da Silva: lioneluri@hotmail.com
Vinicius Breda Silva: vinicius_breda_silva@hotmail.com

🧠 Tecnologias Utilizadas
Tecnologias Utilizadas
Python 3.10+
FastAPI
Uvicorn
Pandas / NumPy
Scikit-Learn
Jupyter Notebook
Pickle (para salvar o modelo)

🗂️ Estrutura do Repositório
techchallenge/
│
├── dados/                     # Base de dados utilizada no projeto
├── diagnosticos.ipynb         # Notebook com análise exploratória e testes
├── main.py                    # API FastAPI para servir o modelo
├── modelo_pipeline.pkl        # Modelo treinado
├── .gitignore
├── LICENSE
└── README.md

🚀 Como Executar o Projeto
1. Criar ambiente virtual
python -m venv env
2. Ativar o ambiente
env\Scripts\activate
3. Instalar dependências
pip install -r requirements.txt
4. Executar a API
uvicorn main:app --reload
A API ficará disponível em:
http://127.0.0.1:8000
🔍 Endpoints Principais

GET /predict

