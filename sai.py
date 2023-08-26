def is_palindrome(input_string):
    cleaned_string = ''.join(filter(str.isalnum, input_string)).lower()
    return cleaned_string == cleaned_string[::-1]

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
