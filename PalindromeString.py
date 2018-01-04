def reverse(s):
    x=s[::-1]
    print x
    return x
 
def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False

s = "malayalam"
ans = isPalindrome(s)
if ans == 1:
    print("Yes")
else:
    print("No")