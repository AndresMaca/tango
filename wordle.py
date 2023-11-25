import requests
import string

def guessWord(word):
    url = 'https://interview.tangohq.com/guess-word'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiIzYTY4ZTY4YS04Y2YxLTQ3MzItOWJkZC02ZjE5MDAyOTRjNTIiLCJtZXNzYWdlIjoiRGVjb2RpbmcgdGhlIHRva2VuLCBuaWNlLCBoYXZlIGEgcHJpemUiLCJ1cmwiOiIvYm9udXMtam9uYXMiLCJpYXQiOjE3MDA4ODcyMDd9.Cvp5JRyNYGtJudPPB_Qh2MBfdakd5z_hUybL-r84oBk'
    }
    payload = {'myGuess': word}
    
    return requests.post(url, headers=headers, json=payload).json()

max_word_len = 4
word_set = set()
all_letters = string.ascii_lowercase

for i in range(0, len(all_letters), 4):
    group = all_letters[i:i+max_word_len]
    response = guessWord(group)["hint"]["character"]
    valid_words = [group[index] for index, content in enumerate(response) if content]
    for char in valid_words:
        word_set.add(char)
    if len(word_set) == max_word_len: 
        break
    
    print(group)

# while True: 
word =  ''.join(word_set)
for char in word_set:
    response = guessWord(word)
    print(response)
    position_and_character = response["hint"]["positionAndCharacter"]
    result = [word[index] if content else str(char) for index, content in enumerate(position_and_character)]
    print(result)
    word = ''.join(result)
    print(word)

response = guessWord(word)
print(response)
