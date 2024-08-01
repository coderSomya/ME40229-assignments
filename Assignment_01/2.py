def prime_factors(n):

    i = 2
    prime_factors_list = []

    while(i<=n):

        while(n>0 and n%i==0):
            n/=i
            prime_factors_list.append(i)

        i+=1
    
    return prime_factors_list


if __name__ == "__main__":
    
    n = int(input("Enter a number \t"))
    factors = prime_factors(n)

    print(factors)