def ispalindrom(s):
    return s == s[::-1]
s="naman"
ans=ispalindrom(s)

if ans:
    print("yes")
else:
    print("no")
    
