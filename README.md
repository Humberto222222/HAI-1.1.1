Olá a todos, me chamo Humberto, conhecido no Discord como "op3n". Esse projeto, tem como objetivo permitir que você use uma IA, em qualquer dispositivo sem a necessidade de pagar.

# COMO USAR?

Aqui você pode seguir dois caminhos

Caminho 1 (Usando a API Self-Hosted "Hospedada por mim no caso e o modo mais facil.")
Caminho 2 (Usando direto da fonte, usando o Gemini.)

***Obs:.* O caminho "1" será representado por 1.1, 1.2, 1.3 etc... e o caminho "2" será representado por 2.1, 2.2, 2.3 etc...**

1.1: Crie um script na sua linguagem preferida mandando uma requisição POST para o haiapi.hai111.hsyst.com.br
1.2: Segue abaixo um exemplo em python:
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


# Caminho 2

O caminho dois, é muito mais complexo, e por ter uma documentação muito boa explicando tudo muito bem, acesse o GitHub do Google e procure por Gemini Cookbook ou acesse o link abaixo
-- || https://github.com/google-gemini/cookbook || --


# Agradecimentos!

Obrigado por ver este projeto e espero ter te ajudado a realizar sua aplicação ou algo relacionado. Esta "API" está em desenvolvimento e abaixo você pode ver os status dele.

# STATUS

O status da api está: ***EM DEPLOY, TEMPO EXTIMADO PARA RETORNO: 5 horas***
