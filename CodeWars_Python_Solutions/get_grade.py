
# Numerical Score Letter Grade
# 90 <= score <= 100  'A'
# 80 <= score < 90    'B'
# 70 <= score < 80    'C'
# 60 <= score < 70    'D'
# 0 <= score < 60 'F'

def get_grade(s1, s2, s3):
    mean_grade = (s1 + s2 + s3) / 3

    if mean_grade >= 90:
        return 'A'
    elif mean_grade >= 80:
        return 'B'
    elif mean_grade >= 70:
        return 'C'
    elif mean_grade >= 60:
        return 'D'
    else:
        return 'F'

get_grade(90,80,60)
