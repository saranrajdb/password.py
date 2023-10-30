import re
def check(st):
    if len(st)<4 or ' ' in st or '/' in st or st[0].isnumeric():
        return 0
    if not any(map(str.isdigit, st)):
        return 0
    if not re.search(r'\w*[A-Z]\w*', st):
        return 0
    return 1
        
st=input()        
print(check(st))