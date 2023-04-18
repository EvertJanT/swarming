import tkinter as tk
from tkinter import TclError
import time, random, math, sys
import numpy as np
from tkinter import IntVar
global GC, PR, grenzen

class Scherm1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title('Zwerm')
        master.geometry("250x700+400+50")
        self.logo = tk.PhotoImage(file="galaxy.gif")
        self.logo = tk.PhotoImage(file="bird.gif")
        self.label = tk.Label(image=self.logo).pack()
        self.button1 = tk.Button(self.frame, text = 'Nieuw Scherm', width = 25, command = self.new_window)
        self.button1.pack()
        global gebruiker_invoer1 
        gebruiker_invoer1 = 700
        label1 = tk.Label(self.frame, text='hoogte')
        label1.pack()
        self.invoerSpinner1 = tk.Spinbox(self.frame,
                                        from_=650,
                                        to=2000,
                                        increment=25,
                                        textvariable = gebruiker_invoer1,
                                        command=self.invoer,
                                        wrap=True)
        self.invoerSpinner1.pack()
        global gebruiker_invoer2 
        gebruiker_invoer2 = 500
        label2 = tk.Label(self.frame, text='breedte')
        label2.pack()
        self.invoerSpinner2 = tk.Spinbox(self.frame,
                                        from_=450,
                                        to=2000,
                                        increment=25,
                                        textvariable = gebruiker_invoer2,
                                        command=self.invoer,
                                        wrap=True)
        self.invoerSpinner2.pack()
        global gebruiker_invoer3
        gebruiker_invoer3 = 9.8
        label3 = tk.Label(self.frame, text='groeps-cohesie')
        label3.pack()
        self.invoerSpinner3 = tk.Spinbox(self.frame,
                                        from_= 1.0,
                                        to=100.0,
                                        increment=5,
                                        textvariable = gebruiker_invoer3,
                                        command=self.invoer,
                                        wrap=True)
        self.invoerSpinner3.pack()
        global gebruiker_invoer3a
        gebruiker_invoer3a = 2.0
        label3a = tk.Label(self.frame, text='persoonlijke-ruimte')
        label3a.pack()
        self.invoerSpinner3a = tk.Spinbox(self.frame,
                                        from_= 1.0,
                                        to=10.0,
                                        increment=1,
                                        textvariable = gebruiker_invoer3a,
                                        command=self.invoer,
                                        wrap=True)
        self.invoerSpinner3a.pack()

        global gebruiker_invoer4
        gebruiker_invoer4 = IntVar()
        gebruiker_invoer4.set(0)
        self.checkbox1 = tk.Checkbutton(self.frame, text='obstakel',variable=gebruiker_invoer4,
                            onvalue=1, offvalue=0, command=self.invoer)
        self.checkbox1.pack()



        
        self.button2 = tk.Button(self.frame, text='stop', width = 25)
        self.button2['command'] = self.button_clicked
        self.button2.pack()
        self.frame.pack()

    def invoer(self):
        global gebruiker_invoer1, gebruiker_invoer2, gebruiker_invoer3, gebruiker_invoer3a, gebruiker_invoer4
        huidige_invoer1 = self.invoerSpinner1.get()
        huidige_invoer2 = self.invoerSpinner2.get()
        huidige_invoer3 = self.invoerSpinner3.get()
        huidige_invoer3a = self.invoerSpinner3a.get()
        gebruiker_invoer1 = huidige_invoer1
        gebruiker_invoer2 = huidige_invoer2
        gebruiker_invoer3 = huidige_invoer3
        gebruiker_invoer3a = huidige_invoer3a
        
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Scherm2(self.newWindow)
    def button_clicked(self):
        vogel_lijst = []
        try:
            self.master.destroy()
        except TclError:
            print('error')
            pass

