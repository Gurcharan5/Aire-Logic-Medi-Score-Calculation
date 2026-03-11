# Importing final score functions from the other projects
from main import get_score_main
from capillary_bonus import get_score_capillary_bonus
from time_bonus import compare_medi_scores
from user_interact import user_interact

#
# Screenshots of tests can be found in /Test_Screenshots and correspond to the 
# number besides the test
# Github example patients (1)
# Main function
#

# PATIENT 1
get_score_main("air", "alert", 15, 95, 37.1)

# PATIENT 2
get_score_main("oxygen", "alert", 17, 95, 37.1)

# PATIENT 3
get_score_main("oxygen", "CVPU", 23, 88, 38.5)

#
# Testing incorrect inputs
# Main function (2)
#
print("\n")
# Incorrect air or oxygen
get_score_main("pizza", "alert", 15, 95, 37.1)

# Incorrect alertness
get_score_main("air", "pizza", 15, 95, 37.1)

# Incorrect respiration
get_score_main("air", "alert", "pizza", 95, 37.1)

# Incorrect SpO2
get_score_main("air", "alert", 15, "pizza", 37.1)

# Incorrect temperature
get_score_main("air", "alert", 15, 95, "pizza")

#
# Testing correct inputs
# Capillary bonus (3)
#
print("\n")
get_score_capillary_bonus("air", "alert", 15, 95, 37.1, 5.0, "fasting")

#
# Testing incorrect inputs
# Capillary bonus (4)
#
print("\n")
# Invalid blood glucose 
get_score_capillary_bonus("air", "alert", 15, 95, 37.1, "pizza", "fasting")

# Invalid fasting period
get_score_capillary_bonus("air", "alert", 15, 95, 37.1, 5.0, "pizza")

#
# Testing correct inputs
# Time bonus (5)
#
print("\n")
# 24 hours between tests
compare_medi_scores(14, "14/04/2026 14:50", 15, "15/04/2026 14:50")

# < 24 hours between tests no flag required
compare_medi_scores(14, "14/04/2026 14:50", 15, "14/04/2026 13:50")

# < 24 hours between tests flag required
compare_medi_scores(14, "14/04/2026 14:50", 18, "14/04/2026 13:50")

#
# Testing incorrect inputs
# Time bonus (6)
#
print("\n")
# Invalid old medi score
compare_medi_scores("pizza", "14/04/2026 14:50", 15, "15/04/2026 14:50")

# Invalid new medi score
compare_medi_scores(14, "14/04/2026 14:50", "pizza", "15/04/2026 14:50")

# Invalid old time
compare_medi_scores(14, "pizza", 15, "15/04/2026 14:50")

# Invalid new time
compare_medi_scores(14, "14/04/2026 14:50", 15, "pizza")

#
# Testing user interact
# Correct inputs (7)
# I am using the main function to get the score and not the bonus methods although the 
# code can be easily adapted to work with that method too.
# I will not have to test incorrect inputs as the same methods are being run as before
# from main and they have already been tested as working
#
print("\n")
user_interact()
