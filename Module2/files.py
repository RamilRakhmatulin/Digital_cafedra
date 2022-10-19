import os
from os import path
from pathlib import Path
print("File Main.py")
file=open("..\Module1\main.py", "r")
print(file.read())
file.close()

# print("Fail Variables.py")
# file = open("../Module1/variables.py", "r")
# for line in file:
#     print(line.strip())
# #
# file.close()

# with open("../Module1/variables.py", "r") as file:
#     # открытие файла
#     for line in file:
#         print(line.strip())
# # закрытие файла

cur_path=os.getcwd()
# files_dir=os.path.join(cur_path, "Files")
files_dir=Path(cur_path) / "Files"
print(files_dir)
try:
    # os.mkdir((files_dir))
    files_dir.mkdir()
except FileExistsError:
    pass
# file_path=os.path.join(files_dir, "file.txt")
file_path=files_dir / "file.txt"
# with open(file_path, "w+") as file:
with file_path.open("w+") as file:
    file.write(str(123))
    file.seek(0)
    print(file.read())

# os.remove("file2.txt")
# print(os.path.exists("file2.txt"))
print(Path("files.py").exists())
print(Path("files.py"))

print(file_path)
print(path.basename(file_path))
print(path.dirname(file_path))
print(path.splitext("file.txt"))

print(path.join("..", "testdir"))
print(path.abspath(path.join("..", "testdir")))

TEST=os.environ.get(
    "TEST",
    "default value for environment variable "
)
print("test", TEST)

