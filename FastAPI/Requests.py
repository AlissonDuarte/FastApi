import requests

url = "https://graph.facebook.com/v12.0/{{111420255005189}}/message_templates?fields=name,category,content,language,name_or_content,status"

payload={}
headers = {
  'Authorization': 'Bearer {{insira sua header aqui}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


