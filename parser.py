from parsec import many1 as one_or_more, digit, string, try_choice, joint

natural_number = one_or_more(digit())
negative_number = joint(string("-"), natural_number)
integer = try_choice(negative_number, natural_number)
real_number = joint(integer, string("."), natural_number)
number = try_choice(real_number, integer)

# >>> number.parse("-12")
# ('-', ['1', '2'])