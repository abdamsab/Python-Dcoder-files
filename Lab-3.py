
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

hrs = (dura // 60)
hrsrmd = dura % 60

hour += hrs
mins +=hrsrmd

print("Event End at: ", hour, ":", mins )