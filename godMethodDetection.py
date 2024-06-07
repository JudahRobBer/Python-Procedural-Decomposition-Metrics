import accessofForeignData, communicativeFunctionalityChecker, complexityMetricGenerator

class godMethodDetector():
  def __init__(self, CFC: dict, AFD: dict, Cyc: dict):
    self.optimalCFC = CFC
    self.optimalAFD = AFD
    self.optimalCyc = Cyc

  def ranked(self):
    print(sort(self.optimalCFC))
