f = open("url.txt", mode="r", encoding="UTF-8")

# for x in range(10):
#     f.write("hello" + str(x))
# f.close

for line in f.readlines():
    print(line, end="\n\n")

f.close
