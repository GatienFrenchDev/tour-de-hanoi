"""
Ce module permet l'usage d'une pile dans Python.
"""


class Pile:
    """
    Objet représentant une pile (LIFO).
    La pile est basée sur une liste.
    Le dernier élément de la liste représente le haut de la pile.
    """

    def __init__(self):
        self.content = []
    
    def est_vide(self) -> bool:
        """
        Retourne True si la pile est vide
        et False si la pile ne l'est pas.
        """
        return self.content == []

    def empiler(self, element):
        """
        Ajoute un élément au dessus de la pile.
        """
        self.content += [element]
    
    def depiler(self):
        """
        Enlève le dernier de la pile tout en le renvoyant.
        """
        return self.content.pop()
    
    def dernier(self):
        """
        Renvoie le dernier élément de la pile.
        """
        return self.content[-1]
    
    def taille(self) -> int:
        """
        Renvoie le nombre d'éléments dans la pile.
        """
        return len(self.content)
