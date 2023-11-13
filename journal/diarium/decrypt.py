import sqlite3
from markdownify import markdownify as md

con = sqlite3.connect("Diarium.sqlite")
cur = con.cursor()

res = cur.execute("SELECT * FROM 'Entries'")
entries = res.fetchall()
# 0 id
# 1 titre
# 2 text


res = cur.execute("SELECT * FROM 'Media'")
medias = res.fetchall()
# 0 id
# 1 --
# 2 data
# 3 --
# 4 file extension
# 5 index ?
# 6 diaryId


def entryConvert(entry, media, name):
    if entry[0] == media[6]:
        images = [name] if len(entry) == 6 else entry[3] + [name]
        return [entry[0], entry[1], entry[2], images]
    return [entry[0], entry[1], entry[2], entry[3]] if len(entry) == 4 else [entry[0], entry[1], entry[2], []]


i = 0
for media in medias:
    # with open(f"image_{i}.jpg", "wb") as fh:
    #     fh.write(media[2])
    entries = list(
        map(lambda entry: entryConvert(entry, media, f"images/image_{i}.jpg"), entries)
    )
    i += 1

print(entries)
j = 0
for entry in entries:
    i = 0
    add = ""
    for image in entry[3]:
        add += f"![image_{i}](" + image + ")"
        i += 1

    value = "# " + entry[1] + "\n" + md(entry[2]) + add
    with open(f"note_{j}.md", "w") as my_file:
        my_file.write(value)
    j += 1
