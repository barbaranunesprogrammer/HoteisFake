# 🤖 Chatbot Simples para Hotel

Um chatbot simples desenvolvido em Python para simular um atendimento básico de hotel, respondendo perguntas sobre preços, produtos e finalizando a conversa quando solicitado.

---

## 📌 Status do Projeto

![Status](https://img.shields.io/badge/status-finalizado-brightgreen)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🧠 Funcionalidades

- ✔️ Cumprimenta o usuário pelo nome
- ✔️ Pergunta quantidade de pessoas
- ✔️ Responde sobre preços e produtos
- ✔️ Reage a despedidas
- ✔️ Finaliza com o comando `sair`

---

## 🗂 Estrutura do Código

O bot utiliza detecção de palavras-chave:

```python
if "preço" in mensagem:
    return "Os preços variam conforme o produto..."
▶️ Como Executar o Projeto
Certifique-se de ter Python instalado (3.x)

Salve o código em bot.py

Execute no terminal:

python bot.py
💬 Exemplo de Execução
Hoteis Fake agradece seu contato ! Digite 'sair', para encerrar.

Oi! Qual é o seu nome? > Maria
Quantas pessoas irão se hospedar? > 2
Olá, Maria! Como posso ajudar você hoje?

Maria: preço
Bot: Os preços variam conforme o produto , para 2 pessoas.

Maria: sair
Bot: Até a próxima!
📁 Código Utilizado
def responder(mensagem):

    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem or "ola" in mensagem:
        return f"Olá {nome}! Como posso ajudar?"

    elif "preço" in mensagem or "valor" in mensagem or "custo" in mensagem or "quanto custa" in mensagem or "quanto é" in mensagem or "quanto e" in mensagem or "preços" in mensagem
or "diaria" in mensagem or "diária" in mensagem or "tarifa" in mensagem or "diarias" in mensagem or "tarifas" in mensagem or "valores" in mensagem :
        return f"Os preços variam conforme o produto , para {quantidadeDePessoas} pessoas."

    elif "produto" in mensagem or "produtos" in mensagem or "item" in mensagem or "itens" in mensagem or "mercadoria" in mensagem:
        return "Temos vários produtos disponíveis."

    elif "tchau" in mensagem or "obrigado" in mensagem or "valeu" in mensagem or "até mais" in mensagem
or "ate mais" in mensagem or "adeus" in mensagem or "até logo" in mensagem or "ate logo" in mensagem:
        return "Até mais! Obrigado por conversar comigo!"

    else:
        return "Não entendi, pode repetir?"


print("Hoteis Fake agradece seu contato ! Digite 'sair',para encerrar.\n")
nome = input("Oi! Qual é o seu nome? ")
quantidadeDePessoas = input("Quantas pessoas irão se hospedar? ")
print(f"Olá, {nome}! Como posso ajudar você hoje?\n")
print (f"{nome}, qual e sua duvida ?")
while True:
    user = input(f"{nome}: ")
    if user.lower() == "sair" :
        print("Bot: Até a próxima!")
        break
    resposta = responder(user)
    print("Bot:", resposta)
🛠 Tecnologias
Python 3.x

🧩 Melhorias Futuras
NLP básica

Interface gráfica

Integração com API real

Histórico de conversa

📄 Licença
Este projeto está sob licença MIT — livre para uso e modificação.

👩‍💻 Desenvolvido por
Bárbara Elen Sales Nunes

LinkedIn: https://www.linkedin.com/in/barbaranunesprogrammer/
GitHub: https://github.com/barbaranunesprogrammer


