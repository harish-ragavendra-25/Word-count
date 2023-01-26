'''
name: HARISH RAGAVENDRA S
reference numbver: 22008967
'''
with open("word.txt",'r') as t:
    count=0
    r=t.read()
    words=r.split(" ")
    for i in words:
        count+=1
    print(count)
