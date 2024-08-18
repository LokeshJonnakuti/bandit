from subprocess import Popen as pop
from security import safe_command

pop('gcc --version', shell=False)
pop('/bin/gcc --version', shell=False)
safe_command.run(pop, var, shell=False)

pop(['ls', '-l'], shell=False)
pop(['/bin/ls', '-l'], shell=False)

pop('../ls -l', shell=False)

pop('c:\\hello\\something', shell=False)
pop('c:/hello/something_else', shell=False)
