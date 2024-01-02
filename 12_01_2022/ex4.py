import multiprocessing
import re
def fun(file,word):
    f = open(file,'r')
    words = re.findall(r'\w+',f.read())
    for i in range(len(words)):
        if words[i] == word:
            return(i,word[i])

def work(jobs,results,word):
    while True:
        try:
            file = jobs.get()
            result = fun(file,word)
            results.put(result)
        finally:
            jobs.task_done()

def create_processes(word,jobs,results,proc_amount):
    for _ in range(proc_amount):
        process = multiprocessing.Process(target = word,args = (jobs,results,word))
        process.daemon = True
        process.run()

def write(word,file_list,proc_amount):
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue9
    create_processes(word,jobs,results,proc_amount)
    for file in file_list:
        jobs.put(file)
    try:
        jobs.join()
    except:
        print('CANCELLED')
    while not results.empty():
        result = results.get_nowait()
        print(result)     