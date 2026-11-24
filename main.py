import os

TEXT = "Q"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)

data = open("/output/entry.txt", "rb").read()
assert data == TEXT.encode("utf-8"), "written bytes must equal TEXT exactly"
assert len(TEXT) == 1 and "A" <= TEXT <= "Z", "exactly one letter, A-Z"
