import machinery.accessofForeignData as accessofForeignData, machinery.communicativeFunctionalityChecker as communicativeFunctionalityChecker, machinery.complexityMetricGenerator as complexityMetricGenerator

class godMethodDetector():
  def __init__(self, CFC: dict, AFD: dict, Cyc: dict):
    self.optimalCFC = CFC
    self.optimalAFD = AFD
    self.optimalCyc = Cyc

  def ranked(self):
    print(sort(self.optimalCFC))
