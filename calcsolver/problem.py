class Problem:
  def __init__(self, start_number, end_number, move_count, operators):
    self._start_number= start_number
    self._end_number = end_number
    self._move_count = move_count
    self._operators = operators

  def start_number(self):
    return self._start_number

  def end_number(self):
    return self._end_number

  def move_count(self):
    return self._move_count

  def operators(self):
    return self._operators
    
