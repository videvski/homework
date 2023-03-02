The original code doesn't work with the Python 3.11.2 version kernel.
---
There is an error "cannot import name 'fetch' from 'js'".
This error continues to appear even after importing js and updating all other modules.
My workaround was to use the requests module that is made for python and importing it in the file.

'''
{
import requests
res = requests.get('https://raw.githubusercontent.com/luabud/wordle/main/encoded_words.json',headers={'Accept' : 'application/json'})
json_words = res.json()
encoded_words = json_words["encoded_words"]
}
'''
