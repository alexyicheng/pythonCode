# 02.12.2024

# read bill.text
f1 = open('bill.txt','r',encoding='utf-8')
f2 = open('bill.txt.bak', 'a', encoding='utf-8')
for line in f1:
    if line.strip().split(',')[-1] == '正式':
        f2.write(line)
        # f2.write('\n')
        f2.flush()
    else:
        continue
# write bill.txt.bak
#
f1.close()
f2.close()


