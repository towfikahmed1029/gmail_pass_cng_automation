with open(r"alltest.txt", 'r') as fp2:
    lines2 = fp2.readlines()
    lines2 = " ".join(lines2)
count = 1
with open(r"missing.txt", 'w') as fpw:
    fpw.write("")
with open(r"gmail.txt", 'r') as fp:
    lines = fp.readlines()
    for i in lines:
        full = i 
        i = i.split(":")[0]
        if i in lines2:
            pass
        else:
            with open(r"missing.txt", 'a') as fpw:
                fpw.write(full)
                print("Line number-->>",count, "Missing Gmail-->>>",full)
        count +=1



with open('missing.txt', 'r') as in_file:
    lines2 = in_file.readlines()
    for i in lines2:
        with open('input.txt', 'a',newline='') as out_file:
            out_file.write(i)