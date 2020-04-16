import time
time = int(time.time())
hr = time//3600
minutes = (time%3600)//60
sec = ((time%3600)%60)//60

hr_cur = hr%24-6
print("Current time is", hr_cur,":", minutes, "CST")
