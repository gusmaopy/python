import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc721f58464552ae8597543c09ce6b98f"
# Your Auth Token from twilio.com/console
auth_token = "e2d945fdec2b2383b63a7fdfdfcb3a23"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
   tabela_vendas = pd.read_excel(f'{mes}.xlsx')
   if (tabela_vendas['Vendas'] > 55000).any():
       vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
       vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
       print(f'Celso Gusmão como solicitado no mes de {mes} o vendedor {vendedor}, teve {vendas} de vendas.')
       message = client.messages.create(
           to="+5514997766672",
           from_="+18149291162",
           body=f'Celso Gusmão como solicitado no mes de {mes} o vendedor {vendedor}, teve {vendas} de vendas.')
       print(message.sid)



# Verificar se algum valor na coluna Vendas daquele arquivo é maior de R$ 55.000

# Se for maior do que  R$ 55.000 --> enviar um SMS com o Nome, o mês e as Vendas do Vendedor

# Caso não seja maior do que R$ 55.000 não quero fazer nada