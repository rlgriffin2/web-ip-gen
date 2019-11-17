import subprocess
#firstIP = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE).stdout.decode()
#p1 = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
#oldip = p1.stdout.decode()
p2 = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
newip = p2.stdout.decode()
#if(oldip~=newip):
#    publish(newip)
subprocess.call(['./publishIP', '-$newip'])
