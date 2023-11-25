import requests
import string

# Function to send a word guess to the API
def guess_word(word):
    # API endpoint and headers
    url = 'https://interview.tangohq.com/guess-word'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiIzYTY4ZTY4YS04Y2YxLTQ3MzItOWJkZC02ZjE5MDAyOTRjNTIiLCJtZXNzYWdlIjoiRGVjb2RpbmcgdGhlIHRva2VuLCBuaWNlLCBoYXZlIGEgcHJpemUiLCJ1cmwiOiIvYm9udXMtam9uYXMiLCJpYXQiOjE3MDA4ODcyMDd9.Cvp5JRyNYGtJudPPB_Qh2MBfdakd5z_hUybL-r84oBk'
    }
    payload = {'myGuess': word}
    
    # Sending the guess and returning the JSON response
    return requests.post(url, headers=headers, json=payload).json()

# Function to fetch valid characters to form a word
def fetch_valid_chars(max_word_len):
    word_set = set()
    all_letters = string.ascii_lowercase
    
    # Iterating over letters to form a word based on the API response
    for i in range(0, len(all_letters), 4):
        group = all_letters[i:i+max_word_len]
        response = guess_word(group)["hint"]["character"]
        valid_words = [group[index] for index, content in enumerate(response) if content]
        for char in valid_words:
            word_set.add(char)
        if len(word_set) == max_word_len: 
            break
    
    return ''.join(word_set)

# Function to reveal the word by guessing and printing the API responses
def reveal_word(word_set):
    word =  ''.join(word_set)
    
    # Iterating through the word and guessing characters to reveal the word
    # we don't need to go tru all the alphabet but only from our word_set as they are the only valid words.
    # that give us a O(K*N) where K: len(word_set) and N: position_and_character n<1000 and K < max(english_char_ascii)
    for char in word_set:
        response = guess_word(word)
        print(response)
        position_and_character = response["hint"]["positionAndCharacter"]
        result = [word[index] if content else str(char) for index, content in enumerate(position_and_character)]
        print(result)
        word = ''.join(result)
        print(word)

    response = guess_word(word)
    print(response)

# Define maximum word length for the API call
max_word_len = 4

# Fetch valid characters to form a word
word_set = fetch_valid_chars(max_word_len)

# Reveal the word by guessing characters
reveal_word(word_set)
