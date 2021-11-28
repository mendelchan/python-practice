
def timeConversion(s):
    # Write your code here
    hh=int(s[:2])
    if "PM" in s:
        if hh!=12:
            hh+=12

    if "AM" in s:
        if hh==12:
            hh=00
    
    hour=(str(hh)).zfill(2)
    
    return f"{hour}{s[2:-2]}"


print(timeConversion("01:00:00AM"))
print(timeConversion("01:00:00PM"))

print(timeConversion("11:00:00AM"))
print(timeConversion("11:00:00PM"))

print(timeConversion("12:00:00AM"))
print(timeConversion("12:00:00PM"))