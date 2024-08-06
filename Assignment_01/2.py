def prime_factors(n):

    i = 2
    prime_factors_list = []

    while(i*i<=n):

        while(n>0 and n%i==0):
            n/=i
            # keep dividing by i as long as its divisible
            prime_factors_list.append(i)

        i+=1

    if(n>2):
        prime_factors_list.append(int(n))
    
    return prime_factors_list


if __name__ == "__main__":

    try:
        n = int(input("Enter a number \t"))
        factors = prime_factors(n)

        print(factors)        
    except :
        print("Please enter a valid number..")

