import functools


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
def printer():
	while True:
		event = (yield)
		print(f'I receive {event}')


p = printer()
pipe_line = int_handler(str_handler(default_handler(),p),p)
test = ['sddasdas',32322,'dsadasdd',412123,True,False]
for t in test:
	pipe_line.send(t)
