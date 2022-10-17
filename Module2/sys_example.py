import sys

print(sys.version)
print(sys.version_info)

print(sys.argv)

if len(sys.argv) <3:
    print("не указаны папка-источник и папка-назначения")
    exit(1)

source_dir=sys.argv[1]
dest_dir=sys.argv[2]
print("source dir =", source_dir)
print("dest dir =", dest_dir)
