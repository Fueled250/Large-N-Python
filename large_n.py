#S.McDonald 12/2/2016
#large_n
#This program has a function that accepts a list and a number n. The function then displays
#all the numbers in the list that are greater than the number n.


def main():
    #list of numbers
    num_list = list(range(25)) #range is set to 25. Numbers 0-24 will be used

    #define a number n
    n = 7 #the number 7 is set for the number n

    #find all the numbers in num_list that are greater than n
    larger = [num for num in num_list if num > n] #compare all numbers in num_list with n and find
    #which ones are greater than n and assign them to larger

    #output/display
    print(larger) #display all the numbers in num_list that are greater than n


#call main()
main()
    
