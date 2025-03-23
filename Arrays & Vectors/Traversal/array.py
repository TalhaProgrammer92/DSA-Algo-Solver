class Solution:
    @staticmethod
    def traverse(array: list) -> None:
        """ Array traversal algorithm """
        for index, element in enumerate(array):
            print(f"The array contains '{element}' (type: {type(element).__name__}) at index {index} <- array[{index}]")

def detect_type(value: str):
    """ Detects and converts the input to int, float, or keeps it as a string """
    try:
        if "." in value:
            return float(value)  # Convert to float if it contains a decimal
        return int(value)  # Convert to int if no decimal
    except ValueError:
        return value  # Keep as string if conversion fails

def main() -> None:
    """ The main part of the program """
    array = []

    # Take input
    size = int(input('How many elements do you want to enter? '))

    # Enter numbers/elements to array
    for count in range(size):
        value = input(f'Enter element #{count+1}: ')
        array.append(detect_type(value))  # Auto-detect type

    # Solution
    Solution.traverse(array)

    # Time Complexity
    print("\nTime Complexity: O(n) (Linear Time) - Because we traverse the array once.")

if __name__ == '__main__':
    main()
