from pathlib import Path
SAMPLE = Path(__file__).resolve().parent / "hello.txt"
print(SAMPLE)

def read_whole_file()->str:
   with open (SAMPLE, "r", encoding="utf-8") as f:
        return f.read()
print(read_whole_file())

def read_as_line()->list:
    with open(SAMPLE,"r",encoding="utf-8") as f:
        return f.readlines()
print(read_as_line())