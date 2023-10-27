import itertools as it
import time


def nth_prime(length):
    Prime_List = [2,3]
    
    for i in it.count(Prime_List[-1],2):
        if i%3 ==0:
            continue
        
        Isprime= True
        limit = int(i ** 0.5)+1
        
        for j in Prime_List:
            if (i%j)==0:
                Isprime = False
                break
            
            if j > (limit):
                break
            
        if Isprime:
            Prime_List.append(i)
            if len(Prime_List) == length-2:
                break
            
    print(i)
    
if __name__ =="__main__":
    start = time.perf_counter()
    
    n=1000000
    nth_prime(n)
    print(time.perf_counter() - start)
    # you can access all the primes found till N in the (Prime_List) list