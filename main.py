import numpy as np

def main():
    MAX_LENGTH: int = 20
    numbers: np.ndarray = np.zeros((MAX_LENGTH, MAX_LENGTH), dtype=int)

    for field_goal in range(1, MAX_LENGTH):
        numbers[field_goal, 0] = numbers[field_goal - 1, 0] + 3

    for touchdown in range(1, MAX_LENGTH):
        numbers[0, touchdown] = numbers[0, touchdown - 1] + 6

    for touchdown in range(1, MAX_LENGTH):
        prev_touchdown: int = touchdown - 1
        for field_goal in range(1, MAX_LENGTH):
            numbers[field_goal, touchdown] = numbers[field_goal, prev_touchdown] + 6

    print(numbers)

if __name__ == "__main__":
    main()
