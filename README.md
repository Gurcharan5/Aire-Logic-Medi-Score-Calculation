# Aire Logic Medi Score Calculation

## Basic Overview
This project has been coded using Python. The main function of the program (air or oxygen, consciousness, respiration rate, spO2 and temperature) are all handled within `main.py`. The capillary blood glucose bonus is within `capillary_bonus.py` and the trend alerts is within `time_bonus.py`. Within `tests.py`, I have tested the functionality of each solution, testing example cases, valid cases as well as invalid cases. Within `user_interact.py`, users can input information which is then handled by the main.py functions and main functions. You can use this program to test the functionality or interact with specfic methods directly.

# Main Takeaways

## main.py
- Classes are used to handle enums for 'air or oxygen' and 'patient consciousness'. This is done so interaction is much more straightforward and users don't have to remember what input values 1 or 0 correspond to.
- Each property is calculated using a separate function with a main `get_score_main` function which will calculate and output a final Medi Score as long as the inputs are valid.
- Each function has its own validation and sanitisation of inputs embedded within `try except` blocks to inform users of any invalid inputs.

## capillary_bonus.py
- The capillary blood glucose calculations are carried out by a separate function, and an adaptation of the `get_score_main` is done within `get_score_capillary_bonus` to accomodate for this.
- To remove the code and improve the system, having `get_score_main` return the final Medi Score would mean I can just call it and add on the capillary blood glucose score, although this does come with the downside of returning a 0 score string.

## time_bonus.py
- To compare two results, the user will have to input an old score, the time the old score was taken as well as the new score and the time the new score was taken. The two times are then compared and if the difference is under 24 hours, the function tests to see if there was a large fluctuation.
- In a real world scenario, this would most likely be run alongside the `main.py` and would be saved alongside the current side in a database. When the user clicks submit, `time_bonus.py` would be improved to take the current time, then be automatically run to flag any issues.

## tests.py
- Within this program, I run tests on my functions which includes correct cases and incorrect cases. The purpose of this is to demonstrate the input sanitisation within each function and to show the program will not break if the user gives an invalid input.
- There are screenshots of each test running in /Test_Screenshots to show the app functioning as intended.

## user_interact.py
- In my implementation for `user_interact.py`, inputs are also taken for the bonus questions, so the whole system can be tested including capillary blood glucose and alerting for trends. `user_interact.py` uses the current system time to input the new time as the new medi score is generated based off the user's inputs.
- This can be adapted to remove the bonus questions section of the program and adjusting the final call. You would have to add `from main import get_score_main` and adjusting the final function call to `get_score_main(airOrOxygen, alertOrCVPU, respirationRate, SpO2, temperature)`

# Other Implementations
- Another way to develop this function could also be to include a class. In a case where there is more than just the final medi score needing to be saved, storing patients as a class would be a better implementation.
- Using a class would remove the `patient_values` array list and would require implementation of get methods.

