letter = ''' Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Farman").replace("<|Date|>", "16 August 2025"))