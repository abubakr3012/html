x='qWo4iDn!weofneOri1ng5eo$ring^eo6Din12go4e'
nums=0
alpha=0
symbols=0
for i in x:
    if i.isdigit():
        nums+=1
    elif x.isalpha():
        alpha+=1
    else:
        symbols+=1
print(nums)
print(alpha)
print(symbols)
