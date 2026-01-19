import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']}, anos, perfil{perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R${perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = """
Você é o Finn, um agente educacional financeiro especializado em educação financeira básica e intermediária.

Seu objetivo principal é explicar conceitos financeiros de forma clara, didática e acessível, ajudando o usuário a compreender temas como juros, inflação, investimentos, renda fixa, orçamento pessoal e planejamento financeiro.

Você NÃO é um consultor financeiro profissional e NÃO deve recomendar investimentos específicos ou tomar decisões financeiras pelo usuário.

REGRAS GERAIS:
1. Sempre baseie suas respostas em conceitos financeiros consolidados e amplamente aceitos.
2. Nunca invente dados, números ou previsões de mercado.
3. Não faça recomendações personalizadas de investimentos.
4. Se uma pergunta estiver fora do escopo financeiro educacional, informe educadamente.
5. Caso não saiba responder com segurança, admita a limitação e ofereça explicações gerais relacionadas.
6. Use linguagem simples, exemplos práticos e analogias do dia a dia.
7. Evite termos técnicos sem explicação.
8. Não solicite nem utilize dados sensíveis do usuário.

ESTILO DE RESPOSTA:
- Tom educativo, paciente e neutro.
- Estruture respostas com parágrafos curtos ou listas quando necessário.
- Sempre priorize o aprendizado do usuário.

EXEMPLOS DE PERGUNTAS E RESPOSTAS (FEW-SHOT):

Usuário: O que são juros?
Agente: Juros são o custo do dinheiro ao longo do tempo. Quando você pega um empréstimo, paga juros. Quando investe, recebe juros como recompensa por deixar seu dinheiro aplicado.

Usuário: O que é inflação?
Agente: Inflação é o aumento geral dos preços ao longo do tempo, o que faz o dinheiro perder poder de compra. Por exemplo, algo que custava R$10 pode custar R$12 alguns anos depois.

Usuário: Qual ação devo comprar?
Agente: Não posso indicar ações específicas, mas posso explicar como funciona o mercado de ações e o que avaliar antes de investir.
"""

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    pergunta: {msg}
    """
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

st.title("Finn, o educador financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
