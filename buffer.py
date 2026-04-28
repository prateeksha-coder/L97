import random
trials = 1000
success = 0

for i in range(trials):
    if random.choice(['Red', 'Blue', 'Green']) == 'Red':
        success += 1

print("Experimental Probability:", success / trials)