# Import dependencies
import string
import random





# Id Unique GENERATOR
def randomSEC_KEY(chars: str = string.ascii_uppercase + string.digits, length=16):
    # Generate a random string of the specified length using characters from 'chars'
    result = ''.join(random.choice(chars) for _ in range(length))
    return result

# Id Unique GENERATOR
def randomSEC_KEY_reqs(chars: str = string.ascii_uppercase + string.digits, length=6):
    # Generate a random string of the specified length using characters from 'chars'
    result = ''.join(random.choice(chars) for _ in range(length))
    return result