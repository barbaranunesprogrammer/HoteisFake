

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
    
    elif "wi-fi"in mensagem or "wifi" in mensagem or "internet" in mensagem or "wifi gratuito" in mensagem or "wi-fi gratuito" in mensagem or "internet gratuita" in mensagem:
        return "Sim, oferecemos Wi-Fi gratuito para todos os hóspedes."
    
    elif "incluso" in mensagem or "inclusa" in mensagem or "inclusos" in mensagem or "inclusas" in mensagem or "café da manhã" in mensagem or "cafe da manha" in mensagem:
        return "Sim, o café da manhã está incluído na diária."
    
    elif "check-in" in mensagem or "checkin" in mensagem or "entrada" in mensagem or "horário de entrada" in mensagem or "horario de entrada" in mensagem:
        return "O check-in é a partir das 14h."
    elif "piscina" in mensagem or "academia" in mensagem or "spa" in mensagem or "fitness" in mensagem or "lazer" in mensagem:
        return "Sim, temos piscina, academia e spa disponíveis para os hóspedes."
    elif "cancelamento" in mensagem or "política de cancelamento" in mensagem or "cancelar reserva" in mensagem:
        return "Nossa política de cancelamento permite cancelamentos gratuitos até 24 horas antes da data de chegada."
    elif "estacionamento" in mensagem or "vaga de carro" in mensagem or "parking" in mensagem:
        return "Oferecemos estacionamento gratuito para os hóspedes."
    elif "animais de estimação" in mensagem or "pet" in mensagem or "pets" in mensagem or "animalzinho" in mensagem:
        return "Sim, aceitamos animais de estimação mediante uma taxa adicional."
    elif "ar-condicionado" in mensagem or "ar condicionado" in mensagem or "climatização" in mensagem:
        return "Todas as nossas acomodações possuem ar-condicionado."
    elif "contato" in mensagem or "telefone" in mensagem or "e-mail" in mensagem or "email" in mensagem:
        return "Você pode entrar em contato conosco pelo telefone (11) 1234-5678 ou pelo e-mail contato@hoteisfake.com.br"
    elif "pagamento" in mensagem or "formas de pagamento" in mensagem or "cartão de crédito" in mensagem or "dinheiro" in mensagem:
        return "Aceitamos diversas formas de pagamento, incluindo cartões de crédito, débito e dinheiro."
    elif "crianças" in mensagem or "bebês" in mensagem or "menores" in mensagem:
        return "Crianças são bem-vindas! Oferecemos berços e camas extras mediante solicitação."
    elif "quantas pessoas" in mensagem or "capacidade" in mensagem or "lotação" in mensagem:
        return f"Nossas acomodações podem acomodar confortavelmente 8 pessoas.\n"
    else:
        return "Não entendi, pode repetir?"

print("Hoteis Fake agradece seu contato! Digite 'sair' para encerrar.\n")

nome = input("Oi! Qual é o seu nome?")

quantidadeDePessoas = input("Quantas pessoas irão se hospedar?")

if int(quantidadeDePessoas) <= 8:
    print("Ótimo! Temos acomodações disponíveis para essa quantidade de hóspedes.\n")
else:
    print("Nossas acomodações suportam até 8 pessoas por quarto. Para mais pessoas, será necessário reservar mais de um quarto.")

quantidadeDeQuartos = input("Quantos quartos você gostaria de reservar? ")

print(f"Perfeito, {nome}. Você está reservando {quantidadeDeQuartos} quarto(s) para {quantidadeDePessoas} pessoa(s).")

print(f"Agora posso tirar suas dúvidas sobre sua estadia, {nome}.")
print("O que você gostaria de saber?")

while True:
    user = input(f"{nome}: ")
    if user.lower() == "sair" :
        print("Bot: Até a próxima!")
        break
    resposta = responder(user)
    print(f"Bot:  {resposta}\n")

