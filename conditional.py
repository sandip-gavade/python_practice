n = int(input("please input a number "));
if n<=100 and n>=1:
    print("you have entered -",n," this is between 1 and 100");
    if n<=50 and n>=1:
        print("you have entered -", n, " this is between 1 and 50");
        if n<=25 and n>=1:
            print("you have entered -", n, " this is between 1 and 25");
elif n<=200 and n>=101:
    print("you have entered -", n, " this is  between 101 and 200");
else:
    print("you have entered -", n, " this is  not between 1 and 200");