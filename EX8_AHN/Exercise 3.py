def main():
    n, m = eval(input("Enter two numbers to find the GCF seperate using a comma: " ))

    while True:
        if(not m==0):
            n, m = m, n%m
        else:
           print(n, "is the greatest common factor.")
           break
        

main()
