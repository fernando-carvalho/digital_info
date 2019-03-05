import requests
import json

code = 'AQTSzhjO8tZs-2pFc3IE7hiiOJu02f2a4YMpuRI8AGWES0SwKjcD3waAgF-qD-3-PE_-_QQILFRHw_8oWkJxg3YqPrJ4HTgFHuv5BeavWvzg9bWEIY95X2N7jT9BYvIl87M-8_9QVyRjNYhoRk3cKtGG_Fe6j0Ljhidl8R-qOmeKN46JuoOEgcuCog3VWw'

response = requests.post('http://www.linkedin.com/oauth/v2/accessToken',
                     data = {'grant_type':'authorization_code',
                     		 'code':code,
                     		 'redirect_uri':'http://68.183.125.29:5000',
                     		 'client_id':'77se22zag9iejz',
                     		 'client_secret':'kBpqQgsjTrWXu4wB'
                     		 }
                     	)

print (response)
#
#print (teste.text)
