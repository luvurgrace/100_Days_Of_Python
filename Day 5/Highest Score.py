# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

scores = [8, 65, 89, 86, 55, 91, 64, 89, 1]
max_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score
print(max_score)

min_score = scores[0]
for score in scores:
    if score < min_score:
        min_score = score
print(min_score)