import random
import string

source = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
pw = ''.join(random.choice(source) for i in range(12))
print(pw)


