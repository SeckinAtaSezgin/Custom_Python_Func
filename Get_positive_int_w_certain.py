def get_p_integer():
    class NotPositiveError(UserWarning):
        pass
    class Wrong_Input_Error(UserWarning):
        pass
    class UncertaintyError(UserWarning):
        pass
    while True:
        try:
            number = int(input("Please enter a positive number: "))
            if number < 0:
                raise NotPositiveError
            else:
                while True:
                    q = str(input("Are you Sure? (yes or no?)")).lower()
                    try:
                        q == "yes"
                        if q != "no" and q != "yes":
                            raise Wrong_Input_Error
                        elif q == "no":
                            raise UncertaintyError
                        break
                    except Wrong_Input_Error:
                        print("Just yes or no")
            return(number)
        except ValueError:
            print("This was not a number, please try again.")
        except NotPositiveError:
            print("The number was not positive, please try again.")
        except UncertaintyError:
            print("Try another number")
