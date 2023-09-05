print("Start API uitlees applicatie")

import requests

paginaresults = requests.get('https://catfact.ninja/facts')

print(paginaresults)

feitjes = paginaresults.json()
print("Feitje is: "+feitjes['data'][0]['fact'])
# print(feitjes['data'][1])