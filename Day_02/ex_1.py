# Daily Workout --> Fitness Streak

work_log = [1, 1, 1, 0, 1, 1, 0]
longest_streak = 0
current_streak = 0
# for loop including if, else
for day in work_log:
    if day == 1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(longest_streak)
