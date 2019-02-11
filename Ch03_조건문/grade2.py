score = 75

if score < 60:
    grade = 'F'
else:
    if score < 70:
        grade = 'C'
    else:
        if score < 80:
            grade = 'B'
        else:
            if score < 90:
                grade = 'A'
            else:
                grade = 'A+'

print('당신의 학점은 ',grade)

