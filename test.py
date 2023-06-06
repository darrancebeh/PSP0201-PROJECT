import string;
import random;

refGen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5));

print(refGen)