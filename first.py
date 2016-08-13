#!/usr/bin/python3
import numpy as np

class item:
    def __init__(self, value, suit, rank):
        self.display = value 
        self.suit = suit
        self.rank = rank

class poker(object):
    def __init__(self,item):
        self.component = item
        self.cards=[]
        self.suits=['clubs', 'diamonds', 'hearts', 'spades']
        self.values=['3','4','5','6','7', '8', '9', '10', '11', '12', '13', '14', '15']
        self.play_1=[]
        self.play_2=[]
        self.play_3=[]
        
    def creatCards(self):
        self.cards.append(self.component('poker', 'black', 16))
        self.cards.append(self.component('poker', 'red', 17))
        for i in self.suits:
            for j in self.values:
                if (int(j) == 11):
                    temp = self.component('jack', i, 11)
                elif (int(j) == 12):
                    temp = self.component('queen', i, 12)
                elif (int(j) == 13):
                    temp = self.component('king', i, 13)
                elif (int(j) == 14):
                    temp = self.component('ace', i, 14)
                elif(int(j) == 15):
                    temp = self.component('2', i, 15)
                else:
                    temp = self.component(j, i, int(j))
                self.cards.append(temp)
    def print_cards(self):
        p1=sorted(self.play_1, key=lambda state:state.rank, reverse=False)
        p2=sorted(self.play_2, key=lambda state:state.rank, reverse=False)
        p3=sorted(self.play_3, key=lambda state:state.rank, reverse=False)
        print('\n')
        for i in p1:
            print(i.display, end=' ')
        print('\n')
        for i in p2:
            print(i.display, end=' ')
        print('\n')
        for i in p3:
            print(i.display, end=' ')
            
    def distrCards(self):
        agricola = np.random.randint(0, 3)
        temp = self.cards[:]
        for i in range(51):
            position = np.random.randint(0, len(temp))
            if((i%3) == 0):
                self.play_1.append(temp[position])
            elif((i%3) == 1):
                self.play_2.append(temp[position])
            else:
                self.play_3.append(temp[position])
            del temp[position]
        if (agricola == 0):
            for i in temp:
                self.play_1.append(i)
        elif(agricola == 1):
            for i in temp:
                self.play_2.append(i)
        else:
            for i in temp:
                self.play_3.append(i)

result=poker(item)
result.creatCards()
result.distrCards()
result.print_cards()
        
