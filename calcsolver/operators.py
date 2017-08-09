import abc

class Operator(object, metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def operate(self, state):
    pass

class AddOperator(Operator):
  def __init__(self, value):
    self._value = value

  def operate(self, state):
    return state.value() + self._value

  def __str__(self):
    if self._value > 0:
      sign = "+" 
    else:
      sign = "-"
    return "[ %s %d ]" % (sign, abs(self._value))

  def value(self):
    return self._value

class MultiplyOperator(Operator):
  def __init__(self, value):
    self._value = value

  def operate(self, state):
    return state.value() * self._value

  def __str__(self):
    return "[ * %d ]" % self._value

  def value(self):
    return self._value

class DivideOperator(Operator):
  def __init__(self, value):
    self._value = value

  def operate(self, state):
    return state.value() / self._value

  def __str__(self):
    return "[ / %d ]" % self._value

  def value(self):
    return self._value

