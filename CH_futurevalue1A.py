# CH_furturevalue1A.py
# PSC input principle p1

def main():

    print "calculate a future value of a 10 yr investment"
    p1 = input ("Enter the amount of investment: ")
    
    apr = 0.03

    for i in range (10):
        principal = p1 * ( 1 + apr )

    print "the future investment value in 10 years is: ", principal

main()
