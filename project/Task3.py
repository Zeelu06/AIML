scorenew = []
scores = [45, 82, 91, 38, 76, 55, 91, 60, 82, 100]

for score in scores:
    if score not in scorenew:
        scorenew.append(score)

print(scorenew)
def secondhighest():
    s1h = max(scorenew)
    scorenew.remove(s1h)
    s2h = max(scorenew)
    print("Second highest score:", s2h)

secondhighest() 
scorenew = scorenew[:2] + [70] + scorenew[2:]
print(scorenew)
rev_score = scorenew[::-1]
print(rev_score)
print(scorenew)
