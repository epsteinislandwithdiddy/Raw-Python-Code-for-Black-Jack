import random
# importing random DO NOT DELETE THIS OR THE CODE DOESNT WORK

def card_dealing():
  card_deck = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Joker', 'Queen', 'King']
  cards = card_deck * 3  #change this if you want to change the size of the deck, x4 is for 52 cards which is standard, its currently 39
  random.shuffle(cards)
  return cards

def ValueForHand(hand):
  values = 0
  for card in hand:
        if card == 'Ace':
            values += 1
        elif card in ['1','2','3','4','5','6','7','8','9','10']:
            values += int(card)
        elif card in ['Joker', 'Queen', 'King']:
            values += 10
  return values

def convertnum(hand):
    value_conversion = {'Ace': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,'6': 6, '7': 7, '8': 8, '9': 9, '10': 10,'Joker': 10, 'Queen': 10, 'King': 10}
    return [value_conversion[card] for card in hand]
    #Ace is only counts for the value "1" for simplicity measures. 

def addtohand(deck, hand):
  if len(deck) > 0:
    card = deck.pop()
    hand.append(card)
  return hand

def playervsdealer():
  deck= card_dealing()
  player_hand = [deck.pop(), deck.pop()]
  dealer_hand = [deck.pop()]


  print('Welcome to the casino. Get ready to win big or lose it all!')
  print('Your starting hand is', player_hand)
  print(f'Your value is ,{convertnum(player_hand)}, and your total is {ValueForHand(player_hand)}')
  print(f'The Dealer value is ,{convertnum(dealer_hand)}, and the total is {ValueForHand(dealer_hand)}')

  while True:
    player_choice = input('Would you like to hit or stand? ')
    if player_choice == 'hit':
      addtohand(deck, player_hand)
      print('Your new hand is', player_hand)
      print(f'Your value is ,{convertnum(player_hand)}, and your total is {ValueForHand(player_hand)}')
      if ValueForHand(player_hand) > 21:
        print('You bust')
        return
    elif player_choice == 'stand':
      break

  while ValueForHand(dealer_hand) < 17:
    addtohand(deck, dealer_hand)
    print("Dealer draws", dealer_hand)
    print(f"The Dealer's hand is {dealer_hand}, total is {ValueForHand(dealer_hand)}")

  player_total = ValueForHand(player_hand)
  dealer_total = ValueForHand(dealer_hand)

  if ValueForHand(dealer_hand) > 21:
    print('Dealer busts')
  elif player_total > dealer_total:
    print('Player wins')
  elif player_total < dealer_total:
    print('Dealer wins')
  else:
    print('Tie')