# CH_futurevalue1B.py
# PSC input principle p1
# input interest rate apr

def main():

    print "calculate a future value of a 10 yr investment"
    p1 = input ("Enter the amount of investment: ")
    apr = input ("Enter the annual interest rate: ")
    

    for i in range (10):
        principal = p1 * ( 1 + apr )

    print "the future investment value in 10 years is: ", principal

main()
