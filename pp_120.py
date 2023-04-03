def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
    

words = ['Dad', 'Evil olive.', 'Never odd or even.', 'Amore, Roma.', 'test', 'ad', 'a']


for s in words:
    if is_palindrome(s):
        print(f'{s} is a palindrome')
    else:
        print(f'{s} is not a palindrome')