from parsec import many1, digit, string, try_choice, compose

natural_number = many1(digit()).parsecmap("".join).parsecmap(int)
negative_number = compose(string("-"), natural_number).parsecmap(lambda x: -x)
integer = try_choice(negative_number, natural_number)

# >>> integer.parse("-12")
# ('-', ['1', '2'])