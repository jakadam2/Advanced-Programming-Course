import functools

class Test:
	def __init__(self,*args,**kwargs) -> None:
		self.kwargs = kwargs
		self.args = args

def coroutine(fun):
	functools.wraps(fun)
	def wrapper(*args,**kwargs):
		gen = fun(*args,**kwargs)
		next(gen)
		return gen
	return wrapper


@coroutine
def int_handler(succ,rec):
	while True:
		event = (yield)
		if type(event) == int:
			print(f'Event {event} is handled by int handle')
			rec.send((event,'int_file'))
		elif succ is not None:
			succ.send(event)


@coroutine
def str_handler(succ,rec):
	while True:
		event = (yield)
		if  type(event) == str:
			print(f'Event {event} is handled by str handler')
			rec.send((event,'str_file'))
		elif succ is not None:
			succ.send(event)



@coroutine
def default_handler(succ = None):
	while True:
		event = (yield)
		print(f'Event {event} is handled by default handler')


@coroutine
def tuple_handler(succ = None):
	while True:
		event = (yield)
		if type(event) == tuple:
			if event[0] == 'Test':
				obj = globals()[event[0]](*event[1:])
				print(f'I made a object {event[0]} with parameters {obj.args}')
			else:
				print(f'I cannot made a object {event[0]}')
		elif succ is not None:
			succ.send(event)


@coroutine
def printer():
	while True:
		event = (yield)
		print(f'I receive {event}')


p = printer()
pipe_line = int_handler(str_handler(tuple_handler(default_handler()),p),p)
test = ['sddasdas',32322,'dsadasdd',412123,True,False,('Test',1,2,3,4,5),(523452 ,23423 ,423423)]
for t in test:
	pipe_line.send(t)
