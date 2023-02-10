from TuringMachine import TuringMachine

# Open the Turing Machine M = (Q, Σ, Γ, δ, q0, #, F) as a dictionary from a file
def openFile (fileName):
    file = open(fileName, 'r').read()
    return eval(file)

TM_dict = openFile('TM_3a.dat')

# Ask user to enter the input string
input_str = str(input('Please provide the input string: '))
flag = True
for i in range(len(input_str)):
    if not(input_str[i] in TM_dict['Sigma']):
        flag = False
        break

# If the input characters match the 
if flag:
    M = TuringMachine(TM_dict, input_str)
    M.run(100000)
else:
    print('The character',input_str[i],'is not in the alphabet')
