import subprocess
import sys
#firstIP = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE).stdout.decode()
#p1 = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
#oldip = p1.stdout.decode()


def publish(username, password):
    p2 = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
    newip = p2.stdout.decode()
    subprocess.call(['./publishIP', '-$newip', '-$username', '-$password'])

if __name__ == '__main__':
    publish((sys.argv[1]),(sys.argv[2]))
