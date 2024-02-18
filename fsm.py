# DFA Implementation in Python

# 5-tuple collection summarizing the DFA

#seven states
from ast import Pass, main


states = []
alphabets = []
start_state = ""
final_states = []
transition = {}

# Inputs which the DFA will accept/reject
input_states = "start,dot!,11,dash!,0!,00,000!,four0,five0 ,six0,seven0!"
alphabets = "0 1"
start_state = "start"
final_states = ["seven0!"]

dict_char_morse = {
    "a" : ". -",
    "b" : "- . . .",
    "c" : " - . - .",
    "d" : "- . .",
    "e" : ".",
    "f" : ". . - .",
    "g" : "- - .",
    "h" : ". . . .",
    "i" : ". .",
    "j" : ". - - -",
    "k" : " - . -",
    "l" : ". - . .",
    "m" : "- -",
    "n" : "- .",
    "o" : " - - -",
    "p" : ". - - .",
    "q" : "- - . -",
    "r" : ". - .",
    "s" : ". . .",
    "t" : "-",
    "u" : ". . -",
    "v" : ". . . -",
    "w" : ". - -",
    "x" : "- . . -",
    "y" : "- . - -",
    "z" : "- - . .",
    "1" : ". - - - -",
    "2" : ". . - - -",
    "3" : ". . . - -",
    "4" : ". . . . -",
    "5" : ". . . . .",
    "6" : "- . . . .",
    "7" : "- - . . .",
    "8" : "- - - . .",
    "9" : "- - - - .",
    "0" :"- - - - -"
}

#transition map of state + alphabet => state
transition = {
"start 0"   :   "start",
"start 1"   :   "dot",
"dot 1"     :   "11",
"dot 0"     :   "0",
"11 1"      :   "dash",
"dash 0"    :   "0",
"0 0"       :   "00",
"0 1"       :   "dot",
"00 0"      :   "000",
"000 0"     :   "four0",
"000 1"     :   "dot",
"four0 0"   :   "five0",
"five0 0"   :   "six0",
"six0 0"    :   "seven0"
}



class DFA:
    def __init__(self, strStates, strAlphas,strStartState,strFinalStates,dictTransition):
        self.states = self.setStates(strStates)
        self.alphabets = self.setAlphabets(strAlphas)
        self.start_state = self.setStartState(strStartState)
        self.final_states = self.setFinalStates(strFinalStates)
        self.transition = self.setTransition(dictTransition)
        self.current_state = self.start_state

    def setStates(self, strStates: str):
        strStates = strStates.split()
    
    def setAlphabets(self, strAlphas):
        return
    
    def setStartState(self, strStartState):
        return
    
    def setFinalStates(self, strFinalStates):
        return
    
    def setTransition(self, dictTransition):
        return
    
    def getCurrentState(self):
        return
    
    def getInitialState(self):
        return
    
    def getNextState(self):
        return
    
    def current_state_accepting(self):
        return
    
def simplified_max_munch(DFA, characterMap):
    return

def main():

    print("hi")