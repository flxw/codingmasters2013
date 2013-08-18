import sys
import itertools
import threading

def checkGroupSkill(g,l,rl):
    if sum(group) == 100:
        l.acquire()
        rl.append('')
        l.release()

############## main #############################
candidates = []
candidateID = 0

# process data first
for line in sys.stdin:
    try:
        candidates.append(int(line))
    except:
        pass

# traverse list step by step and build groups
amount = 0
lock = threading.Lock()
rl = []
for group in itertools.combinations(candidates, 6):
    t = threading.Thread(None, checkGroupSkill, None, [group,lock,rl])
    t.run()

print len(rl)
