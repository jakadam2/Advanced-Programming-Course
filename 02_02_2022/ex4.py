import multiprocessing
import re

def add_task(P,files,queue):
    for file in files:
        queue.put((P,file))

def find_word(P,file_name):
    with open(file_name,'r') as f:
        words = re.split('\n| ',f.read())
        return words.count(P)
    
def worker(jobs,results):
    while True:
        word,file_name = jobs.get()
        result = find_word(word,file_name)
        results.put((result,file_name))
        jobs.task_done()

def create_processes(process_amount,jobs,results):
    for _ in range(process_amount):
        process = multiprocessing.Process(target = worker,args=(jobs,results))
        process.daemon = True
        process.start()

def max_num_occurrences(P,files,process_amount):
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    create_processes(process_amount,jobs,results)
    add_task(P,files,jobs)
    jobs.join()
    maxnr = 0
    maxfile = None
    while not results.empty():
        nr,file = results.get()
        if nr > maxnr:
            maxnr = nr
            maxfile = file
    print(f'In file {maxfile} is {maxnr}')
