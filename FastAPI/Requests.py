import requests

url = "https://graph.facebook.com/v12.0/{{111420255005189}}/message_templates?fields=name,category,content,language,name_or_content,status"

payload={}
headers = {
  'Authorization': 'Bearer {{EAAuvWQ3xYccBALbnV7mmactFX69bAMJtG19BhTvBwvZBo8kVHJZCPkGPXpGebjF3YVATeMYsZB5JJjZB6Lq7i4QLOcq6q75LXjKQ5XJRSvofyZBrnPqdjL9KRPuPfSvqnQmcmV2Qt3TiJHI87jwRXCnaAZCY0JTKk9cb6DqZBw74vPZA1LIjn5pSCprRbMSOuhUQiy6tRnXjawZDZD}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


