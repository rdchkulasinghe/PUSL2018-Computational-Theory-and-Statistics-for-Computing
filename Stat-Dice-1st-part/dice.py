# dice 1st part
def count_combinations(n_dice, target_sum):
    """
       This function does something.

       Args:
           n_dice: The number of dice using.
           target_sum: The target value of sum.

       Returns:
           The count of the all favourable outcomes
       """
    if n_dice == 0:
        return 1 if target_sum == 0 else 0
    count = 0
    for i in range(1, 7):
        count += count_combinations(n_dice-1, target_sum-i)
    return count


favorable_outcomes = count_combinations(10, 30)
probability = favorable_outcomes / 6**10   # probability of favourable all outcomes of getting sum 30

unfavorable_outcomes = 6**10 - favorable_outcomes
un_fav_probability = unfavorable_outcomes / 6**10  # probability of having unfavourable outcomes.

sum_of_all_probabilities = probability + un_fav_probability  # probabilities sum of favourable and unfavourable


print("Answer: ")

# 10 dice throws add up to sum of 30
print("All outcomes 6^6: ", 6**10)
print(f"The all favourable outcomes: {favorable_outcomes}")
print(f"The Probability of getting sum 30 : {probability}")

print()  # a blank line

# extra details
print(f"All unfavourable Outcomes: {unfavorable_outcomes}")
print(f"The probability of not getting 30 sum: {un_fav_probability}")

print()  # a blank line

print(f"Sum of probabilities: {sum_of_all_probabilities}")  # 1