import re

# Sample text
text = "123456"

# Define a regex pattern for email
# pattern = r'[a-zA-Z0-9]+@[g]{1}[m]{1}[a]{1}[i]{1}[l]{1}+\.[a-zA-Z]'

#pattern = r'^(?!.*[0-3]).*$'  # except 0 to 3 any letters are applicable 

pattern=r'[^0-3]'

# Search for the pattern in the text
match = re.search(pattern, text)
if match:
    print("thank you")  # Output: Found email: example@example.com
else:
    print("sakkaga kottu ra ayya")
