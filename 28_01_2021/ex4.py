import multiprocessing
import re

def fun(file_name,word_list):
    f = open(file_name,'r')
    words = re.findall(r'\w+',f.read())
    counted = [words.count(word_list[i]) for i in range(len(word_list))]
    for i in range(len(counted)):
        amount = counted[i]
        if amount == max(counted):
            print(word_list[i],amount)


def work(jobs,results,word_list):
    while True:
        try:
            file_name = jobs.get()
            result = fun(file_name,word_list)
            results.put(result)
        finally:
            jobs.task_done()

def create_processes(concurrency,jobs,results,word_list):
    for _ in range(concurrency):
        process = multiprocessing.Process(target = work, args = (jobs,results,word_list))
        process.daemon = True
        process.start()

def print_words(word_list,file_list,concurrency):
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
