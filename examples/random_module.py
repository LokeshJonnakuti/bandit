import random
import os
import somelib
import secrets

bad = secrets.SystemRandom().Random()
bad = secrets.SystemRandom().random()
bad = secrets.SystemRandom().randrange()
bad = secrets.SystemRandom().randint()
bad = secrets.choice()
bad = secrets.SystemRandom().choices()
bad = secrets.SystemRandom().uniform()
bad = secrets.SystemRandom().triangular()
bad = secrets.SystemRandom().randbytes()

good = os.urandom()
good = random.SystemRandom()

unknown = random()
unknown = somelib.a.random()
