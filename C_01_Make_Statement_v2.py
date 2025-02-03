# Functions go here
def make_statement(statement, decoration, lines):
    """creating headings (3 lines), subheadings (2 lines) and
    emphasised text / mini-headings (1 line). Only user emoji for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main Routine goes here
make_statement("Programming is Fun!", "=", 3)
make_statement("Programing is still fun!", "*", 2)
make_statement("Emoji in action", "😒", 1)
