def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


s1 = "RADAR"
if is_palindrome(s1):
    print(f"{s1} είναι παλίνδρομη.")
else:
    print(f"{s1} δεν είναι παλίνδρομη.")

s2 = "ΣΟΦΟΣ"
if is_palindrome(s2):
    print(f"{s2} είναι παλίνδρομη.")
else:
    print(f"{s2} δεν είναι παλίνδρομη.")

s3 = "PYTHON"
if is_palindrome(s3):
    print(f"{s3} είναι παλίνδρομη.")
else:
    print(f"{s3} δεν είναι παλίνδρομη.")
