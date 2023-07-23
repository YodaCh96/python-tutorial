import re

pattern = '[abc]'

# Test Strings
test_string_1 = "a"
test_string_2 = "ac"
test_string_3 = "Hey Jude"
test_string_4 = "abc de ca"

result = re.match(pattern, test_string_1)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	