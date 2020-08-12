import random
suits = ["spade", "club", "heart", "diamond"]
faces = ["6", "7", "8", "9", "10", "J", "Q", "K", "T"]
pointToFaces = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "Q": 3, "K": 4, "T": 11} 
cards = []
cardsCount = cards
for suit in suits:
    for face in faces:
        cards.append((suit, face))
numberOfPoints = 0
random.shuffle(cards)

def getPoint(card1):
    cardFace = card1[1]
    pointToFaces[cardFace]
    return pointToFaces[cardFace]
while True:
    random.shuffle(cards)
    card1 = random.choice(cards)
    card1 = cards.pop()
    message = input(str("Засчитать или взять новую карту: "))
    if message == "get":
        result = getPoint(card1)
        print('Карта ', card1)
        print(result)
        card = cards.pop()
        print(cardsCount)
        random.choice(cards) 
        numberOfPoints += result
        print('Point ', numberOfPoints)
    if message == "count":
        print('Игра закончена. Очки: ', numberOfPoints)
        break
    if numberOfPoints == 21:
        print("Вы выиграли!")
        break
    if numberOfPoints > 21:
        print('Конец игры! Вы проиграли!')
        break

    
