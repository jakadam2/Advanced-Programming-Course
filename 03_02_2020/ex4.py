class CorsoDiLaurea:

	def __init__(self):
		self._students = {}
		self._nr_students = 0
		self._grad_mean = None
		self.grad_mean_ok = None
		self_observers = []

	def add_observer(self,observer):
		self._observers.append(observer)

	def remove_observer(self,observer):
		self._observer.remove(observer)

	def notify(self):
		for observer in observers:
			observer.update()

	@property
	def grad_mean(self):
		return self._grad_mean

	@grad_mean.setter
	def grad_mean(self,value):
		self._grad_mean = value
		if value > 100:
			self.grad_mean_ok = True
		else:
			self.grad_mean_ok = False


