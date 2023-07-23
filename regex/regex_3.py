import re

pattern = '[0-39]'

# Test Strings
test_string_1 = "4569"
test_string_2 = "9378956"

result1 = re.match(pattern, test_string_1)
result2 = re.match(pattern, test_string_2)

print(result1)
print(result2)