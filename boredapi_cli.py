import requests
ninjakey = '9CFsOYH9VcBCKu1QpLue9w==y2N1CwwvEpmadf7A'

apii = 'https://api.api-ninjas.com/v1/thesaurus?word=cute'

resp = (requests.get(apii, headers={'X-Api-Key': ninjakey})).json()

print(resp)


