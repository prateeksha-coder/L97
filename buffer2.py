import random

def spinner_experiment():
    spinner = ['Win', 'Lose', 'Lose', 'Win', 'Lose']
    
    result = random.choice(spinner)
    
    prob = spinner.count('Win') / len(spinner)
    print("Probability of Winning:", round(prob, 2))
    
    if result == 'Win':
        return 'You Won!'
    else:
        return 'Try Again!'

res = spinner_experiment()
print(res)