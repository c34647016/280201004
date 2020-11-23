grades = [[50,90,60],[15,60,75],[99,95,91]]
for _ in grades:
  s1 = _[0] * 0.3
  s2 = _[1] * 0.3
  s3 = _[2] * 0.4
totav = (str(s1) + ", " +  str(s2) + ", " + str(s3))
print(totav)