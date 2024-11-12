from typing import TypeAlias


class MasterSolver:
    State: TypeAlias = dict[int, int]

    def __init__(self, num_properties: int = 3, num_values: list[int] = [3]):
        self.history: list[MasterSolver.State] = []
        self.current_guess: MasterSolver.State = {"correctness": 0}
        self.num_properties: int = num_properties
        self.num_values: list[int] = num_values
        self.best_state: MasterSolver.State = {}

    def prompt_correctness_score(self) -> None:
        """
        Prompts the user to provide a correctness score for the current guess
        and sets the correctness score to the current guess.
        """
        print(f"Guess: {self.current_guess}")
        try:
            answer = int(input("Enter correctness score: "))

            if answer > self.num_properties or answer < 0:
                print(
                    "Invalid input. Please enter a number between 0 and the number of properties."
                )
                self.prompt_correctness_score()
            else:
                self.current_guess["correctness"] = answer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            self.prompt_correctness_score()
