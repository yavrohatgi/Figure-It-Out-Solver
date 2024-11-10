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


def main():
    """
    Main function to demonstrate getting a correctness score from the user.
    """
    example_state = {1: 1, 2: 1, 3: 1}
    correctness = get_correctness_from_user(example_state)
    print(f"Correctness: {correctness}")


if __name__ == "__main__":
    main()
