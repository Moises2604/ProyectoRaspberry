import requests
import sys
 
id = "@Bot_Polo_bot"
 
token = "677207877:AAHplxYT3iixb9wA1MMhjDu7jBetq4DiVQQ"
 
url = "https://api.telegram.org/bot" + token + "/sendMessage"
params = {
'chat_id': id,
 
'text' : str('holaa')
}
 
requests.post(url, params=params)
