import requests

# URL do alvo
url = 'http://haiapi.hai111.hsyst.com.br'

# Dados a serem enviados na solicitação POST
data = {
    'key1': 'PROMPT do BOT',
    'key2': 'MENSAGEM A SER ENVIADA'
}

# Envio da solicitação POST
response = requests.post(url, data=data)

# Verificar o status da resposta
if response.status_code == 200:
    print("Solicitação POST enviada com sucesso!")
    print("Resposta:")
    print(response.text)
else:
    print("Falha ao enviar a solicitação POST. Código de status:", response.status_code)
