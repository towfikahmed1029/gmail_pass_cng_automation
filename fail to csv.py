import csv
with open('fail.txt', 'r') as in_file:
    lines = (line.split(":") for line in in_file if line)
    with open('fail.csv', 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Gmail', 'Password','Recovery','year'))
        writer.writerows(lines)