class Scherm2:
    def __init__(self, master):
        global breedte, hoogte, GC, PR, grenzen
        breedte = 700
        hoogte  = 500
        grenzen = []
        grens_straal = 30
        hoogte = int(gebruiker_invoer1)
        breedte = int(gebruiker_invoer2)
        GC = gebruiker_invoer3
        PR = gebruiker_invoer3a
        #obstakel = gebruiker_invoer4
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title('canvas')
        master.geometry(str(breedte) + 'x'+ str(hoogte) + '+650+50')
        self.quitButton = tk.Button(self.frame, text = 'Stop', width = 25,
                                    command = self.close_windows)
        self.quitButton.pack()
        mijnCanvas = tk.Canvas(self.frame, bg="white", height=hoogte, width=breedte)
        mijnCanvas.pack()
        while gebruiker_invoer4.get() == 1:
            grenzen = [[100,100],[100,300],[100,600],[100,900],[300,100],[600,100],[900,100],[600,300],
                       [900,300],[900,900],[300,300],[300,600],[300,900],[600,100],[600,300],[600,900],
                       [900,100],[900,300],[900,600],[275,700],[250,700],[800,200],[250,700],[100,100]]

            grenzen = [[100,100],[300,300],[600,600],[900,900],[1200, 1200]] 
            for grens in grenzen:
                mijnCanvas.create_oval(int(grens[0])-grens_straal, int(grens[1])-grens_straal, int(grens[0])+grens_straal, int(grens[1])+grens_straal, fill="#0064FF", width=0)
            break
        self.frame.pack()    
            
   
        class Vogel:
            global breedte, hoogte
            leider_vogel_random_snelheids_verandering = 0.2
            grens_reactie_snelheid_verandering = 0.02
            leider_max_snelheid = 3.0
            max_snelheid = 10
            leider_grens_reactie = 200
            grens_reactie = 100
            def __init__(self, kleur):
                self.size=3
                self.x = random.randrange(15,breedte-15)
                self.y =random.randrange(15,hoogte-40)
                self.vorm = mijnCanvas.create_oval(self.x-self.size, self.y -self.size,self.x +self.size,self.y+self.size, fill=kleur)
                self.vx = random.randrange(-2, 2)
                self.vy = random.randrange(-2, 2)
            def update_zijkanten(self):
                mijnCanvas.move(self.vorm, self.vx, self.vy)
                pos = mijnCanvas.coords(self.vorm)
                if pos[2] >= (breedte-10) or (pos[0] ) <= 10:
                    self.vx *= -1
                if pos[3] >= (hoogte-40) or (pos[1]) <= 10:
                    self.vy *= -1
            def update_beweging(self):
                mijnCanvas.move(self.vorm, self.vx, self.vy)
                snelheid = math.sqrt(self.vx*self.vx + self.vy*self.vy)
                if (snelheid > max_snelheid):
                    self.vx = self.vx * max_snelheid/snelheid
                    self.vy = self.vy * max_snelheid/snelheid

                if (self.x < grens_reactie):
                    self.vx += grens_reactie_snelheid_verandering
                if (self.y < grens_reactie):
                    self.vy += grens_reactie_snelheid_verandering
                if (self.x > breedte - grens_reactie):
                    self.vx -= grens_reactie_snelheid_verandering
                if (self.y > hoogte - grens_reactie):
                    self.vy -= grens_reactie_snelheid_verandering
                
                # vogels bewegen weg van grenzen



        class Leider_vogel:
            global breedte, hoogte
            leider_vogel_random_snelheids_verandering = 0.2
            grens_reactie_snelheid_verandering = 0.2
            leider_max_snelheid = 3.0
            leider_grens_reactie = 200

            def __init__(self, kleur):
                self.size=1
                self.x = random.randrange(15,breedte-15)
                self.y =random.randrange(15,hoogte-15)
                self.vorm = mijnCanvas.create_oval(self.x-self.size, self.y -self.size,self.x +self.size,self.y+self.size, fill=kleur)
                self.vx = random.randrange(-2, 2)
                self.vy = random.randrange(-2, 2)
            def update_zijkanten(self):
                try:
                    mijnCanvas.move(self.vorm, self.vx, self.vy)
                except TclError:
                    sys.exit()
                    pass
                pos = mijnCanvas.coords(self.vorm)
                if pos[2] >= (breedte-10) or (pos[0] ) <= 10:
                    self.vx *= -1
                if pos[3] >= (hoogte-40) or (pos[1]) <= 10:
                    self.vy *= -1
            def update_beweging(self):
                mijnCanvas.move(self.vorm, self.vx, self.vy)
                if (self.x < leider_grens_reactie):
                    self.vx += grens_reactie_snelheid_verandering
                if (self.y < leider_grens_reactie):
                    self.vy += grens_reactie_snelheid_verandering
                if (self.x > breedte - leider_grens_reactie):
                    self.vx -= grens_reactie_snelheid_verandering
                if (self.y > hoogte - leider_grens_reactie):
                    self.vy -= grens_reactie_snelheid_verandering

                self.vx += random.uniform(-leider_vogel_random_snelheids_verandering, leider_vogel_random_snelheids_verandering)
                self.vy += random.uniform(-leider_vogel_random_snelheids_verandering, leider_vogel_random_snelheids_verandering)
        
                # Cap maximale snelheid
                snelheid = math.sqrt(self.vx*self.vx + self.vy*self.vy)
                if (snelheid > leider_max_snelheid):
                    self.vx = self.vx * leider_max_snelheid/snelheid
                    self.vy = self.vy * leider_max_snelheid/snelheid

                
                self.x += self.vx
                self.y += self.vy


        vogel_lijst = []
        LV = Leider_vogel('white')

        for k in range(150):
            vogel_lijst.append(Vogel('red'))

        #parameter
        max_snelheid = 10

        grens_reactie = 100
        leider_grens_reactie = 200
        grens_reactie_snelheid_verandering = 0.2

        minimale_afstand= 3.0
        minimale_afstand= float(PR)
        vergelijk_snelheids_venster = 5
        vergelijk_snelheids_venster = float(GC)

        leider_vogel_random_snelheids_verandering = 0.2
        leider_max_snelheid = 2.0

        while True:
            LV.update_zijkanten()                
            LV.update_beweging()
            for vogel1 in vogel_lijst:
                leider_diffx = LV.x - vogel1.x
                leider_diffy = LV.y - vogel1.y 
                vogel1.vx += 0.0007 * leider_diffx
                vogel1.vy += 0.0007 * leider_diffy
                vogel1.x += vogel1.vx
                vogel1.y += vogel1.vy

                # vogels bewegen weg van andere nabije vogels
                # bereken ook de gemiddelde snelheid van vogels in een groter gebied
                # bereken gemiddelde snelheid van andere vogels
                avxtotal = 0
                avytotal = 0
                avcount = 0
                for vogel2 in vogel_lijst:
                    if (vogel1 != vogel2):
                        dx = vogel2.x - vogel1.x
                        dy = vogel2.y - vogel1.y
                        afstand = math.sqrt(dx*dx + dy*dy)
                        if (afstand < minimale_afstand):
                            vogel1.vx -= dx * 0.5
                            vogel1.vy -= dy * 0.5
                        if (afstand < vergelijk_snelheids_venster):
                            avxtotal += vogel2.vx
                            avytotal += vogel2.vy
                            avcount += 1
                # Match naar de gemiddelde snelheid van vogels die dichtbij zijn
                    
                if (avcount != 0):
                    avx = avxtotal / avcount
                    avy = avytotal / avcount
                    vogel1.vx = (0.90 * vogel1.vx + 0.1 * avx)
                    vogel1.vy = (0.90 * vogel1.vy + 0.1 * avy)                

		# bots tegen obstakels en vertraag
                for grens in grenzen:
                        dx = grens[0] - vogel1.x
                        dy = grens[1] - vogel1.y
                        afstand = math.sqrt(dx*dx + dy*dy)
                        if (afstand < grens_straal + 15):
                                vogel1.vx -= dx * 0.1
                                vogel1.vx *= 0.6
                                vogel1.vy -= dy * 0.1
                                vogel1.vy *= 0.6

                vogel1.x += vogel1.vx
                vogel1.y += vogel1.vy
                vogel1.update_zijkanten()                
                vogel1.update_beweging()

            self.frame.update()

    def close_windows(self):
        vogel_lijst = []
        try:
            self.master.destroy()
        except TclError:
            print('error')
            pass

def main(): 
    root = tk.Tk()
    app = Scherm1(root)
    root.mainloop()
    

if __name__ == '__main__':
    main()
