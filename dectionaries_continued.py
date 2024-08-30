work = { 
    "Monday" : 2, "Tueday" : 3, "Wednesday" : 4, "Thursday" : 5, "Friday" : 6,}

work["Saturday"] = 7
meep = work.pop("Wednesday")
print(len(work))
if "Friday" in work:
    print("i worked friday")