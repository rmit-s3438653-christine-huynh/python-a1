def main():
    print "calculate a future value of a 10 yr investment"
    principle = 1000
    apr = 0.03

    for i in range (10):
        principal = principal * ( 1 + apr )

    print "the value in 10 years is: ", principal

main()
