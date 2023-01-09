import csv
with open('output.txt', 'r') as in_file:
    lines = (line.split(":") for line in in_file if line)
    with open('output.csv', 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Gmail', 'Password','Recovery','year'))
        writer.writerows(lines)