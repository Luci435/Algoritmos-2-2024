class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None


def printlist(L):
  current=L.head
  while current!=None:
    print (current.value, end=" -> ")
    current=current.nextNode
  print (" ")
#Agrega un elemento al comienzo de L, siendo L una LinkedList

def add(L,element):
  newElement=Node()
  newElement.value=element
  newElement.nextNode=L.head
  L.head=newElement
  
#Busca un elemento de la lista. Devuelve la posición donde se encuentra la primera instancia del elemento. 
#Devuelve None si el elemento no se encuentra.

def search(L,element):
  currentNode=L.head
  pos=0
  while currentNode!=None:
    pos=pos+1
    if currentNode.value==element:
      return pos-1
    currentNode=currentNode.nextNode
  return None

#Si pudo insertar con éxito devuelve la posición donde se inserta el elemento.
#En caso contrario devuelve None. 
#Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.

def insert(L,element,position):
  newElement=Node()
  newElement.value=element
  currentNode=L.head  
  if position>length(L):
    return None
  if position==0:
    add(L,element)
    return position
  elif position<0:
    return None
  else:
    pos=0
    while currentNode!=None:
      if pos==position-1:
        newElement.nextNode=currentNode.nextNode
        currentNode.nextNode=newElement
        return position
      else:
        pos+=1
        currentNode=currentNode.nextNode
        

#Se debe desvincular el Node a eliminar.
#Devuelve la posición donde se encuentra el elemento a eliminar. 
#Devuelve None si el elemento a eliminar no se encuentra.

def delete(L,element):
  pos=search(L,element)
  if pos==None:
    return None
  elif pos>0:
    currentNode=L.head
    for i in range(0,pos-1):
      currentNode=currentNode.nextNode
    currentNode.nextNode=currentNode.nextNode.nextNode    
    return pos
  elif pos==0:
    L.head=L.head.nextNode
    return pos
  else:
    return None

#Devuelve el número de elementos.

def length(L):
  pos=0
  currentNode=L.head
  while currentNode!=None:
    currentNode=currentNode.nextNode
    pos+=1
  return pos

#Devuelve el valor de un elemento en una position de la lista 
#Devuelve None si no existe elemento para dicha posición.

def access(L,position):
  currentNode=L.head
  pos=0
  while currentNode!=None:
    if pos==position:
      return currentNode.value
    else:
      pos+=1
      currentNode=currentNode.nextNode

#Permite cambiar el valor de un elemento de la lista en una posición determinada
#Devuelve None si no existe elemento para dicha posición. 
#Caso contrario devuelve la posición donde pudo hacer el update.

def update(L,element,position):
  currentNode=L.head
  pos=0
  while currentNode!=None:
    if pos==position:
      currentNode.value=element
      return pos
    else:
      pos+=1
      currentNode=currentNode.nextNode


#doy vuelta la lista ya que al utilizar add los añade "al revés"
def invertList(L):
  #uso una lista auxiliar en la que pongo todos los valores de la lista C 
  auxC=LinkedList()
  for j in range (0, length(L)):
    add(auxC,access(L,j))
  #cambio una lista por otra 
  L.head=auxC.head
  return L

def printList(L):
  currentNode=L.head
  while currentNode.nextNode!=None:
    print(currentNode.value, end=" ")
    currentNode=currentNode.nextNode
  print("")
  return