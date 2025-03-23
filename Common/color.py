class ANSI:
    FOREGROUND = {
        "black": "\033[30m", "red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m",
        "blue": "\033[34m", "magenta": "\033[35m", "cyan": "\033[36m", "white": "\033[37m",
        "bright_black": "\033[90m", "bright_red": "\033[91m", "bright_green": "\033[92m", "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m", "bright_magenta": "\033[95m", "bright_cyan": "\033[96m", "bright_white": "\033[97m"
    }

    BACKGROUND = {
        "black": "\033[40m", "red": "\033[41m", "green": "\033[42m", "yellow": "\033[43m",
        "blue": "\033[44m", "magenta": "\033[45m", "cyan": "\033[46m", "white": "\033[47m",
        "bright_black": "\033[100m", "bright_red": "\033[101m", "bright_green": "\033[102m",
        "bright_yellow": "\033[103m",
        "bright_blue": "\033[104m", "bright_magenta": "\033[105m", "bright_cyan": "\033[106m",
        "bright_white": "\033[107m"
    }

    STYLE = {
        "bold": "\033[1m", "dim": "\033[2m", "italic": "\033[3m", "underline": "\033[4m",
        "blink": "\033[5m", "reverse": "\033[7m", "hidden": "\033[8m"
    }

    RESET = "\033[0m"

    @staticmethod
    def color_text(text: str, fg: str = None, bg: str = None, style: str = None) -> str:
        """Apply ANSI color and style to text."""
        codes = []
        if fg and fg in ANSI.FOREGROUND:
            codes.append(ANSI.FOREGROUND[fg])
        if bg and bg in ANSI.BACKGROUND:
            codes.append(ANSI.BACKGROUND[bg])
        if style and style in ANSI.STYLE:
            codes.append(ANSI.STYLE[style])
        return "".join(codes) + text + ANSI.RESET

if __name__ == '__main__':
    # Example Usage
    print(ANSI.color_text("Hello, World!", fg="red", bg="black", style="bold"))
