from Common.color import ANSI
from Common.misc import line, input_in_range

class Solution:
    @staticmethod
    def traverse(array: list) -> None:
        """ Array traversal algorithm """
        print('',
            ANSI.color_text(
                line('=', 60),
                'red',
                None,
                'bold'
            ), sep='\n'
        )
        for index, element in enumerate(array):
            a: str = ANSI.color_text(
                f"The array contains '{element}'",
                'green'
            )
            b: str = ANSI.color_text(
                f"(type: {type(element).__name__})",
                'bright_blue',
                None,
                'bold'
            )
            c: str = ANSI.color_text(
                f"at index {index} <- array[{index}]",
                'magenta',
                None,
                "italic"
            )

            print(a, b, c)

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
    while True:
        try:
            size = int(input(
                ANSI.color_text(
                    'How many elements do you want to enter? ',
                    'yellow',
                )
            ))
            break
        except Exception:
            print(
                ANSI.color_text(
                    'Invalid input! Enter a number',
                    'red'
                )
            )

    # Separator
    print(
        ANSI.color_text(
            line('-', 50),
            'red'
        )
    )

    # Enter numbers/elements to array
    for count in range(size):
        value = input(
            ANSI.color_text(
                f'Enter element #{count+1}: ',
                'cyan'
            )
        )
        array.append(detect_type(value))  # Auto-detect type

    # Solution
    Solution.traverse(array)

    # Seperator
    print(
        ANSI.color_text(
            line('=', 60),
            'red',
            None,
            'bold'
        )
    )

    # Time Complexity
    print(
        ANSI.color_text(
            "\nTime Complexity: O(n) (Linear Time) - Because we traverse the array once.",
            'blue',
            None,
            'bold'
        )
    )

if __name__ == '__main__':
    main()
