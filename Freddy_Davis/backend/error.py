try:
    f =open('hai.txt','r')
    f.write("i am freddy")
except IOError:
    print("could not find file")
else:
    print("success")
    f.close()
