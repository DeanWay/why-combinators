import Control.Applicative (Alternative (some, (<|>)))
import Text.Parsec.Char (digit, string)
import Text.Parsec.String (Parser)

oneOrMore = some

joint p1 p2 = (++) <$> p1 <*> p2

naturalNumber :: Parser String
naturalNumber = oneOrMore digit

negativeNumber = string "-" `joint` naturalNumber

integer = negativeNumber <|> naturalNumber

realNumber = integer `joint` string "." `joint` naturalNumber

number = realNumber <|> integer