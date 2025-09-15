import re
pattern=r"Hello"
text="Hello World"
print(bool(re.match(pattern,text)))

import re
pattern=r"Hello"
text="World Hello"
print(bool(re.search(pattern,text)))