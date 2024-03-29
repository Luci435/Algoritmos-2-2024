from linkedlist import *

class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
    height=None

#search(B,element)
#Devuelve la key asociada a la primera instancia del elemento.
#Devuelve None si el elemento no se encuentra.
def searchT(AVL, element):
  if AVL.root==None:
    return None
  else:
    return searchByValue(AVL.root, element)

#Recibe el nodo actual y el elemento a buscar
#recursivamente se mueve por el arbol hasta encontrar la key correspondiente al valor
def searchByValue(currentNode, element):
  if currentNode!=None:
    if currentNode.value==element:
      return currentNode.key
    else:
      key=searchByValue(currentNode.leftnode, element)
      if key!=None:
        return key
      key=searchByValue(currentNode.rightnode, element)
      if key!=None:
        return key

#insert(B,element,key)
#Si pudo insertar con éxito devuelve la key donde se inserta el elemento. 
#En caso contrario devuelve None.
def insertT(AVL,element,key):
  if key==None: #caso donde no se pasa bien la key
    return None
  else: #creo el nodo con todos sus atibutos 
    newNode =AVLNode()
    newNode.key = key
    newNode.value = element
    newNode.bf=0
    newNode.height=1
    if AVL.root==None: #si no existe el arbol lo creo con el nodo como raiz
      AVL.root=newNode
      return key
    else: #inserto el elemento si ya habia raiz 
      insertElement(newNode, AVL.root)
      reBalanceRecu(AVL,newNode) #rebalanceo desde el padre del nodo insertado hasta la raiz
      return key

#Recibe el nuevo nodo y el actual para recursivamente buscar el lugar correspondiente según la key del nuevo nodo
def insertElement(newNode, currentNode):
  if newNode.key > currentNode.key: #comparo keys para saber si va a la izq o derecha
    if currentNode.rightnode == None:
      currentNode.rightnode= newNode
      newNode.parent=currentNode
    else:
      insertElement(newNode, currentNode.rightnode) #si no hay espacio continuo comparando
  else:
    if currentNode.leftnode == None:
      currentNode.leftnode = newNode
      newNode.parent=currentNode
    else: 
      insertElement(newNode, currentNode.leftnode)
  return 

#delete(B,element)
#Se debe desvincular el Node a eliminar.
#Devuelve clave (key) del elemento a eliminar. 
#Devuelve None si el elemento a eliminar no se encuentra.
def deleteT(AVL, element):
  key=searchT(AVL,element) #busca la key del elemento
  #si no existe el elemento retorna none
  if key==None:
    return None
  else:
    #uso accessReturnNode para recibir el nodo que hay que eliminar directamente y no tener que buscarlo
    node=accessReturnNode(AVL.root, key)
    parent=node.parent
    #el nodo no tiene hijos
    if node.rightnode==None and node.leftnode == None:
      if node.key>parent.key:
        parent.rightnode=None
        reBalanceRecu(AVL, parent) #rebalanceo el padre del nodo
        return key
      elif node.key<parent.key:
        parent.leftnode=None
        reBalanceRecu(AVL, parent)  #rebalanceo el padre del nodo
        return key
      else:
        return None
    elif node.rightnode!=None:
      #tiene un solo hijo (el de la derecha)
      if node.leftnode==None:
        if node.key<parent.key:
          current=node.rightnode
          parent.leftnode=current
          current.parent=parent
          reBalanceRecu(AVL, parent)  #rebalanceo el padre del nodo 
          return key
        else: 
          current=node.rightnode
          parent.rightnode=current
          current.parent=parent
          reBalanceRecu(AVL, parent) #rebalanceo el padre del nodo
          return key
      else:
      #tiene dos hijos
      #menor de los mayores
        current=node.rightnode
        while current.leftnode!=None:
          current=current.leftnode
        exleft=current.leftnode
        current.leftnode=node.leftnode
        if current.rightnode!=None:
          rightnode=current.rightnode
          if current.rightnode.value!=node.rightnode.value :
            current.rightnode=node.rightnode
            rightnode.parent=current.rightnode
            current.rightnode.leftnode=rightnode
          else:
            current.rightnode=None
        else: 
          current.rightnode=node.rightnode
          current.rightnode.leftnode=exleft
          node.rightnode.parent=current
        if key<parent.key:
          parent.leftnode=current
        else:
          parent.rightnode=current
        current.parent=parent
        reBalanceRecu(AVL, current.rightnode)  #rebalanceo el hijo derecho ya que le cambia el bf
        return key
    else:
    #right no existe y left si
      if node.key<parent.key:
        current=node.leftnode
        parent.leftnode=current
        current.parent=parent
        reBalanceRecu(AVL, parent)
        return key
      else:
        current=node.leftnode
        parent.rightnode = current
        current.parent=parent
        reBalanceRecu(AVL, parent)
        return key
