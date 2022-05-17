# Test Plan 
___

### Requirements

##### Functional
1. The program will check a Social Security Number based on the format rules, can be found in (Insert Link).
2. The program will allow as many validations as the user wants, in a single execution of the program.
3. The program needs to revise the entered Social Security Number before checking it, to avoid letters and special characters.

##### Non-Functional
1. Needs to deliver a clear output of the result
2. Adapts if any change in rules may appear in the future
3. Runs in short periods

### Criteria
**The program will check a Social Security Number (SSN) based on the format rules.**

- *Scenario*: Validate a Social Security Number
- *Given*: The user have supplied a valid input
- *When*: The user sends a SSN by pressing enter
- *Then*: The system will return the corresponding confirmation

**The program will allow as many validations as the user wants, in a single execution of the program**

- *Scenario*: Validate the repetition of the program
- *Given*: The user received the message of validation, and the system display: "Do you want to leave the program?"
- *When*: The user answers 'n'
- *Then*: The system will start over again and allow another validation

- *Scenario*: Validate the repetition of the program
- *Given*: The user received the message of validation, and the system display: "Do you want to leave the program?"
- *When*: The user answers 'y'
- *Then*: The system will end the program execution.

**The program needs to revise the entered Social Security Number before checking it, to avoid letters and special characters.**

- *Scenario*: Validate the entered input
- *Given*: The user shows the message: "Enter the Social Security Number: "
- *When*: The user supplies any input containing a letter
- *Then*: The system will revise this value and repeats the process all over again until it receives a correct value to validate

- *Scenario*: Validate the entered input
- *Given*: The user shows the message: "Enter the Social Security Number: "
- *When*: The user supplies any input containing a special character, different from the hyphen.
- *Then*: The system will revise this value and repeats the process all over again until it receives a correct value to validate

### Test Environment
The following tests will be executed with unittest python native package in the 3.9 version, analyzing the two main components of the system: *check* function and *string_validation* function. 

### Test Cases

| Test Name  | Component  | Description| Input  | Expected Result  | Test Result  |
|:---:|---|---|---|---|:---:|
| test01  |  check | Validates the 1st part has 3 digits  | 12-56-9715  | False  |   |
| test02  |  check | Validates the 2nd part has 2 digits  | 137-1-8468  | False  |   |
| test03  | check  | Validates the 3rd part has 4 digits  | 198-65-13  | False  |   |
| test04  | check  | Validates the 1st section is not 000  | 000-51-3854  | False  |   |
| test05  | check  | Validates the 1st section is not 666  | 666-17-3546  | False  |   |
| test06  | check  | Validates the 1st section is not between 900 or 999  | 943-34-1389  | False  |   |
|test07| check| Validates the 2nd section is between 01 and 99|123-00-4683 |False | |
|test08 |check |Validates the 3rd section is between 0001 and 9999|123-09-0000 |False | |
|test09 | check |Validates a Social Security Number |357-54-9878 |True | |
| test10 | string_validation  | Validates the number doesn't have a non-hyphen symbol  | 13?-48-118/  | False  |   |
| test11 | string_validation  | Validates the number doesn't have 9 digits  | 12-5-384  | False  |   |
| test12  | string_validation | Validates the number doesn't have letters  | 159-w4-3848  | False  |   |
| test13  | string_validation | Validates the number have 9 digits  | 123-45-6789  | True  |   |