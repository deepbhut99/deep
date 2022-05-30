import shutil

# original = r'D:\OneDrive\Desktop\websocket update\1.py'
# target = r'D:\OneDrive\Desktop\websocket update\2.py'

# shutil.copyfile(original, target)


file = open("D:/OneDrive/Desktop/websocket update/1.py", "r")
replacement = ""
# using the for loop
for line in file:
    changes = line.replace("situations", "1")
    replacement = replacement + changes 

file.close()
# opening the file in write mode
fout = open("D:/OneDrive/Desktop/websocket update/1.py", "w")
fout.write(replacement)
fout.close()
