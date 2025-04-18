# Program Description: creates a class to make sure inputs are valid

class ValidationClass:

    # create function that checks correct float input value
    def checkFloat(self, str_input):
        try:
            answer = float(str_input)       # try to convert string to float
        except:
            return -1                       # invalid if input was not numeric

        if answer < 0:                      # check if input is a positive number
            return -1

        # user provided a valid float input
        return answer


    # create a function that checks correct integer input value
    def checkInteger(self, str_input):
        try:
            answer = int(str_input)         # try to convert string to integer
        except:
            return -1
        
        if answer <= 0:
            return -1

        # user provided a valid integer input
        return answer
