class State:
  
  def __init__(self, value=None, steps=None):

    if value is None:
      value = 0
    if steps is None:
      steps = []

    self._value = value
    self._steps = steps

  def clone(self):
    return State(_value, _steps)

  def apply(self, operator):
    self._steps.append(operator)
    self._value = operator.operate(self)

  def value(self):
    return self._value

  def steps(self):
    return self._steps
