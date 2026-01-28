

def responder(mensagem):

    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem or "ola" in mensagem:
        return f"Olá {nome}! Como posso ajudar?"

    elif "preço" in mensagem or "valor" in mensagem or "custo" in mensagem or "quanto custa" in mensagem or "quanto é" in mensagem or "quanto e" in mensagem or "preços" in mensagem or "diaria" in mensagem or "diária" in mensagem or "tarifa" in mensagem or "diarias" in mensagem or "tarifas" in mensagem or "valores" in mensagem :
        return f"Os preços variam conforme o produto , para {quantidadeDePessoas} pessoas."

    elif "produto" in mensagem or "produtos" in mensagem or "item" in mensagem or "itens" in mensagem or "mercadoria" in mensagem:
        return "Temos vários produtos disponíveis."

    elif "tchau" in mensagem or "obrigado" in mensagem or "valeu" in mensagem or "até mais" in mensagem or "ate mais" in mensagem or "adeus" in mensagem or "até logo" in mensagem or "ate logo" in mensagem:
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
