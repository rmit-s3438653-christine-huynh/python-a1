# CH_futurevalue1C.py
# PSC input principle p1
# input interest rate apr
# input number of years for investment

def main():

    print "calculate a future value of a 10 yr investment"
    p1 = input ("Enter the amount of investment: ")
    apr = input ("Enter the annual interest rate: ")
    year = input ("Enter the number of years for the investment: ")
    

    for i in range (year):
        principal = p1 * ( 1 + apr )

    print "the future investment value in 10 years is: ", principal

main()
