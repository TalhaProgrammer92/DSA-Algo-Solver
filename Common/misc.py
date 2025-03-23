def line(symbol: str, times: int) -> str:
    """ Symbol multiplier to create a line """
    return symbol * times

def input_in_range(range: tuple | list, input_value) -> bool:
    """ To check if the input is in range or not
     Return True if the input in range otherwise False
     """

    return input_value in range