#busca recursivamente el nodo correspondiente a la key 
#una vez encuentra el nodo lo devuelve 
def accessReturnNode(currentNode, key):
  if currentNode.key==key:
    return currentNode
  else:
    if currentNode.key<key:
      if currentNode.rightnode !=None:
        node=accessReturnNode(currentNode.rightnode, key)
      else:
        return None
    else:
      if currentNode.key>key:
        if currentNode.leftnode != None:
          node=accessReturnNode(currentNode.leftnode, key)
        else:
          return None
      else:
        return None
  return node

# rotateLeft(Tree,avlnode) 
# Descripción: Implementa la operación rotación a la izquierda 
# Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
# Salida: retorna la nueva raíz
def rotateLeft(avl, avlnode):
  newparent=avlnode.rightnode #avlnode es la raíz
  if avlnode.parent.leftnode==avlnode: #me fijo si es hijo izquierdo o derecho
    left=True
  else:
    left=False
  if avlnode.parent==None: #avlnode es la raiz
    #cambio referencias y queda como nuevo padre el hijo izq y como raiz del avl
    avlnode.parent=newparent
    avlnode.rightnode=newparent.leftnode #le asigno como hijo izq el ex hijo der de la nueva raiz
    avlnode.rightnode.parent=avlnode
    newparent.parent=None #elimino el padre de la nueva raiz
    newparent.leftnode=avlnode
  else: #no es la raíz
    exparent=avlnode.parent #gurdamos referencias
    if newparent.leftnode!=None: #cambiamos hijos si tienen
      avlnode.rightnode=newparent.leftnode
      avlnode.rightnode.parent=avlnode
    else: #sino solo eliminamos el viejo hijo
      avlnode.rightnode=None
    avlnode.parent=newparent #rotamos
    newparent.leftnode=avlnode
    newparent.parent=exparent  #actualizamos padre del nuevo nodo rotado
    if left:
      exparent.leftnode=newparent
    else:
      exparent.rightnode=newparent
  avlnode=reHeightBF(avlnode) #actualizar alturas y bf 
  newparent=reHeightBF(newparent)
  return

# rotateRight(Tree,avlnode) 
# Descripción: Implementa la operación rotación a la derecha 
# Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
# Salida: retorna la nueva raíz

def rotateRight(avl, avlnode):
  newparent=avlnode.leftnode #guardo el nuevo padre (hijo izq)
  if avlnode.parent.leftnode==avlnode:  #me fijo si es hijo izquierdo o derecho
    left=True
  else:
    left=False
  if avlnode.parent==None: #avlnode es la raiz
    #cambio referencias y queda como nuevo padre el hijo izq y como raiz del avl
    avlnode.parent=newparent
    avlnode.leftnode=newparent.rightnode #le asigno como hijo izq el ex hijo der de la nueva raiz
    avlnode.leftnode.parent=avlnode
    newparent.parent=None #elimino el padre de la nueva raiz
    newparent.rightnode=avlnode
  else: #no es la raíz
    exparent=avlnode.parent #gurdamos referencias
    if newparent.rightnode!=None: #cambiamos hijos si tienen
      avlnode.leftnode=newparent.rightnode
      avlnode.leftnode.parent=avlnode
    else: #sino solo eliminamos el viejo hijo
      avlnode.leftnode=None
    #rotamos
    avlnode.parent=newparent
    newparent.rightnode=avlnode
    newparent.parent=exparent #actualizamos padre del nuevo nodo rotado
    if left:  #colocamos al nuevo nodo al lado correspondiente 
      exparent.leftnode=newparent
    else:
      exparent.rightnode=newparent
  avlnode=reHeightBF(avlnode)  #actualizar alturas y bf 
  newparent=reHeightBF(newparent)
  return

