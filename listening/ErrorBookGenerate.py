import datetime
import os
from pprint import pprint

#get file from last commit
# Files = os.("git diff --name-only HEAD HEAD^").read().split("\n")
Files = os.popen("git diff --name-only HEAD HEAD^^").read().split("\n")
    # 在windows中, ^是转义符, 要想敲一个^, 需要敲^^
# pprint(Files)
#get time as MONTH-DAY
time = datetime.datetime.now().strftime("%m%d%H")
def file_cmp(file1, file2, save):
    # direct compare each line of them
    # ONLY print the different line
    # save to 'save'
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2, open(save, "w", encoding="utf-8") as f3:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        # write head
        f3.write(f"{'Ref':<40}|Test\n")
        for i in range(len(lines1)):
            # ignore space and '\n'
            if lines1[i].strip() != lines2[i].strip():
            # if lines1[i] != lines2[i]:
                # delete the last '\n' in lines1[i]
                if lines1[i][-1] == '\n':
                    lines1[i] = lines1[i][:-1]
                # align '|' to a fixed position
                f3.write(f"{lines1[i]}{' '*(max(0, 40-len(lines1[i])))}|{lines2[i]}")
                # f3.write(f"{lines1[i]}  \t|  {lines2[i]}")
for file in Files:
    # print("DEBUG: ", file, file.startswith("listening/test"), os.path.exists(file))
    if(os.path.exists(file) and file.startswith("listening/test")):
        filename = os.path.basename(file)
        print(filename)
        file_cmp(f"listening/ref/{filename}", f"listening/test/{filename}", f"listening/err/{filename}.{time}.txt")
        # os.system(f"comp listening\\ref\\{filename} listening\\test\\{filename} > listening\\err\\{filename}.{time}.txt")
        # os.system(f"fc /w /c /l /n listening/ref/{filename} listening/test/{filename} > listening/err/{filename}.{time}.txt")
# os.system(f"git add err && git commit -m \"update {time}'s error books\" && git push")
