def calculate_fibonacci_sums():

    # maximum limit for numbers
    MAX_VAL = 4*1000000

    #variables to store odd and even sums
    ODD_SUM = 0
    EVEN_SUM = 0

    # f(n-2)
    last_to_last = 0
    # f(n-1)
    last = 1

    # 2nd element is 1, so we add 1 to odd elements sum
    ODD_SUM+=1

    while(last + last_to_last <=MAX_VAL):

        # update f(n-1) and f(n-2) and
        temp = last 
        last += last_to_last
        last_to_last = temp

        #last now stores the new element
        if (last%2==0):
            EVEN_SUM+= last
        else:
            ODD_SUM+= last

    return ODD_SUM, EVEN_SUM


if __name__ == '__main__':
    ODD_SUM, EVEN_SUM = calculate_fibonacci_sums()
    print("sum of odd terms: ", ODD_SUM)
    print("sum of even terms: ", EVEN_SUM)


    