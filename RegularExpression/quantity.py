from re import finditer

text="abcd67py0844puqr123cdef"

# pattern="[a-z]{3}"
# pattern="[0-9]{4}"
# pattern="([c-h]|[t-z])" 

pattern="([a-z]{3}|[0-9]{3})"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"===",m.group())