# Importing the main function to make sure medi score can be calculated and time
from capillary_bonus import get_score_capillary_bonus
from time_bonus import compare_medi_scores
from datetime import datetime

# Function to allow users to input their own values into the program
def user_interact():

    # Main function inputs
    print("Is the patient breathing 'air' or 'oxygen'?")
    airOrOxygen = input()

    print("Is the patient 'alert' or 'CVPU'?")
    alertOrCVPU = input()

    print("What is the patient's respiation rate as a number?")
    respirationRate = input()

    print("What is the patient's SpO2 as a number?")
    SpO2 = input()

    print("What is the patient's temperature as a number?")
    temperature = input()

    # Bonus question inputs
    print("What is the patient's capillary blood score?")
    capillary_blood = input()

    print("Is the patient 'fasting' or is this '2-hours' post eating?")
    fasting = input()

    print("What was the patient's last medi score?")
    lastScore = input()

    print("When was the last test taken (day/month/year hour:minute)?")
    lastTime = input()

    # Taking current time for new time to check if 24 hours passed
    currentTime = datetime.now()
    formattedCurrentTime = currentTime.strftime("%d/%m/%Y %H:%M")

    # Final function call
    compare_medi_scores(lastScore, lastTime, get_score_capillary_bonus(airOrOxygen, alertOrCVPU, respirationRate, SpO2, temperature, capillary_blood, fasting), formattedCurrentTime)


    
