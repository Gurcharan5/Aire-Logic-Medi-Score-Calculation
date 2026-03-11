# Importing my get score main function from main so i can calculate medi score for 
# the other variables
from main import get_score_main

# Function to check capillary blood glucose and return relevant score
def check_capillary_blood_glucose(bloodGlucose, period):

    # As the repo did not specify where the inputs were of an enum type, I have
    # followed a similar logic as with air and oxygen where users can input text
    # rather than a number.
    if period not in ["fasting", "2-hours"]:
        print("You did not give a valid fasting condition!")
        return False
    
    # Testing the user gave a user input
    try:
        bloodGlucose = float(bloodGlucose)
        bloodGlucose = round(bloodGlucose, 1)
    except ValueError:
        print("You did not give your blood glucose as a number!")
        return False

    # Returning the correct score based on period and blood glucose value
    else:
        if period == "fasting":
            if (4.0 <= bloodGlucose <= 5.4):
                return 0
            elif (3.5 <= bloodGlucose <= 3.9) or (5.5 <= bloodGlucose <= 5.9):
                return 2
            else:
                return 3
        elif period == "2-hour":
            if (5.9 <= bloodGlucose <= 7.8):
                return 0
            elif (4.5 <= bloodGlucose <= 5.8) or (7.9 <= bloodGlucose <= 8.9):
                return 2
            else:
                return 3

# Function to get the final medi score of a user
def get_score_capillary_bonus(airOrOxygen, consconsciousness, respirationRate, spO2, temperature, bloodGlucose, period):
    
    # Getting medi score for the other variables and adding to the list
    patient_values = [check_capillary_blood_glucose(bloodGlucose, period)]

    total_medi_score = 0

    # Attempting to add the bloody capillary score
    # This will fail if one of the main variables returned False
    try: 
        total_medi_score += get_score_main(airOrOxygen, consconsciousness, respirationRate, spO2, temperature)
    except ValueError:
        print("One or more of your input values is wrong!")
        return

    # Failsafe if the user gives an invalid blood glucse level
    for value in patient_values:
        if value is False:
            print("One or more of your input values is wrong!")
            return
        else:
            total_medi_score += value

    # Return final medi score
    print(f"The final Medi Score for the patient is: {total_medi_score}")
    return total_medi_score
