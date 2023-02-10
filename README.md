# Turing-Machine
The first file named ”TuringMachine.py” is the class of Turing Machine. 
The other file is ”TestTM.py”, which is used for reading the input string and the characteristics of the designed Turing Machine.
  
TestTM.py reads the Turing Machine variables from a .dat file and receive the input string as an input for the user. 
Then based on these items, it calls the TuringMachine class and run the designed Turing Machine.

## Turing Machine as an Accepter
First, I run a Turing Machine that can accepts the language L as follows:

![Fig1a](https://user-images.githubusercontent.com/83058686/218005953-efa6bd23-f52e-463e-acbd-81757aafac4a.PNG)

We save the above Turing Machine variables in TM_1a.dat file, and load it in our Python code as a dictionary.
Running the code for different input strings shows that our Turing Machine works well and halts in a 
final states for all strings in L and it halts in a nonfinal state for all strings that does not belong to L.

Then we try the following language for Turing machine programming:  
*The language is wwR and where the string (wwR) is even.*
  
We solved the problem with the following steps:  
Step 1: Starting at the leftmost character, we check it off by replacing a with x or b with y.  
Step 2: We then let the read-write head travel right to find the rightmost character, which in turn is 
checked off by replacing it with the same symbol that we used to check off the leftmost character.  
Step 3: After that, we go left again to the leftmost a or b.  
Step 4: We repeat the process from Step 1. Traveling back and forth this way, we match each character 
in w with its corresponding character in wR.  
Step 5: If after some time no a’s or b’s remain, then the string must be in L.
  
The above steps can be shown in details in the following transition graph.  
![Fig1b](https://user-images.githubusercontent.com/83058686/218006790-06c03ac3-bdf3-4fbd-8beb-dbce0aa49c39.PNG)

We saved the above Turing Machine in ’TM 1b.dat’ file, and loaded it in our Python code as a dictionary. 
Running the code for different input strings shows that our Turing Machine works well and halts in a 
final states for all strings in L and it halts in a nonfinal state for all strings that does not belong to L.
  
## Turing Machine as a Transducer
First, we consider the following example, which is a Turing Machine that can copy strings of 1’s.  
![Fig2a](https://user-images.githubusercontent.com/83058686/218007171-5d81e018-11e3-4bbe-9c4d-f005ad46cbe7.PNG)
  
We save the above Turing Machine in TM_2a.dat file, and load it in our Python code as a dictionary. 
Running the code for different input strings shows that our Turing Machine can successfully copy a string of 1’s and halts in a final states.

Then we try to solve the problem of addition of two binary numbers. 
We suppose the binary numbers to be added are input to the Turing machine and are separated by a ’+’. 
I could solve the problem in a more straight forward approach if I would use three tapes for the Turing Machine but since I wanted to keep using the simple general Turing Machine, I solved the problem in a heuristic way with the following steps. It is not the fastest approach but it does the task.  
Step 1: Starting at the leftmost character of the first number, we let the read-write head travel right 
to find the rightmost character of the second number.  
Step 2: We then subtract one from the second number, and we go left to the rightmost character of 
the first number.  
Step 3: We add one to the first number and repeat the process from Step 1.  
Step 4: Traveling back and forth this way, we subtract one by one from the second number and add it to the first number accordingly, up to the time that the second number is all zero.  
Step 5: We then delete all the remaining characters of the second number and the ’+’ symbol. The read-write head also travel left to the leftmost character of the result number.  
  
The above steps can be shown in details in the following transition graph.  
![Fig2b](https://user-images.githubusercontent.com/83058686/218007857-85f730bc-b460-4b42-b635-ba22c02efd29.png)

We saved the above Turing Machine in ’TM_2b.dat’ file, and loaded it in our Python code as a dictionary. 
Running the code for different input strings shows that our Turing Machine works well.
  
## Turing Machine for Complicated Tasks
First, we consider the following example, which is a Turing Machine that can multiply two unary numbers.  
![Fig3a](https://user-images.githubusercontent.com/83058686/218008216-f6747f5b-13cb-45b3-b02e-22fee95b809d.PNG)

To implement the approach described in above example, I supposed the binary numbers to be multiplied are input to the Turing machine and are separated by a ’*’.

We save the above Turing Machine in TM_3a.dat file, and load it in our Python code as a dictionary. 
Running the code for different input strings shows that our Turing Machine can successfully multiply two unary numbers and halts in a final states.

Next we try to solve Unary Division. It should be noted that the result of integer division has two parts, the quotient (Q) and the remainder (R), s.t. Dividend = Divisor*Q+R.  
To solve this problem, I supposed the unary numbers to be divided are input to the Turing machine and are separated by a ’/’. 
The following steps describe the designed Turing Machine:  
Step 1: Starting at the leftmost character of the first number (Dividend), we let the read-write head 
travel right to the blank after the rightmost character of the second number (Divisor). We turned that 
blank into character ”Q”.  
Step 2: We then go left to the leftmost 1 of the divisor and change it to x.  
Step 3: We go left again to the leftmost 1 of the dividend and change it to blank.  
Step 4: Traveling back and forth this way, up to the time that there is no 1 in the divisor. We go to 
the blank after the rightmost character after Q and change it to 1.  
Step 5: We go back and change all x in divisor to 1. and restart the iteration from step2.  
Step 6:We iterate the above up to the time that there is no character left in the dividend. So we delete 
the operator ”/” and we change the first character of the divisor to ”R”.  
Step 7: We change all x in the divisor to 1 and we delete all 1 remained in the divisor. And, we move 
the read-write head back to the character R.  
The result is in the form of R-Q-. The number after R is the remainder and the number after Q is the 
quotient. The equation Dividend = Divisor*Q+R stands for the results.
  
The above steps can be shown in details in the following transition graph  
![Fig3b](https://user-images.githubusercontent.com/83058686/218009129-9346ec00-a300-4019-9f95-6ceb1d862cd4.png)
  
I saved the above Turing Machine in ’TM 3b.dat’ file, and loaded it in my Python code as a dictionary. 
Running the code for different input strings shows that the Turing Machine works well. 

