class State:
    """
    A state of the game for 'Figure It Out'
    correct: the number of correct attributes
    attempts: the number of attempts made already
    state: the state of the game, representing chosen attributes.
    """
    def __init__(self, correct, attempts, state):
        self.correct = correct
        self.attempts = attempts
        self.state = state
    
    def get_actions(self):
        """Generate possible actions or next states."""
        # Implement algorithm here 
        # Can use Minimax to get future states, but we wont know if they are correct
        # Can do KNN to get the closest state, but again same problem
        # We need to enter a state into the system and get how many attributes are correct
        return [State(self.correct, self.attempts + 1, self.state)]

    def get_utility(self):
        """Define a utility function for game end states."""
        if self.correct == 4:
            return 100  # High utility for game completion
        elif self.correct == 0:
            return 50 # if no correct, we can eliminate all the attributes
        elif self.correct == 1:
            return 30 # little better than 2 correct, so we can find which one is actually correct
        elif self.correct == 2:
            return 20 # hard to find the correct one

    def nextstate(currentstate):
        if currentstate.correct == 4:
            print("You have completed the game")
            return currentstate
        else:
            correct = int(input("Enter the number of correct attributes: "))
            attempts = currentstate.attempts + 1
            # Check if the correct input is valid
            while True:
                state = input("Enter the state of the game: ")
                if len(state) == 4 and all(c in {'0', '1', '2', '3'} for c in state):
                    break 
                else:
                    print("Error! Enter a valid state")
            return State(correct, attempts, state)
            
def main():
    currentstate = State(0, 0, 0) # initial state
    while currentstate.correct != 4:
        currentstate = State.nextstate(currentstate)
        print(f"Correct: {currentstate.correct}, Attempts: {currentstate.attempts}, State: {currentstate.state}")

if __name__ == "__main__":
    main()