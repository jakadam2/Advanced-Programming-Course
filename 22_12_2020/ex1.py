def attach(sufix,my_file):
    f = open(my_file,'a+')
    while True:
        word = yield
        f.write(word + sufix + '\n')
        if word.endswith(sufix):
            f.close()
            break

def i_o(suffix,my_file):
    f = open(my_file,'r')
    words = f.read()
    words = words.split('\n')
    attacher = attach(suffix,'test2.txt')
    attacher.send(None)
    try:
        for word in words:
            attacher.send(word)
    except:
        pass

i_o('jjj','test.txt')

    