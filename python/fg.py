maths = 80
science = 90
english = 75



avg = (maths + science + english) / 3


if avg >= 90:
    grade = "A+"
elif avg >= 85:
    grade = "A-"
elif 75 < avg < 85:
    grade = "B"
else:
    grade = "C"

print(f"Based on ypur score, your grade is : {grade}")