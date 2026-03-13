# Aire Logic Medi Score Calculation

## Basic overview
This project has been coded using Python. The main function of the program (air or oxygen, consciousness, respiration rate, spO2 and temperature) are all handled within `main.py`. The capillary blood glucose bonus is within `capillary_bonus.py` and the trend alerts is within `time_bonus.py`. Within `tests.py`, I have tested the functionality of each solution, testing example cases, valid cases as well as invalid cases. Within `user_interact.py`, users can input information which is then handled by the main.py functions and main functions. You can use this program to test the functionality or interact with specfic methods directly.

# How to run
1. You will need a Python installation of 3.8+. You can download and install Python from https://www.python.org/downloads/ 
2. Download the repisitory and its files using pip or the GitHub website.
3. Run IDLE or any preffered IDE and locate the downloaded files
4. Use `user_interact.py` to run a medi score calculation or read through `main.py` to understand my implementation.

# How to use 
1. When running `user_interact.py` you will be asked to give an answer for each relevant section of the medi score.
2. You will be asked to give your answers in a certain way, either as a number or in the values stated in '  '
3. You will be notified of any invalid inputs at the end.
4. You can run the program again if you wish to input a new medi score or correct the values from your last run.

# Main functions
## main.py
- Classes are used to handle enums for 'air or oxygen' and 'patient consciousness'. This is done so interaction is much more straightforward and users don't have to remember what input values 1 or 0 correspond to.
- Each property is calculated using a separate function with a main `get_score_main` function which will calculate and output a final Medi Score as long as the inputs are valid.
- Each function has its own validation and sanitisation of inputs embedded within `try except` blocks to inform users of any invalid inputs.

## capillary_bonus.py
- The capillary blood glucose calculations are carried out by a separate function, and an adaptation of the `get_score_main` is done within `get_score_capillary_bonus` to accomodate for this.
- To remove the code and improve the system, having `get_score_main` return the final Medi Score would mean I can just call it and add on the capillary blood glucose score, although this does come with the downside of returning a 0 score string.

## time_bonus.py
- To compare two results, the user will have to input an old score, the time the old score was taken as well as the new score and the time the new score was taken. The two times are then compared and if the difference is under 24 hours, the function tests to see if there was a large fluctuation.
- In a real world scenario, this would most likely be run alongside the `main.py` and would be saved alongside the current time in a database. When the user clicks submit, `time_bonus.py` would be improved to take the current time, then be automatically run to flag any issues depending on the time of the previous record. This functionality has been tested within `user_interact.py` where it asks for the previous Medi score and time and compares it to the new Medi score and current time.

## tests.py
- Within this program, I run tests on my functions which includes correct cases and incorrect cases. The purpose of this is to demonstrate the input sanitisation within each function and to show the program will not break if the user gives an invalid input.
- There are screenshots of each test running in /Test_Screenshots to show the app functioning as intended.

## user_interact.py
- In my implementation for `user_interact.py`, inputs are also taken for the bonus questions, so the whole system can be tested including capillary blood glucose and alerting for trends. `user_interact.py` uses the current system time to input the new time as the new medi score is generated based off the user's inputs.
- This can be adapted to remove the bonus questions section of the program and adjusting the final call. You would have to add `from main import get_score_main` and adjusting the final function call to `get_score_main(airOrOxygen, alertOrCVPU, respirationRate, SpO2, temperature)`

# Other implementations
- Another way to develop this function could also be to include a class. In a case where there is more than just the final medi score needing to be saved, storing patients as a class would be a better implementation.
- Using a class would remove the `patient_values` array list and would require implementation of get methods.
- Having a GUI interface would also remove the need for input sanitisation as you would be able to implement drop down menus for the enums, and limit the other fields to just integer / float inputs. This would help clean up the code and remove redundant code. It would also mean I can remove the print statements entirely and simply return a value.
- Storing records in a database such as a MySQL or Supabase would allow real world testing (such as automatically comparing the new and old medi scores).
- Taking JSON inputs could also be implemented as this would align with the program being run server side and taking requests when a user presses submit. It could also mean the medi score is part of a large patient details program (one which may also take details such as diet or fitness), but is able to only take the parts necessary to get the medi score.
## Why I didn't implement these
The main reason was due to this being a function writing technical exercise rather than a fully working implementation. The solution I have developed is designed to be back end functionality that can either be embedded into the app or run server side. I have attempted to show how a user may interact with the program in a production setting through my use of taking user inputs and sanitising them, although I did not go to the extent of developing a GUI and database application.

# Limitations in solution
- Due to the table being incomplete for the spO2% on the left side of 0 and not specifying whether it related to oxygen or air, I made the assumption that values below 87% for both air and oxygen have the same medi score value.
- In the capillary blood glucose bonus section, 4.5 for CBG (2 hours after fasting) has both scores 2 and 3. In my code I made the assumption that 4.5 gives a value of 2 and values lower is 3.

