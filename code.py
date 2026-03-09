with open ("distanze.txt", 'r', encoding='utf-8') as f:
    lines=f.readlines()
    f.close()

with open ("listino.txt", 'r', encoding='utf-8') as ff:
    lines2=ff.readlines()
    ff.close()

cit_let={}
for line in lines2:
    parti=line.strip().split()
    lett=parti[0]
    num=parti[-1]
    cit=" ".join(parti[1:-1])
    cit_let[lett]=(cit, num)

colleg=[]
for line in lines:
    city , distance = line.strip().split(":")
    x , y = city.split("-")
    if x=="a":
        colleg.append(y)
    elif y=="a":
        colleg.append(x)
for elem in colleg:
    print(cit_let[elem][0])

m=(0,0)
for elem in cit_let:
    if cit_let[elem][1]>m:
        m=(elem, cit_let[elem][1])



