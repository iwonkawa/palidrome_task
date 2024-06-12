# Test the function
strings = [
    "We panic in a pew",
    "racecar",
    "Never a foot too far, even",
    "Was it a car or a cat I saw",
    "Madam, in Eden, I’m Adam"
    "Step on no pets!"
]

def check_palindrome(text):
    # Remove spaces and convert to lowercase
    converted_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Get the length of the converted text
    length = len(converted_text)
    
    # Use a for loop to compare characters from start and end
    for i in range(length // 2):
        if converted_text[i] != converted_text[length - i - 1]:
            return False
    return True


for string in strings:
    print(f'"{string}" -> {check_palindrome(string)}')