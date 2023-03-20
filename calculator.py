sum = 0
while (True):
    userinput = input("Enter the price:\n")
    if (userinput!= 'q'):
        sum = sum + int(userinput)
        print(f"order total so far{sum}")
    else:
        print(f'your bill total is {sum}.thanks for shopping us.')
        break
    
