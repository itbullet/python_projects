f1 = open(r"C:\Users\eduar\Dropbox\Documents\Python\06052019\file1.txt", "r")
f2 = open("C:/Users/eduar/Dropbox/Documents/Python/06052019/file2.txt", "a")
for line in f1.readlines():
  f2.write("\n%s" %line)
f2.close()
f1.close()