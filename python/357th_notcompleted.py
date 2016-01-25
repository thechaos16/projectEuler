import math
import prime_handler as ph

def divisors(n):
    div = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if i not in div:
                div.append(i+n/i)
    return div

def checker(n,obj = None):
    div = divisors(n)
    dd=0
    for i in range(len(div)):
        if obj.is_prime(div[i])==0:
            dd=1
            break
    if dd==0:
        return 1
    return 0

nn = []
#for i in range(2,100000000):
 #   if checker(i)==1:
  #      nn.append(i)

phi = ph.PrimeHandler(100000000)
prime_list = phi.get_prime_list()
print('list is finished')
cnt=0
for prime in prime_list:
    if checker(prime-1,prime_list):
        #print(prime-1)
        cnt+=prime-1
