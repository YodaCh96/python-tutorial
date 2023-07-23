import re

pattern = '^a...s$'

# Test Strings
test_string_1 = "abyss"
test_string_2 = "abs"
test_string_3 = "alias"
test_string_4 = "Alias"
test_string_5 = "An abacus"
test_string_6 = "a   s"

result = re.match(pattern, test_string_1)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
