# Finn — Agente Educacional Financeiro com IA

Este é o projeto **Finn**, um agente educacional financeiro inteligente criado como parte do desafio *DIO Lab: BIA do Futuro* para demonstrar um assistente de IA generativa focado em **educação financeira**.

O agente foi idealizado para explicar conceitos financeiros de forma clara e acessível, ajudando usuários a entender temas como **juros, inflação, renda fixa, planejamento de orçamento e conceitos de investimento**, sem fazer recomendações personalizadas de ativos.

---

## Visão Geral

O Finn é um agente de IA projetado para:

- Explicar conceitos financeiros de forma simples e didática.
- Responder dúvidas comuns sobre finanças pessoais.
- Evitar alucinações ou respostas inseguras, mantendo foco educacional.
- Admitir limitações e redirecionar quando necessário.

Este projeto inclui documentação completa, prompts bem definidos, exemplos de uso e uma aplicação funcional de chatbot (protótipo).

---

## Estrutura do Repositório
```
dio-lab-bia-do-futuro/
├── README.md # (este arquivo)
├── docs/ # Documentação do agente
│ ├── 01-documentacao-agente.md
│ ├── 02-base-conhecimento.md
│ ├── 03-prompts.md
│ ├── 04-metricas.md
│ └── 05-pitch.md
├── data/ # Base de conhecimento (dados mockados)
│ ├── transacoes.csv
│ ├── historico_atendimento.csv
│ ├── perfil_investidor.json
│ └── produtos_financeiros.json
├── src/ # Código da aplicação (chatbot)
│ └── app.py
├── assets/ # Imagens e diagramas
└── examples/ # Exemplos de interações e casos de uso
```
yaml
Copiar código

---

## Como Funciona

1. **Documentação:** Definição do caso de uso, persona, arquitetura e segurança do agente.
2. **Base de Conhecimento:** Dados mockados organizados para uso seguro pelo agente.
3. **Prompts:** *System prompt* e exemplos de interação para guiar o comportamento da IA.
4. **Aplicação Funcional:** Protótipo de chatbot integrando LLM com dados e prompts.
5. **Métricas:** Critérios definidos para avaliar respostas e minimizar alucinações.
6. **Pitch:** Apresentação de 3 minutos explicando o valor da solução.

---

## Principais Funcionalidades

- **Respostas educativas e contextualizadas** sobre temas financeiros.
- **Estrutura de prompts robusta** para minimizar respostas incorretas.
- **Exemplos de interações** reais no manual de prompts.
- **Arquitetura de integração** entre interface, LLM e base de conhecimento.

---

## Tecnologias

- Chatbot com LLM (ex:OLLAMA gpt-oss:20b)
- Protótipo interativo (ex: Streamlit)
- Dados mockados em CSV/JSON
- Markdown para documentação

---

## Base de Conhecimento

Os arquivos em `data/` servem como referência de dados modelados para o agente — eles **não contêm informações sensíveis** e podem ser adaptados para diferentes casos de uso.

---

## Licença

Este projeto foi desenvolvido como parte de um desafio educacional e pode ser usado e adaptado livremente para fins de aprendizado.

---

## Contribuição

Contribuições, sugestões e melhorias são bem-vindas!  
Se quiser testar ou expandir o Finn, abra uma issue ou envie um pull request.

---

Obrigado por visitar este projeto! 🚀  
Finn — *ensinar finanças com IA, de forma simples e responsável*.
