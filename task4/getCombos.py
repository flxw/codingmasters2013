import sys
import itertools

def calculateSkillLevel(g):
    skill = 0
    for i in g:
        skill += candidates[i]

    return skill
############## main #############################
candidates = {}
candidateID = 0

# process data first
for line in sys.stdin:
    try:
        candidates[candidateID] = int(line)
        candidateID += 1
    except:
        pass

# traverse list step by step and build groups
amount = 0
for group in itertools.combinations(candidates, 6):
    if calculateSkillLevel(group) == 100:
        amount += 1

print amount
