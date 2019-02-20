#pragma once
#include <string>
#include <vector>
using namespace std;
enum Suit{
	CLUBS,DIAMONDS,HEARTS,SPADES
};
enum Rank {
	TWO=2,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN,JACK,QUEEN,KING,ACE
};
string suitToString(Suit x);
string rankToString(Rank x);

struct CardStruct{
	Suit s;
	Rank r;
};

string toString(CardStruct x);

string toStringShort(CardStruct x);

class Card{
	public:
		void initialize(Suit suit, Rank rank);
		Suit getSuit();
		Rank getRank();
		string toString();
		string toStringShort();
		Card();
		Card(Suit suit, Rank rank);
	private:
		bool valid;
		Suit suit;
		Rank rank;
};

class CardDeck {
	public:
		CardDeck();
		void print();
		void printShort();
		void shuffle();
		Card drawCard();
	private:
		vector<Card> cardvector;
		int currentCardIndex;
		void swap(int a, int b);
};

class Blackjack {
	public:
		bool isAce(Card c);
		int getCardValue(Card c);
		int getPlayerCardValue(Card c);
		int getDealerCardValue(Card c,int dealerHand);
		bool askPlayerDrawCard();
		void drawInitialCards();
		void playGame();

	private:
		CardDeck deck;
		int playerHand;
		int dealerHand;
		int playerCardDrawn;
		int dealerCardDrawn;
};