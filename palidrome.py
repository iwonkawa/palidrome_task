# Test the function
strings = [
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw",
    "No lemon, no melon"
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