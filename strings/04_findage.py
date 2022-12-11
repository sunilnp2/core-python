from datetime import date

dob = date(2002,7,8)

t = date.today()

age = t.year - dob.year - ((t.month, t.day)) < ((dob.month, dob.day))

print(age)