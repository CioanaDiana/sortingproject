with open("length.txt","r") as f:
    n=f.readline()
    a=[int(i) for i in f.readline().split()]
#a.sort()
#a.sort(reverse=True)
with open("length.txt","w", encoding="utf-16") as f:
    f.write(str(n) + "\n")
    f.write(" ".join (str(i) for i in a))