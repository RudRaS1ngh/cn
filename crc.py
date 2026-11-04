msg = str(input("Enter the message: "))
gen = str(input("Enter generator polynomial: "))

def xor(m, g):
    m=list(m)
    n=len(g)
    for i in range(len(m)-n+1):
        if m[i]=='1':
            for j in range(n):
                m[i+j]=str(int(m[i+j])^int(g[j]))
    rem=''.join(m[-(n-1):])
    return rem

msg0=msg+'0'*(len(gen)-1)
rem=xor(msg0,gen)
msgrem=msg+rem
print("Transmitted Message:",msgrem)

rcv=input("Enter received message:")
if '1' not in xor(rcv,gen):
    print("No Error Detected")
else:
    print("Error Detected")
