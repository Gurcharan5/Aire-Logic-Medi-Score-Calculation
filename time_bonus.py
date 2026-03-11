# Importing datetime which will be used to compare two times
from datetime import datetime, timedelta

# Function to compare two medi scores based off time
def compare_medi_scores(oldScore, oldTime, newScore, newTime):

    # Ensuring the user has given a correct time format
    try:
        oldTime  = datetime.strptime(oldTime, "%d/%m/%Y %H:%M")
        newTime = datetime.strptime(newTime, "%d/%m/%Y %H:%M")
        timeDifference = abs(newTime - oldTime)
    except ValueError:
        print("Your time inputs are not the correct format!")
        return

    # Ensuring the user has given integers for old and new medi scores
    try:
        oldScore = int(oldScore)
        newScore = int(newScore)
    except ValueError:
        print("Your medi scores were not given as numbers!")
        return

    # Checking if there is under 24 hours between the two times
    if timeDifference >= timedelta(hours=24):
        print("24 hours exceeded, no flag required.")
    else:
        # Checking if there is a large enough difference between readings
        scoreDifference = newScore - oldScore
        if scoreDifference > 2:
            print("There is a large difference between reading, please investigate further!")
        else:
            print("There is no large fluctuation within the last 24 hours, no flag required.")

    