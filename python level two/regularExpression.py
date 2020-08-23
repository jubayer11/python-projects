import re

patterns = ['term1','term2']
text = 'This is string with term1, not the other1'

for pattern in patterns:
    print("I'm searching for: "+pattern)
    if re.search(pattern,text):
        print("Match")
    else:
        print("No Match")
#Another way

match = re.search('term1',text)
print(type(match))
print(match.start())

spilt_term = '@'

email = 'user@gmail.com'

print(re.split(spilt_term,email))
#another way

print(re.findall('match','test phrase match in match middle'))

def multi_re_find(patterns,pharase):
    for pat in patterns:
        print("searching for patterns {}".format(pat))
        print(re.findall(pat,pharase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...ssssss...sddddd'
test_phrase1 = 'This is a string! But is has punctuation. How can we remove it?'
test_phrase1 = 'This is a string with number 123456'



test_patterns = ['[^!.?]+'] #those symbol
test_patterns = ['[A-Z]+'] #capital letter
test_patterns = [r'\d+'] #digit
test_patterns = [r'\D+'] #non digit
test_patterns = [r'\s+'] #white space
test_patterns = [r'\S+'] #non white space
test_patterns = [r'\w+'] #alpha Numeric
test_patterns = [r'\W+'] #alpha Numeric








multi_re_find(test_patterns,test_phrase)
multi_re_find(test_patterns,test_phrase1)

