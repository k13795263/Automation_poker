#!/usr/bin/python3

def straigth (poker):
    cards = sorted(poker[:])
    source = [15, 16, 17]
    if(len(cards) < 5):
        return(0)
        
    for i in source:
        if i in cards:
            return(0)
            
    length = len(cards) - 1
    while(length > 0):
        if((cards[length] - cards[length -1]) == 1):
            length -= 1
        else:
            return(0)
    return 1
    
def pairStraigth(poker):
    cards = sorted(poker[:])
    source = [15, 16, 17]
    length = len(cards)
    if (length < 6):
        return 0
    if ((length % 2) != 0):
        return 0
    for i in source:
        if i in cards:
            return 0
    setCards = set(cards)
    if(length != (2 * len(setCards))):
        return 0
    else:
        p = 0
        while(p < (length -2)):
            if((cards[p] == cards[p+1]) and (cards[p+2] - cards[p]) == 1):
                p += 2
            else:
                return 0
    return 1

def airplane(poker):
    cards = sorted(poker[:])
    if (len(cards) < 8):
        return 0
    setCard = set(cards)
    cardList =[]
    while(len(setCard) > 0):
        key = setCard.pop()
        n = 0
        for i in cards:
            if (key == i):
                n += 1
        if (n == 3):
            cardList.append(key)
        elif(n > 3):
            return (0)
    if ((3 * len(cardList) + len(cardList)) != len(cards)):
        return (0)
    length = len(list) - 1
    while(length > 0):
        if((list[length] - list[length -1]) == 1):
            length -= 1
        else:
            return(0)
    return 1

def pairOffour(poker):
    cards = sorted(poker[:])
    if(len(cards) != 6):
        return 0
    setCard = set(cards)
    while(len(setCard) > 0):
        key = setCard.pop()
        n = 0
        for i in cards:
            if (key == i):
                n += 1
        if (n == 4):
            return 1
    return 0

def signal(poker):
    if (len(poker) == 1):
        return 1
    else:
        return 0

def pair(poker):
    if(len(poker) != 2):
        return 0
    else:
        if(poker[0] != poker[1]):
            return 0
    return 1
    
def fullHouse(poker):
    if(len(poker) != 3):
        return 0
    else:
        if(poker[0] == poker[1] == poker[2]):
            return 1
        else:
            return 0
            
def oneOfFullHouse(poker):
    cards = sorted(poker[:])
    if(len(poker) != 4):
        return 0
    else:
        setCard = set(cards)
        while(len(setCard) > 0):
            key = setCard.pop()
            n = 0
            for i in cards:
                if (key == i):
                    n += 1
            if (n == 3):
                return 1
    return 0

def bomb(poker):
    if(len(poker) != 4):
        return 0
    else:
        if(poker[0] == poker[1] == poker[2] == poker[3]):
            return 1
        else:
            return 0
            
def nuclear(poker):
    if(len(poker) != 2):
        return 0
    else:
        if((poker[0] + poker[1]) != 33):
            return 0
    return 1
