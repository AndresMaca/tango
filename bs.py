import requests

url = 'https://interview.tangohq.com/guess'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiIzYTY4ZTY4YS04Y2YxLTQ3MzItOWJkZC02ZjE5MDAyOTRjNTIiLCJtZXNzYWdlIjoiRGVjb2RpbmcgdGhlIHRva2VuLCBuaWNlLCBoYXZlIGEgcHJpemUiLCJ1cmwiOiIvYm9udXMtam9uYXMiLCJpYXQiOjE3MDA4ODcyMDd9.Cvp5JRyNYGtJudPPB_Qh2MBfdakd5z_hUybL-r84oBk'
}

# Define the range
lower_bound = 1
upper_bound = 100000000

while lower_bound <= upper_bound:
    # Guess using binary search > log(n) n: len(upper_bound - lower_bound)
    guess = (lower_bound + upper_bound) // 2
    payload = {'myGuess': guess}
    response = requests.post(url, headers=headers, json=payload).json()
    print(response)
    # Process the response
    status = response['status']
    if status == 'higher':
        lower_bound = guess + 1
    elif status == 'lower':
        upper_bound = guess - 1
    else:
        print(response)
        print(f"The number is: {guess}")
        break
