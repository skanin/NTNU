from random import *

avaliableCards = ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10]

dealerScore = 0
playerScore = 0


def main():
    dealerCards = []
    playerCards = []
    global playerScore
    global dealerScore

    won = False

    while not won:
        for i in range(2):
            dealerCards.append(pickCard())

        for i in range(2):
            playerCards.append(pickCard())

        if checkRealBlackJack(playerCards):
            print("You won!")
            break


        playerScore = calcScore(playerCards)
        dealerScore = calcScore(dealerCards)

        printScores(playerCards, dealerCards, playerScore, dealerScore)

        answer = input("Do you want another card? : ")
        if answer == "no":
            checkHighestScore(playerScore, dealerScore)
            break
        else:
            while answer == "yes":
                playerCards.append(pickCard())
                playerScore = calcScore(playerCards)
                if playerScore > 21:
                    print("You lost!")
                    break
                printScores(playerCards, dealerCards, playerScore, dealerScore)
                answer = input("Do you want another card?: ")



def printScores(playerCards, dealerCards, playerScore, dealerScore):
    print("Dealer cards are " + str(dealerCards[0]) + " and ?")
    print("Dealer score: " + str(dealerScore))
    print("Dealer: " + str(dealerCards))
    print("Your score is: " + str(playerScore))
    print("You: " + str(playerCards))


def checkHighestScore(playerScore, dealerScore):
    if playerScore > 21 > dealerScore:
        print("You lost!")
    elif playerScore < 21 < dealerScore:
        print("You won!")
    elif playerScore > dealerScore:
        print("You won!")
    elif dealerScore > playerScore:
        print("You lost!")



def calcScore(liste):
    score = 0

    for i in range(0, len(liste)):
        if not isinstance(liste[i], int):
            if liste[i] == 'A' and not (score + 13 > 21):
                score += 13
                continue
            elif liste[i] == 'A' and (score + 13 > 21):
                score += 1
                continue
            else:
                score += 10
        else:
            score += liste[i]

    return score


def checkRealBlackJack(liste):
    if len(liste) == 2:
        if not 'A' in liste:
            return False
        else:
            if 'K' in liste or 'Q' in liste or 'J' in liste:
                return True
    return False


def pickCard():
    return avaliableCards[randint(0, len(avaliableCards) - 1)]

main()
