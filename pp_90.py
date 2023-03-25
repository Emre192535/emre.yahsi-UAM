def is_palindrome(text: str) -> bool:
    text = ''.join(c for c in text if c.isalnum())
    text = text.lower()
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("Dad")) # True
print(is_palindrome("Evil olive.")) # True
print(is_palindrome("Never odd or even.")) # True
print(is_palindrome("Amore, Roma.")) # True

print(is_palindrome("test")) # False
print(is_palindrome("ad")) # False
print(is_palindrome("a")) # True

