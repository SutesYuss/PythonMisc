"""Author: Sudi Yussuf
"""
import graph as graph
import triangles as triangles
import dice as d
import words as w
from fraction import Fraction as Fraction

#triangles.py test cases
print("triangles.py test cases")
try:
  triangles.triangles(6)
except NotImplementedError:
    print("Function not working properly")
try:
  triangles.ctriangles(6)
except NotImplementedError:
    print("Function not working properly")
try:
  triangles.pascal(6)
except NotImplementedError:
    print("Function not working properly")
print("____________________________________")
print()
print()

#dice.py test cases
print("dice.py test cases")
try:
  m = d.diceroller()
except NotImplementedError:
    print("Function not working properly")
try:
  d.print_bar_chart(m)
except NotImplementedError:
    print("Function not working properly")
print("____________________________________")
print()
print()


#words.py test cases
print("words.py test cases")
try:
  w.firstlines("text")
except NotImplementedError:
    print("Function not working properly")

print("____________________________________")
print()
print()



#fraction.py test cases
print("fraction.py test cases")
#Initialization and printing of a fraction with value 0. Hint: Such a fraction should have denominator 1 in reduced form
s = Fraction(0,2);
print(s);

#Initialization and printing of a fraction with numerator and denominator that are relatively prime
s = Fraction(5,7);
print(s);

#Initialization and printing of a fraction with nonzero numerator and denominator that are not relatively prime
s = Fraction(8,6);
print(s);

#The sum of two fractions with the same denominator
s = Fraction(5,6);
p = Fraction(7,6);

print(s + p);


#The sum of two fractions with different denominators
s = Fraction(8,6);
p = Fraction(7,5);

print(s + p);

#Use functools.total_ordering to enable Fractions to be compared with any of the comparison operators in 


boo = s < p;
print(boo);

boo = s > p;
print(boo);

boo = s != p;
print(boo);

boo = s == p;
print(boo);

boo = s >= p;
print(boo);

boo = s <= p;
print(boo);


s = s.from_str('6/7')
print(s)

print("____________________________________")
print()
print()




#graph.py test cases
vertices = {0, 1, 2, 3}
edges = {(0, 1), (0, 2), (1, 2), (2, 3)}
try:
    print("EdgelistGraph")
    edge_g = graph.EdgelistGraph([(0, 1), (0, 2), (2, 1), (2, 3)])
    print(f"{str(edge_g)  = }")
    print(f"{repr(edge_g) = }")
    print()
except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")
try:
  print("Extra Cases for EdgeListGraph.....")
  print("Degrees of a vertice")
  print(edge_g.degree(0))
  print("Adjacent Vertices")
  print(edge_g.adjacent_to(0))
  print("Add a vertex")
  print(edge_g.add_vertex(5))
  print("Add Edge")
  edge = (7,8)
  print(edge_g.add_edge(edge))
  print("Remove Vertex")    
  print(edge_g.remove_vertex(2))
  print("Remove Edge")    
  print(edge_g.remove_edge(edge))


except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")
try:
    print("MatrixGraph")
    matrix_g = graph.MatrixGraph([
                                    [False, True, True, False],
                                    [True, False, True, False],
                                    [True, True, False, True],
                                    [False, False, True, False]
                                ])
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")
    print()
except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")



try:
    print("Extra Cases for MatrixGraph.....")
    print("Degrees of a vertice")
    print(matrix_g.degree([False, True, True, False]))
    print("Adjacent Vertices")
    print(matrix_g.adjacent_to([False, True, True, False]))
    print("Add a vertex")
    print(matrix_g.add_vertex([False, True, True, False,True]))
    print("Add Edge")
    edge = (7,8)
    print(matrix_g.add_edge(edge))
    print("Remove Vertex")    
    print(matrix_g.remove_vertex([False, True, True, False,True]))
    print("Remove Edge")    
    print(matrix_g.remove_edge(2))


except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")
  
try:
    print("DictGraph")
    dict_g = graph.DictGraph({0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]})
    print(f"{str(dict_g)  = }")
    print(f"{repr(dict_g) = }")
    print()


except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")
  
try:
    print("Extra Cases for DictGraph.....")
    print("Degrees of a vertice")
    print(dict_g.degree(0))
    print("Adjacent Vertices")
    print(dict_g.adjacent_to(0))
    print("Add a vertex")
    print(dict_g.add_vertex(5))
    print("Add Edge")
    edge = (7,8)
    print(dict_g.add_edge(edge))
    print("Remove Vertex")    
    print(dict_g.remove_vertex(2))
    print("Remove Edge")    
    print(dict_g.remove_edge(edge))


except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")

