def main():
    try:
        a=int(input("Enter a number..."))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("I am in Finally..") # If print statement wrote without finally then it will 
        #not run 
        

main()