# b > a

def euclid_algo(a,b):
    if b==0:
        return a, 0, 1
    gcd, u, v = euclid_algo(b, a % b)
    x = v - (a//b) * u
    y = u
    return gcd, x, y

print(euclid_algo(10, 25))
print(euclid_algo(172, 62))
print(euclid_algo(17, 3400))
