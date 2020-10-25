#If I leave my house at 6:52 am and run 1 mile at an easy pace (8 minutes per mile), then 3 miles at tempo (6 minutes per mile)and 2 mile at easy pace again, what time do I get home for breakfast?

left_house = 412
easy_pace = 8
tempo = 6 
total= 3*easy_pace+3*tempo
oclock=((left_house+total)//60)
minutes=left_house+total-oclock*60
print(oclock,":",minutes)