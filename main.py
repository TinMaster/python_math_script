import math
import numpy as npy
import os

distance_file = os.path.join('water.xyz')
distances = npy.genfromtxt(fname = distance_file, delimiter=',', dtype = 'unicode')
data = distances[2:]

molecules = []

class Molecule:
  def __init__(self,name, x, y,z):
    self.name = name
    self.x = x
    self.y = y
    self.z = z

for x in range(len(data)):
  line = data[x].tolist()
  temp = line.split() #new array with broken up elements
  name = temp[0]
  temp.pop(0)
  temp = [float(i) for i in temp] #never got rid of 
  m = Molecule(name, temp[0], temp[1],temp[2]) 
  molecules.append(m)

def equation(mole1,mole2):
  return math.sqrt((mole1.x - mole2.x)**2 + (mole1.y-mole2.y)**2 + (mole1.z-mole2.z)**2)

def main():
  for i in range(len(molecules)):
    if i + 1 < len(molecules):
      print("The distance between " + molecules[i].name + " & "+ molecules[i+1].name +" is "+ str(equation(molecules[i], molecules[i+1])))
    else: #take the last item and do it to the first item
      print("The distance between " + molecules[i].name + " & "+ molecules[0].name +" is "+ str(equation(molecules[i], molecules[0])))
  
if __name__ == '__main__':
  main()
