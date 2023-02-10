class TuringMachine:
    # Setting the main varaibles of the Turing Machine
    # The input variables are the dictionary of the Turing Machine and the input string
    def __init__(self, TM_dict, input_str):
        self.Transition = list(TM_dict['Delta']) # Transition functions
        self.State = TM_dict['q0']   # Initial state
        self.Blank = TM_dict['Blank']   # Blank character
        self.FinalStates = list(TM_dict['F']) # Set of final states
        self.SideBlanks = 100  # Number of blnaks in each side of the input string
        # Making the tape
        self.Tape = ''.join([self.Blank]*self.SideBlanks) + input_str + ''.join([self.Blank]*self.SideBlanks)
        # Head is positioned at the leftmost character of the input
        self.Head = self.SideBlanks   
        self.atf = -1 # The number of the applicable transition function


    # Finding the applicable transition function from the set of all transition functions
    def trans(self):
        flag = False # Used to know if the transition function exist

        for self.atf in range(len(self.Transition)):
            sameState = self.Transition[self.atf][0] == self.State
            sameSymbol = self.Transition[self.atf][1] == self.Tape [self.Head]

            if sameState and sameSymbol:
                flag = True
                break

        # If there is no transition function defined
        if flag == False: 
            self.atf = -1


    # Updating the tape, state, and the head in one step based on the transition function
    def tapeupdate(self):
        # Check if the head is on the tape
        if self.Head < 0 or self.Head > len(self.Tape):
            print("The Turing Machine head is out of the tape")
        
        # Update the active state, tape, and the position of the head
        else:
            self.State = self.Transition[self.atf][2]
            self.Tape = self.Tape[:self.Head] + self.Transition[self.atf][3] + self.Tape[self.Head+1:]
            if self.Transition[self.atf][4] == 'R':
                self.Head += 1
            elif self.Transition[self.atf][4] == 'L':
                self.Head -= 1


    # Running the Turing Machine
    # Maximum Iteration is an input variable to prevent infinite loops
    def run(self, maxiteration):
        # Find the applicable transition function
        self.trans()

        # Adding the state to the left side of the string
        UpdatedTape = self.Tape[:self.Head] + self.State + self.Tape[self.Head:]
        print(UpdatedTape.replace(self.Blank, ''))

        i = 0 
        # If there is an applicable transition function 
        # and we are less than maximum iteration we iterate the tape update
        while self.atf >= 0 and i <= maxiteration: 
            self.tapeupdate()
            self.trans()
            UpdatedTape = self.Tape[:self.Head] + self.State + self.Tape[self.Head:]
            print(UpdatedTape.replace(self.Blank, ''))
            i += 1

        # Show if the Turing Machine halted in a final or nonfinal state
        if self.State in self.FinalStates:
            print('The Turing Machine halted in the final state ', self.State)
        else:
            print('The Turing Machine halted in the nonfinal state ', self.State)

        # Show if the Turing Machine is in an infinite loop
        if i == maxiteration:
            print('The Turing Machine did not halt because it is in an infinite loop')

        # Show the output string on the tape
        print('The output string is ', self.Tape.replace(self.Blank, ''))