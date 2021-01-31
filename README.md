# TaQu Fever
*Yareli Aguilar, Alejandro Martínez, Diego Pérez, Isaac Pimentel, Saúl Puente.*
## Synopsis
It's food time and everyone wants to eat at QTacos!
Take orders and make the perfect taco by using awesome quantum gate ingredients!
In TaQu Fever you are the Master Taquero, who has to recreate what customers order. You start with a QTortilla, which is a qubit in an initial quantum state, then you apply different ingredients made of quantum gates, and what you get is an awesome QTaco, which you can see as a qubit in a final quantum state. If this QTaco is the QTaco the customer ordered, you win one point. Don't forget this is a time trial game! What will be your highest record?

## Basic Principles (technical concepts quantum mechanics and quantum computing)/ en qué lenguaje está programado y si hay algún detalle con la implementación también.


## Motivation/Goals
We want TaQu Fever to be a fun and entertaining quantum game, but also, we want the user to be capable of use and create quantum algorithms, as well as learn about quantum gates and it's effects on the quantum states. By making QTacos, the user, seeing how any ingredient (quantum gate) changes the initial state, adquires experience and motivation to keep making QTacos and do it as fast as he cans to break his own record. With all this, we can say that TaQu Fever is an useful entertaining game with all the posibility to be educational for the user, and also is about delicious quantum food.

## Elements and instructions
TaQu Fever is a single player arcade game with the following elements:
* QTacos: is the restaurant where the game takes place.
* Master Taquero: is the user's character.
* QTortilla: initial quantum state.
* Customer: is the client of the restaurant.
* Order: is the expected state the customer ask for (the expected QTaco).
* Ingredients:
  * H - desHebrada: is the Hadamard gate applied to the quantum state.
  * X - Xicken: is the Pauli X gate applied to the quantum state.
  * Y - onYon: is the Pauli Y gate applied to the quantum state.
  * Z - Zilantro: is the Pauli Z gate applied to the quantum state.
  * CNOT - pasNOT: is the CNOT gate applied to the quantum state.
* QTaco: final quantum state.
* Countdown: 60 second time bar (adjustable).
* Basket: allows to remove the ingredients from the taco.
#### How to play the game?
The player will start with 3 QTortillas in a plate. As we explained in the synopsis, each QTortilla has an initial quantum random state, which the user can see. The player will be recieving orders from the customers, that indicate the final state they want to have (the QTaco represented as a quantum state). The user has to build the QTacos according to the specification the customer asks for, and obtain the expected quantum state of the QTaco. Each ingredient applies a different gate to the quantum state. Once you put an ingredient to the taco, you cannot erase it. You win a point whenever you get the correct QTaco.
Since it's a time trial game, you will have 60 seconds to complete as much correct QTacos as you can (you can also set the time limit).

## Demostrations

## ToDo
#### Proposals for future work:
* Better graphics.
* More dificulty modes.
* More variation of ingredients (quantum gates).
* Variable screen size and fullscreen implementation.

## instrucciones
* algún detalle en la implementación ????
* a clear title for your project,
* a short abstract,
* the motivation/goals for your project,
* a description of the work you did, and
* proposals for future work.
