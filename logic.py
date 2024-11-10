import json

def get_correctness_from_user(current_guess):
    """
    Prompts the user to provide a correctness score for a given guess.
    Args:
        current_guess (dict): The current guess that the user is providing a correctness score for.
    Returns:
        int: The correctness score provided by the user.
    """
    print(f"Guess: {current_guess}")
    try:
        answer = int(input("Enter correctness score: "))
        return answer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def load_states(filename):
    """
    Loads states from a JSON file.
    Args:
        filename (str): Path to the JSON file.
    Returns:
        dict: Dictionary containing the contents of the JSON file.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON.")
        return {}


def brute_force_state_generator(num_properties, num_values):
    """
    Generates the best state by iterating though previous states.
    Args:
        num_properties (int): The number of properties in the state.
        num_values (int): The number of values for each property.
    Returns:
        dict: The best state.
    """
    states_file = load_states("states.json")
    best_state = states_file.get("best_state", {})
    
    state = {}
    for i in range(1, num_properties + 1):
        if best_state[i]:
            state[i] = best_state[i]
        # Iterate through all the states and find constitute the best state
            
    return state


def main():
    """
    Main function to demonstrate getting a correctness score from the user.
    """
    example_state = {1: 1, 2: 1, 3: 1}
    correctness = get_correctness_from_user(example_state)
    print(f"Correctness: {correctness}")
    best_state = brute_force_state_generator(3, 3)
    print(f"Best state: {best_state}")


if __name__ == "__main__":
    main()
