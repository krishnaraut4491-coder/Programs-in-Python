"""
Recursion :- a function call itself till certain conditon is met
factorial of n = n*(n-1)*(n-2)*.....*2*1
n!= n*(n-1)*(n-2)*.....*2*1

there are 2 parts of recursive function

1.base/terminal :- where to stop
2.recursive condition
"""
# #without recursion
# def fac(n):
#     n_factorial=1
#     while n>1:
#         n_factorial=n_factorial*n
#         n=n-1
#     print(n_factorial)
# fac(4)
#with recursion
def fact_rec(n):
    if n == 1:
        return 1
    else :
        n_factorial=n*fact_rec(n-1)
        n=n-1
    return n_factorial

if __name__ == "__main__":
    print(f" factorial is {fact_rec(5)}")