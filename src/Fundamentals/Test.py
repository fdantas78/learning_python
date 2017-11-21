def func1():
    text = "Example of file access!"
    print(text)
    fileT = open('test.txt', 'r')
    # file.write(text + '\n')
    f_read = fileT.read()
    print(f_read)

    splitMe = f_read.split(' ')
    #splitMe = splitMe.split(' ')
    print(splitMe)

    fileT.close()
    
    
