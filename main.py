# Importing required libraries for the enums
from enum import IntEnum

# Creating the enum classes for air or oxygen and also 
class PatientAirOrOxygen(IntEnum):
    air = 0
    oxygen = 2

class PatientConsciousness(IntEnum):
    alert = 0
    CVPU = 3

# Function to check patient breath
def check_patient_breath(airOrOxygen):

    # Checking the user has given a valid input
    if airOrOxygen not in ["air", "oxygen"]:
        print("You did not give a valid type for oxygen or air!")
        return False

    # Returning the correct medi score based off of the enum class
    if airOrOxygen == "air":
        return PatientAirOrOxygen.air.value
    else:
        return PatientAirOrOxygen.oxygen.value

# Function to check patient consciousness     
def check_patient_consciousness(conconsciousness):

    # Checking the user has given a valid input
    if conconsciousness not in ["alert", "CVPU"]:
        print("You did not give a valid patient conconsciousness!")
        return False
    
    # Returning the correct medi score based off the enum class
    if conconsciousness == "alert":
        return PatientConsciousness.alert.value
    else:
        return PatientConsciousness.CVPU.value

# Function to check the respiration rate
def check_patient_respiration_rate(respirationRate):

    # Checking the user has given a number input
    try:
        respirationRate = int(respirationRate)
    except ValueError:
        print("You did not give your respiration rate as a number!")
        return False

    # Returning the correct medi score based off the value
    if (12 <= respirationRate <= 20):
        return 0
    elif (9 <= respirationRate <= 11):
        return 1
    elif (21 <= respirationRate <= 24):
        return 2
    else:
        return 3

# Function to check the spO2 levels
def check_patient_spO2(airOrOxygen,spO2):

    # Checking the user has given a validd input for air or oxygen
    if airOrOxygen not in ["air", "oxygen"]:
        print("You did not give a valid type for oxygen or air!")
        return False
    
    # Ensuring the spO2 level is a number
    try:
        spO2 = int(spO2)
    except ValueError:
        print("You did not give your SpO2 as a whole number!")
        return False
    
    # Checking for return 0 case
    if (airOrOxygen == "air" and spO2 >= 93) or (airOrOxygen == "oxygen" and 88 <= spO2 <= 92) or (airOrOxygen == "air" and 88 <= spO2 <= 92):
        return 0
    else:
        # Returning correct air medi score
        if (86 <= spO2 <= 87):
            return 1
        elif (84 <= spO2 <= 85):
            return 2
        elif spO2 <= 83:
            return 3
        
        # Returning correct oxygen medi score
        if airOrOxygen == "oxygen":
            if (93 <= spO2 <= 94):
                return 1
            elif (95 <= spO2 <= 96):
                return 2
            elif spO2 >= 97:
                return 3
        
# Function to check patient temperature
def check_patient_temperature(temperature):

    # Checking the user has given a number input and making it 1 dp
    try:
        temperature = float(temperature)
        temperature = round(temperature, 1)
    except ValueError:
        print("You did not give your temperature as a whole number!")
        return False
    
    # Returning the correct medi score based off the user input
    if (36.1 <= temperature <= 38.0):
        return 0
    elif (35.1 <= temperature <= 36.0) or (38.1 <= temperature <= 39.0):
        return 1
    elif temperature >= 39.1:
        return 2
    elif temperature <= 35.0:
        return 3
    
# Function to return the final medi score based off the user's inputs
def get_score_main(airOrOxygen, consconsciousness, respirationRate, spO2, temperature):

    # List which holds all the medi scores from the functions / any wrong inputs
    patient_values = [
        check_patient_breath(airOrOxygen),
        check_patient_consciousness(consconsciousness),
        check_patient_respiration_rate(respirationRate),
        check_patient_spO2(airOrOxygen, spO2),
        check_patient_temperature(temperature)
    ]

    # Variable for final medi score
    total_medi_score = 0

    # Checking if any functions have returned a fault
    for value in patient_values:
        if value is False:
            print("One or more of your input values is wrong!")
            return
        else:
            total_medi_score += value

    # Inform user of final medi score as well as return score for any other functions that need it.
    print(f"The final Medi Score for the patient is: {total_medi_score}")
    return total_medi_score

