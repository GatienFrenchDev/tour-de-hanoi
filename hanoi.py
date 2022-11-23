from pile import Pile
import time, os, pyxel

class Piquet:
    def __init__(self):
        self.stack = Pile()
    
    def empiler(self, plateau):
        assert self.stack.dernier()+1 == plateau
        self.stack.empiler(plateau)
    
    def depiler(self):
        self.stack.depiler()

class Jeu:
    def __init__(self, n):
        self.n = n
        self.tour_selected = 1
        self.focus = False
        self.depart = -1
        self.coup = 0
        self.tours = [Pile(), Pile(), Pile()]
        for i in range(n):
            self.tours[0].empiler(n-i)

    def deplace(self, depart, arrivee):
        if self.tours[depart-1].taille() == 0 : return
        if len(self.tours[arrivee-1].content) != 0:
            if self.tours[depart-1].content[-1] > self.tours[arrivee-1].content[-1]:
                print("""
                ===============
                MOUVEMENT IMPOSSIBLE
                ===============
                """)
                time.sleep(1)
                return
        plateau = self.tours[depart-1].depiler()
        self.tours[arrivee-1].empiler(plateau)
    
    def __str__(self) -> str:
        res = ""
        i = 0
        for tour in self.tours:
            a = tour.content.copy()
            a.reverse()
            for item in a:
                plateau = ""
                for j in range(self.n-item):
                    plateau += " "
                for j in range(item):
                    plateau += "=="
                res += f"\t{plateau}\n"
            i += 1
            res += f"   \##### tour {i} #####/\n\n"
        return res

    def update(self):
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.tour_selected = 3 if self.tour_selected == 3 else self.tour_selected + 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.tour_selected = 1 if self.tour_selected == 1 else self.tour_selected - 1
        elif pyxel.btnp(pyxel.KEY_RETURN):
            if self.focus:
                self.focus = False
                self.deplace(self.depart, self.tour_selected)
                self.depart = -1
            else:
                self.focus = True
                self.depart = self.tour_selected

    
    def draw(self):
        pyxel.cls(7)
        i = 0
        for tour in self.tours:
            i+=1
            j = 0
            pyxel.rect(800*i/4-185/2, 325, 185, 15, 8 if self.tour_selected == i and j == len(tour.content) else 0) # 25 px de margin-top
            for plateau in tour.content:
                j+=1
                clr = 13
                if self.tour_selected == i and j == len(tour.content) : clr = 11 if self.depart == i else 8
                pyxel.rect(800*i/4-(50+(plateau-1)*30)/2, 300-25*(j-1), 50+(plateau-1)*30, 15, clr)
    
    def start(self):
        print("""
 _   _   ___   _   _ _____ _____ 
| | | | / _ \ | \ | |  _  |_   _|
| |_| |/ /_\ \|  \| | | | | | |  
|  _  ||  _  || . ` | | | | | |  
| | | || | | || |\  \ \_/ /_| |_ 
\_| |_/\_| |_/\_| \_/\___/ \___/
                    - Gatien G.\n\n
       1. Lancer le jeu en console
       2. Lancer le jeu avec une GUI
        """)
        choix = input('\n')
        if choix == '1':
            self.console()
        elif choix == '2':
            self.gui()
        else:
            self.start()
        

    def gui(self):
        pyxel.init(800, 500, "Tour de Hanoi", 60, display_scale=1)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
    
    def console(self):
        while self.tours[2].taille() < self.n:
            os.system('cls' if os.name == 'nt' else 'clear')
            #print(self)
            self.refresh()
            arr = input("déplacer l'anneau de la tour n° ")
            dep = input("vers la tour n° ")
            nb = ["1", "2", "3"]
            if arr in nb and dep in nb:
                self.deplace(int(arr), int(dep))
                self.coup += 1
        print(f"""
        ============
        -- FIN DU JEU --
           en {self.coup} coups
        ============
        """)

jeu = Jeu(5)
jeu.start()
