class Pile:
    def __init__(self):
        self.content = []
    
    def est_vide(self):
        return self.content == []

    def __str__(self):
        return str(self.content)

    def empiler(self, element):
        self.content += [element]
    
    def depiler(self):
        last = self.dernier()
        self.content = self.content[:-1]
        return last
    
    def dernier(self):
        return self.content[-1]
    
    def taille(self):
        return len(self.content)

if __name__ == "__main__":
    pile = Pile()
    pile.empiler(34)
    pile.empiler(32)
    pile.empiler(31)
