import re
pattern = r"\d"
text = "Hel5lo Wo6rld"
print(re.findall(pattern, text))

import re
pattern = r"\d+"
text = "Hel57lo Wo6rld"
print(re.findall(pattern, text))
