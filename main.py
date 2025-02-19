f=open('data.txt', 'r')

wamount=f.readline()

words={}

for line in f:
    b=line.replace('\n', '').split('-')
    en=b[0]
    de=b[1]
    words[b[0]]=b[1]    
f.close()

a=input("შეიყვანეთ სიტყვა რომელიც გინდათ გადათარგმნოთ (ინგლისურად): ")
print(f"გერმანულად {a} არის - {words[a]}")
f=open('history.txt', 'a')
f.write(a + '\n')
f.close()



