total_score = 85
num_subjects = 5

# Logic Bug: Uses integer division (//) instead of float division (/)
average_grade = total_score / num_subjects

print(f"Total Score: {total_score}")
print(f"Calculated Average Grade: {average_grade}")