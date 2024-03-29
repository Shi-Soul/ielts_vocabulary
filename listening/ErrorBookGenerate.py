import datetime
import os
from pprint import pprint

#get file from last commit
# Files = os.("git diff --name-only HEAD HEAD^").read().split("\n")
Files = os.popen("git diff --name-only HEAD HEAD^^^^").read().split("\n")
    # 在windows中, ^是转义符, 要想敲一个^, 需要敲^^
# pprint(Files)
#get time as MONTH-DAY
time = datetime.datetime.now().strftime("%m%d%H")
for file in Files:
    # print("DEBUG: ", file, file.startswith("listening/test"), os.path.exists(file))
    if(os.path.exists(file) and file.startswith("listening/test")):
        filename = os.path.basename(file)
        print(filename)
        os.system(f"@fc /w /c /l /n listening\\ref\\{filename} listening\\test\\{filename} > listening\\err\\{filename}.{time}.txt")
        # os.system(f"fc /w /c /l /n listening/ref/{filename} listening/test/{filename} > listening/err/{filename}.{time}.txt")
# os.system(f"git add err && git commit -m \"update {time}'s error books\" && git push")
