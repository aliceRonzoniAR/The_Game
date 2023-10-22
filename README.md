# The_Game
Computer version of the card game called "The Game" 

## RULES
At each turn the player has to choose a card from their hand and play it on a pile following these rules:
- In D1 and D2 numbers have to decrease (from 100 to 2)
- In U1 and U2 numbers have to increse (from 1 to 99)

  On the increasing pile numbers have always to be incresing. Example: 1-3-11-45-78-90
  Same thing for decreasing pile.

  The only exception to these rules is when there is a difference of exactly ten with the card the player wants to play and the card on the pile.
  Let's consider the increasing pile. If the card is exactly 10 numbers smaller than the card on the pile, the player can play that card on that pile.
  Example: the player has 45 in hand and on U1 there is 55. Following the rules, the player shouldn't play 45 on that pile because we need the pile to increse. But since the difference is exactly of 10, the player can go down.
  Same thing happens for the decreasing pile.
  Example: the player wants to play 55 on D1 where there is 45. Since the difference is of exactly 10 numbers can growth, even if the pile is going down.

The game ends when the player cannot play anycard or when all the cards have been played.
