# User Manual
___

### What the app does?

This Python programs allows a person to validates the format of a specific Social Security Number(SSN).

The correct format of a Social Security Number follows the next rules:

- It should have 9 digits.
- It should be divided into 3 parts by hyphen (-).
	- The first part should have 3 digits and should not be 000, 666, or between 900 and 999.
	- The second part should have 2 digits and it should be from 01 to 99.
	- The third part should have 4 digits and it should be from 0001 to 9999.
	
**Only if the entered SSN satisfy all these rules, it'll be confirmed as valid.**

### How to use the app

Before everything, you need to be able to execute the program. If you haven't, check the ReadMe file at the start to get you started properly.

With everything set, when you run the app you'll see the title of the application and the following statements:

**Enter the Social Security Number you want to validate:**

Right next to it, you write the Social Security Number you wish.

Please check the following while entering your Social Security Number:
* Don't include special characters, besides the hyphen
* Don't include any letter
*  The first part should have 3 digits and should not be 000, 666, or between 900 and 999.
* The second part should have 2 digits and it should be from 01 to 99.
* The third part should have 4 digits and it should be from 0001 to 9999.

Then, the program will show a message to confirm or deny correctness of the specified number being:  "This Social Security Number is correct" or "The number is not valid", based on similar rules as listed before.

After the message is shown, a question will appear, saying: "Do you want to leave the program? (y/n)". This only responds to the letter *y* or *n*, the first will exit the program and the second will restart it. If any other value is specified, the message will appear: "An invalid option was supplied, please try again", and inmediatly will reappear the initial question until a proper answer is provided.

### Install Python in Ubuntu

Ubuntu 20.04 and other Debian Linux distributions are shipped with the Python 3 installed by default. You can confirm if python is available by using the below command.

`python3 -V`

You’ll see the python version installed as below.

`Python 3.8.2`

If it’s not installed, you can install Python3 on Ubuntu by using the following command.

`sudo apt install python3.9`

If you want to install a different version of Python, you can update the version number by changing the version at the install script.



### How to run the application in Ubuntu

You can pass the arguments to python from the Linux command line by specifying the argument’s value next to the commands. If you have two or more commands, you can separate them with the space.

Use the below command to pass var1, var2 to the python script file IntegerToRomanConverter.py.

`python3 IntegerToRomanConverter.py var1 var2`

Now, your program will accept this command-line argument and process it as defined in the script.

For more information, visit this site: https://www.stackvidhya.com/run-python-file-in-terminal/

### How to run the UnitTests

To execute the tests described in the DecimalToRoman - TestCases.md file, go to (insert link when available), it's only required to follow a similar process to run the application, described in the previous section, as it runs with a built-in python package.

Only need to execute the next command: 

`python3 UnitTest.py`