import filecmp
import shutil
import tempfile
import zipfile
from pathlib import Path

files_dir=Path("Files")
result=filecmp.cmp(
    files_dir/"file.txt",
    files_dir/"file2.txt"
)
print(result)

result2=filecmp.cmpfiles(
    "Files", "Files2", ["file.txt"]

)
# match, mismatch, errors
print(result2)

# shutil.rmtree("Files2")
shutil.copytree("Files", "Files2")
print(shutil.disk_usage("."))
with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_file:
    print(temp_file.name)
    with zipfile.ZipFile(temp_file.name, 'w') as zipfile:
         zipfile.write(files_dir/"file.txt", "file.txt")
         zipfile.write(files_dir / "file2.txt", "file2.txt")

# shutil.rmtree("temp_file.name")