f = open('text_file.txt')
lines = f.readlines()
new_lines = []
for i in lines:
    new_lines.append(i.strip())
f.close()
f = open('text_file.txt', 'w')
for i in new_lines:
    if i != '':
        f.write(i+'\n')
f.close()


#https://www.journaldev.com/23763/python-remove-spaces-from-string
