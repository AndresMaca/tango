from copy import deepcopy
import requests
# First convert from english to ascci: 
# def string_to_ascii(input_string):
#     return [ord(char) for char in input_string]

# input_string = "Hello Tango"
# ascii_values = string_to_ascii(input_string)
# print(ascii_values)



url = 'https://interview.tangohq.com/guess-escpos'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiI5MWFkYmY2OC0zODcxLTQ2MzMtOWY3Ny0yYzMzODI1NzY5NzYiLCJtZXNzYWdlIjoiRGVjb2RpbmcgdGhlIHRva2VuLCBuaWNlLCBoYXZlIGEgcHJpemUiLCJ1cmwiOiIvYm9udXMtam9uYXMiLCJpYXQiOjE3MDA4ODAxNzd9.tCEybQqLmcuO1dU8i1o4R28C_O9Lhet7OpNEIwm-OHk'
}

# I use this when i struggle to find the right char on the manual.
my_guess = [
    72, 101, 108, 108, 111, 32, 84, 97, 110, 103, 111,
    27, 74, 1,
    73, 39, 109, 32, 101, 120, 99, 105, 116, 101, 100, 32, 116, 111, 32, 106, 111, 105, 110,
    27, 74, 2,
    29, 86, 65, 0
]

# Initialize the starting index
index = 0

# Loop to try different values at index 12
while True:
    # Create a copy of the original array to modify
    guess = deepcopy(my_guess)
    
    # Update the value at index 12 with the current value of `index`
    guess[38] = index
    
    # Print the current array
    print(f"Trying value {index}: {guess}")
    payload = {'myGuess': guess}
    response = requests.post(url, headers=headers, json=payload).json()
    print(response)

    
    # Increment the value for the next iteration
    index += 1
    
    # Break the loop if the index reaches a certain value (adjust as needed)
    if index > 300:
        break