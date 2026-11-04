n=int(input("Enter number of packets:"))
psize=[]
accept=[]
sent=[]
remm=[]
rem=0
cap=int(input("Enter bucket capacity:"))
rate=int(input("Enter rate of drops:"))

for i in range(n):
    psize.append(int(input("Enter packet size:")))

for i in range(n):
    if (psize[i]+rem)>cap:
        accept.append("Dropped")
        sent.append(0)
        rem=0
        remm.append(rem)
    else:
        accept.append(psize[i])
        if (psize[i]+rem)>rate:
            sent.append(rate)
            rem+=(psize[i]-rate)
            remm.append(rem)
        else:
            sent.append(psize[i]+rem)
            rem=0
            remm.append(rem)
            
for i in range(n):
    print(i," ",psize[i]," ",accept[i]," ",sent[i]," ",remm[i])
     
