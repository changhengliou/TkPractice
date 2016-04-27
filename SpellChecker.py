import time
words = open("C:\\Users\\haha\\Desktop\\SpellChecking.txt").readlines()
words = map(lambda x: x.strip(), words)

start = time.time()

if 'Facebook' in words:
    print("True")
else:
    print("False")

total = time.time() - start
print(total/10, "secs")
