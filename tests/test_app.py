import LM

def test_app():
  nn = LM.NN([1, 5, 1])
  nn.train_lm([[1], [2], [3]], [[1], [2], [3]])
  assert True
