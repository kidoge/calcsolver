class State:
  _value = 0
  _steps = []
  
  def __init__(self, value=0, steps=[]):
    self._value = value
    self._steps = steps

  def clone(self):
    return State(_value, _steps)

  def value(self):
    return self._value

  def steps(self):
    return self._steps
