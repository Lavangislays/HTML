maths_score = 80
science_score = 90
ela_score = 75




# Students who got more that 75 in maths, eligible for maths olimpiad
# for maths score less than 75 and > 60, eligible to reappear for exam to try again for maths olimpiad


if maths_score > 75:
    print("You are eligible for maths olypiad")
elif maths_score < 75 and maths_score > 60:
    print("reappear for the exam in one week and apply again")
else:
    print("You are not eligible")
