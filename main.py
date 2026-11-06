from google import genai
from API_KEY import api_key1
from PIL import Image

GEMINI_API_KEY = api_key1

client = genai.Client(api_key=GEMINI_API_KEY)

chat = client.chats.create(
    model="gemini-3.6-flash",
    config={"temperature": 0.7,
            "system_instruction": "Você é um assistente de sustentabilidade alimentar. Analise o texto ou a foto enviada, identifique os ingredientes principais, estime a pegada de carbono em kg de CO2 e retorne uma resposta com sugestões de substituições mais sustentáveis para os ingredientes identificados. Seja claro e conciso em suas respostas, fornecendo informações práticas e acionáveis para promover escolhas alimentares mais sustentáveis."}
)

print(" EcoPlanet AI Iniciado. Digite 'sair' para encerrar a conversa)")


while True:
    opcao = input("digite 'foto' para enviar uma foto ou digite sua pergunta: ")

    if opcao.lower() == 'sair':
            print("Encerrando o assistente. Até logo!")
            break 

    if not opcao:
        continue


    if opcao.lower() == 'foto':
        caminho = input("Digite o caminho da foto (ex: almoco.jpg): ")

        try:
            imagem = Image.open(caminho)

            conteudo = ["Analise esta foto de refeição e siga suas instruções de sustentabilidade.", imagem]

            resposta2 = chat.send_message(conteudo)
            
            print(resposta2.text)
        except Exception as erro:
            print(f"Erro ao carregar ou processar a imagem: {erro}")

    else:
        resposta1 = chat.send_message(f"{opcao}")
        print(resposta1.text)















