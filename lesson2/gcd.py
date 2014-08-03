def gcd(p,q):
    if q == 0: return p
    else: return gcd(q, p % q)
    
print gcd(100, 15)
print gcd(91, 15)
print gcd(33, 15)