# SimpleSolitaire

A simple text based version of Solitaire that I made as part of a COMPSCI 130 assignment.

Players can choose between 1 to 14 cards. I set the limit to 14 because in a regular deck of cards, there are 54 cards with 4 suites. Since this is a simplified game of Solitaire with only one suite of cards it makes sense to have 1/4 of the 54 cards found in deck in this game.

## Simplified rules

After shuffling, n piles of cards are laid from top to bottom. The (0) first pile begins with one upturned card and n - 1 downturned cards. The other piles (the tableau piles) are empty are empty at the beginning. An example is shown below.

~~~
0: 6*********
1:
2:
3:
~~~

The tableau piles can be built down according to the numbers of the cards. Partial or complete tableau piles can be moved if they are built down in order. An example is shown below.

from
~~~
0: 2******
1: 5 4 3
2: 6
3:
~~~
to
~~~
0: 2******
1: 
2: 6 5 4 3
3:
~~~

The empty pile can be filled with any card. If the player does not want to move the card of the first pile (0) to any other tableau piles, the player can get a second card and put the original one to the back of the first pile (0). An example is shown below.

from
~~~
0: 6*********
1: 
2: 
3:
~~~
to
~~~
0: 7*********
1: 
2: 
3:
~~~
or
~~~
0: 7********
1: 6
2: 
3:
~~~

The aim of the game is to build up a stack of cards starting from card n - 1 to card 0.

## Difficulties

- Easy
	- For this difficulty there is no shuffling involved.
- Normal
	- I decided to implement the overhand shuffle. In this shuffle, a random portion of the second half of the deck of cards are shifted to the front of the deck. This shuffling method is not very good at producing a random arrangement of the cards and is therefore why it is the base difficulty for this game.
- Hard
	- This difficulty required a shuffle that would be more effective than the overhand shuffle and so I decided to use the riffle shuffle. In this shuffling method the deck of cards is split into two halves and then interweaved with each other.
- Challenging
	- In order to achieve a truly random shuffle, I had to implement the Fisher-Yates shuffle. In this shuffle, we iterate through the deck of cards starting from the last card in the deck. We then assign a random position between 0 to the current iterate. The cards at the current iterate and the random position are then swapped, and the loop continues until we reaches the first card in the deck. Since this shuffle achieves a truly random deck of cards each time, this is the most challenging shuffle in this game of solitaire.