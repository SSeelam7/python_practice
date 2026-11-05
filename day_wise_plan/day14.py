#1:
# import os
# print(os.path.exists("day13_pipeline.log"))

#2:
import os
path = os.path.join("data", "pipeline.log")
print(path)

files = os.listdir("data")
print(files)
