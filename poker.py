from tkinter import *
from PIL import Image, ImageTk
import random
random.seed()
import pokerlogic as pk

#function to display the image for each card in hand
def displayHand(hand_in, row_to_display_in):
    for i in range(5):
        #open image
        card_name = str(hand[i]['rank']) + ' of ' + str(hand[i]['suit'])
        card = Image.open('/Users/anshitakhare/Documents/Projects to Upload/poker/cards/' + str(hand[i]['rank']) + '_of_' + str(hand[i]['suit']) + '.png')
        
        #resize image
        card_resized = card.resize((150, 218))

        #output the card
        tkcard = ImageTk.PhotoImage(card_resized)

        label = Label(window, image=tkcard)
        label.image = tkcard
        label.grid(row=row_in, column=i*2)

#generate deck        
deck = pk.generateDeck()       
       
human_hand = []
computer_hand = []

#draw each player's hand
for i in range(5):
    card = random.choice(deck)
    deck.remove(card)
    human_hand += [card]

    card = random.choice(deck)
    deck.remove(card)
    computer_hand += [card]


window = Tk()
window.geometry('770x900')
window.title('Pyker')


discardLabel = Label(window, text='Which cards would you like to discard and replace?')
discardLabel.grid(row=0, columnspan= 10)

#display human hand
displayHand(human_hand, 1)  

#create checkbuttons to allow user to select which cards to discard
var = ['var0','var1', 'var2', 'var3', 'var4' ]
checkbuttons = ['checkButton0', 'checkButton1', 'checkButton2', 'checkButton3', 'checkButton4']
for i in range(5):
    card = card_name = str(human_hand[i]['rank']) + ' of ' + str(human_hand[i]['suit'])
    var[i]= IntVar()

    checkbuttons[i] = Checkbutton(window, text=card_name, variable=var[i], onvalue=1, offvalue=0)
    checkbuttons[i].grid(row=2, column = i*2)

#when submit is clicked:
def onSubmitClick():

    #remove selected cards from human hand
    remove_list = []
    for i in range(5):
        if var[i].get() == 1:
            human_hand.pop(i)
            card = random.choice(deck)
            deck.remove(card)
            human_hand.insert(i, card)
        
    submitButton['state'] = DISABLED

    #find out what kind of hand each player has and display it
    kind = pk.whatKindIsThisHand(human_hand)
    yourLabel = Label(window, text='Your Hand: You have a ' + kind)
    yourLabel.grid(row=4, columnspan= 10)

    displayHand(human_hand, 5)

    kind = pk.whatKindIsThisHand(computer_hand)
    computerLabel = Label(window, text='Computer Hand: Computer has a ' + kind)
    computerLabel.grid(row=6, columnspan= 10)

    displayHand(computer_hand, 7)

    #find out who won and display that
    winner = pk.winningHand(human_hand, computer_hand)
    if winner[0] == 1:
        result = 'You win!'        
    elif winner[0] == 2:
        result = 'Computer wins!'   
    else:
        result = 'It\'s a tie!'

    if winner[1] != '':
        result += '\n' + winner[1]

    resultLabel = Label(window, text=result)
    resultLabel.grid(row=8, columnspan= 10)
    
submitButton = Button(window, text='Submit', command=lambda:onSubmitClick())
submitButton.grid(row=3, columnspan=10)


window.mainloop()
        














