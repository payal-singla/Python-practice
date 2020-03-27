def palindrome(name):
    reversed_string = name[::-1]
    if reversed_string==name:
        return 'its palindrome'
    return 'its not'

    
name=input("Enter the name you want to check: ")
print(palindrome(name))