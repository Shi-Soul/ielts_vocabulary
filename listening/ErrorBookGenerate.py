import datetime
import os

#get file from last commit
# Files = os.("git diff --name-only HEAD HEAD^").read().split("\n")
Files = os.popen("git diff --name-only HEAD HEAD^").read().split("\n")
print("PWD: ",os.getcwd())
print("Files: ", Files,os.popen("git diff --name-only HEAD HEAD^").read())
#get time as MONTH-DAY
time = datetime.datetime.now().strftime("%m%d%h")
for file in Files:
    if(os.path.exists(file) and file.startswith("listening/test")):
        filename = os.path.basename(file)
        print(filename)
        os.system(f"diff --ignore-space-change -y --suppress-common-lines listening/ref/{filename} listening/test/{filename} > listening/err/{filename}.{time}.txt")
# os.system(f"git add err && git commit -m \"update {time}'s error books\" && git push")
