# There are many built-in exceptions which are raised in python when something goes wrong.Exceptions in python can be handled using a try statement.
# When exception is handled the code runs smoothly without any interruption.
  

while(True):
    num = input("Enter a number: ")
    print("Enter q to exit the program.")

    if(num == "q"):
        break

    try:    
        num = int(num)
        if (num>5):
            print("Number is greater")
        else:
            print("Number is smaller")
    except Exception as e:
        print(f"Your error is : {e}")        

print("Thanks for playing!!!")
