"""Author: Sudi Yussuf
"""
import unittest
import triangles as t
import dice as d
import words as w
from fraction import Fraction as Fraction
import graph as g



class TestTriangles(unittest.TestCase):
  def test_triangles(self):
    actual = t.triangles(6)
    expected = [1, 3, 6, 10, 15, 21]
    self.assertEqual(actual, expected)
  def test_ctriangles(self):
    actual = t.ctriangles(6)
    expected = [1, 3, 6, 10, 15, 21]
    self.assertEqual(actual, expected)
  def test_pascal(self):
    actual = t.pascal(6)
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    self.assertEqual(actual, expected)



class TestDice(unittest.TestCase):
  def test_diceroller(self):
    m = d.diceroller()
    self.assertTrue(len(m)==6)


class TestWords(unittest.TestCase):
  def test_words(self):
    actual = w.firstlines("text")
    expected = {'this': 0, 'is': 0, 'a': 1, 'text': 1, 'file': 2}
    self.assertEqual(actual, expected)

class TestFraction(unittest.TestCase):
  def test_prime(self):
    actual = Fraction(5,7);
    expected = "5/7"
    self.assertEqual(str(actual), expected) 
  def test_notPrime(self):
    actual = Fraction(8,6);
    expected = "4/3"
    self.assertEqual(str(actual), expected)
  def test_num_denom_diff(self):
    s = Fraction(5,6);
    p = Fraction(7,6);
    actual = s +p
    expected = "2"
    self.assertEqual(str(actual), expected)
  def test_num_denom_same(self):
    s = Fraction(8,6);
    p = Fraction(7,5);
    actual = s +p
    expected = "41/15"
    self.assertEqual(str(actual), expected)
  def test_less_than(self):
    s = Fraction(8,6);
    p = Fraction(7,5);
    actual = s < p
    expected = True
    self.assertEqual(actual, expected)
  def test_greater_than(self):
    s = Fraction(8,6);
    p = Fraction(7,5);
    actual = s > p
    expected = False
    self.assertEqual(actual, expected)
  def test_not_equal(self):
    s = Fraction(8,6);
    p = Fraction(7,5);
    actual = s != p
    expected = True
    self.assertEqual(actual, expected)
  def test_equal(self):
    s = Fraction(8,6);
    p = Fraction(7,5);
    actual = s == p
    expected = False
    self.assertEqual(actual, expected)
  def test_goe(self):
    s = Fraction(8,6);
    p = Fraction(7,5);
    actual = s >= p
    expected = False
    self.assertEqual(actual, expected)
  def test_loe(self):
    s = Fraction(8,6);
    p = Fraction(7,5);
    actual = s <= p
    expected = True
    self.assertEqual(actual, expected)
  def test_from_string(self):
    s = Fraction(8,6);
    actual = s.from_str('6/7')
    expected = '6/7'
    self.assertEqual(str(actual), expected)

class TestGraphEdgeList(unittest.TestCase):
  def test_EdgeListDegrees(self):
    vertices = {0, 1, 2, 3}
    edges = {(0, 1), (0, 2), (1, 2), (2, 3)}
    edge_g = g.EdgelistGraph([(0, 1), (0, 2), (2, 1), (2, 3)])
    actual = edge_g.degree(0)
    expected = 2
    self.assertEqual(actual, expected) 
  def test_EdgeListadj(self):
    vertices = {0, 1, 2, 3}
    edges = {(0, 1), (0, 2), (1, 2), (2, 3)}
    edge_g = g.EdgelistGraph([(0, 1), (0, 2), (2, 1), (2, 3)])
    actual = edge_g.adjacent_to(0)
    expected = {1, 2}
    self.assertEqual(actual, expected) 


class TestGraphMatrixList(unittest.TestCase):
  def test_MatrixListDegrees(self):
    matrix_g = g.MatrixGraph([[False, True, True, False],[True, False, True, False],[True, True, False, True],[False, False, True, False]])
    actual = matrix_g.degree([False, True, True, False])
    expected = 2
    self.assertEqual(actual, expected) 
  def test_MatrixListAdj(self):
    matrix_g = g.MatrixGraph([[False, True, True, False],[True, False, True, False],[True, True, False, True],[False, False, True, False]])
    actual = matrix_g.adjacent_to([False, True, True, False])
    expected = {(True, True, False, True), (True, False, True, False)}
    self.assertEqual(actual, expected) 
 
unittest.main()
