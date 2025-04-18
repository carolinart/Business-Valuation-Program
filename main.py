# import the other files so we can access their classes
from business_val import BusinessValuation
from validation import ValidationClass

def main():

    # create an instance of the BusinessValuation class
    valuation = BusinessValuation()


    # get and validate values entered from get_monetary_values,
    # and get_years functions
    initial_revenue = get_monetary_values('Initial Revenue')
    final_revenue = get_monetary_values('Final Revenue')
    years = get_years('Number of Years Between Values')
    cost = get_monetary_values('Cost of Capital (e.g. 0.1 for 10%)')

    # pass the validated user inputs to the BusinessValuation object
    valuation.set_initial_revenue(initial_revenue)
    valuation.set_final_revenue(final_revenue)
    valuation.set_years(years)
    valuation.set_cost_of_capital(cost)

    # display valuation report
    print("\n--- Valuation Report ---")
    print(valuation)
    

# User input for initial revenue, final revenue, and cost of capital (floats)
def get_monetary_values(value):

    # create an instance of the ValidationClass
    validation = ValidationClass()
    
    float_input = -1                # arbitrary bad value to start loop

    # ask user for input
    while float_input == -1:
        input_val = input("Enter " + value + ": ")

        # use the validation class to check float value entered by user
        float_input = validation.checkFloat(input_val)

        # see if the value is valid
        if float_input == -1:       # there is a problem
            print(value + " must be a positive number. Try again.")

    return input_val


# User input for years between initial and final revenue (integer)
def get_years(value):

    # create an instance of the ValidationClass
    validation = ValidationClass()
    
    int_input = -1                  # arbitrary bad value to start loop
    
    # get number of years between values from user
    while int_input == -1:
        years = input("Enter number of years between values: ")

        # use the validation class to check integer value entered by user
        int_input = validation.checkInteger(years)

        # see if the value is valid
        if int_input == -1:       # there is a problem
            print(value + " must be a value greater than zero. Try again.")

    return years    



# call main function
main()