#recalcula la altura y el balance factor de un nodo fijandose en las alturas de los hijos
def reHeightBF(node):
  if node.leftnode!=None: #tengo hijo a la izq
    if node.rightnode!=None: #tengo hijo a la derecha
      node.bf=node.leftnode.height - node.rightnode.height 
      node.height=max(node.leftnode.height, node.rightnode.height) +1
    else: #no tengo hijo a la derecha
      node.bf=node.leftnode.height
      node.height=node.leftnode.height +1
  else: #no tengo hijo izq 
    if node.rightnode!=None: #tengo hijo derecho
      node.bf=- node.rightnode.height 
      node.height=node.rightnode.height +1
    else: #no tengo hijo a la derecha
      node.bf=0
      node.height=1
  return node

#calcula bf y altura desde el nodo recibido hasta la raiz, no todo el arbol
def calculateBalanceRecur(node):
  if node.leftnode!=None:
    #si tengo hijo a la izq sin calcular su altura, la calculo
    if node.leftnode.height==None:
      return calculateBalanceRecur(node.leftnode)
    else: 
      #si ya está calculada y no tengo un hijo a la derecha, calculo bf
      if node.rightnode==None:
        node.height=node.leftnode.height + 1 
        node.bf= node.leftnode.height
        return node
      elif node.rightnode.height==None:
        #si tengo hijo a la derecha pero su altura no está, la calculo
        return calculateBalanceRecur(node.rightnode)
      else:
        #tengo los dos hijos con sus alturas, calculo bf y altura del nodo actual
        node.height= max(node.leftnode.height,node.rightnode.height) +1
        node.bf= node.leftnode.height - node.rightnode.height
        if node.parent==None:
          return node
        else:
          return calculateBalanceRecur(node.parent) #calculo altura y bf del padre 
  elif node.rightnode!=None:
    #tengo hijo a la derecha sin altura, la calculamos
    if node.rightnode.height==None:
      return calculateBalanceRecur(node.rightnode)
    else:
      #no tengo hijo a la izquierda y el derecho tiene altura, calcular bf
      if node.leftnode==None:
        node.height=node.rightnode.height+1
        node.bf = -node.rightnode.height
        if node.parent==None:
          return node
        else:
          return calculateBalanceRecur(node.parent) #calculo altura y bf del padre 
      elif node.leftnode.height==None:
        #tengo hijo izq sin altura, calcular altura
        return calculateBalanceRecur(node.leftnode)
      else: 
        #tengo dos hijos y alturas, calculo bf y altura
        node.height=max(node.leftnode.height,node.rightnode.height) +1
        node.bf = node.leftnode.height - node.rightnode.height
        return node
  else:
    #estoy en una hoja, bf y altura son 0
    node.bf=0
    node.height=1 #usamos altura uno como si no tuviera hijos asi se puede calcular bf sin problema
  return calculateBalanceRecur(node.parent) #calculo altura y bf del padre 


#recibe el avl y el nodo a balancear, balancea desde el nodo hasta la raiz
def reBalanceRecu(avl,node):
  if node==None:
    return avl, node
  reHeightBF(node) #recalcula la altura y bf del nodo para contemplar casos recursivos
  if node.bf==0 or node.bf==1 or node.bf==-1: #revisa si el nodo está balanceado
    if node.parent==None:
      return node
    else:
      return reBalanceRecu(avl,node.parent) #si está balanceado balancea el padre 
  else:
    if node.bf==-2: #nodo desbalanceado 
      if node.rightnode.bf==1: #caso especial
        rotateRight(avl,node.rightnode) #roto primero a la derecha el hijo 
      rotateLeft(avl,node)
    elif node.bf==2:
      if node.leftnode.bf==-1: #caso especial
        rotateLeft(avl,node.leftnode) #roto primero a la izquierda el hijo 
      rotateRight(avl,node)
  if node.parent==None:
    return node #si es la raiz devuelvo el nodo
  else:
    return reBalanceRecu(avl,node.parent) #recalculo el bf y altura del padre
