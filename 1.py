word=input("Eter a  word:")
a=len(word)
new_word=""
for i in range(a):
    if i%2==1:
        new_word+=word[i].upper()
    else:
        new_word+=word[i]

print(new_word)