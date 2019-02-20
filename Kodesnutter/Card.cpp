#include <iostream>
#include <string>
#include <vector>
#include "Card.h"
using namespace std;

string suitToString(Suit x) {
	switch (x) {
		case CLUBS:
			return "Clubs";
			break;
		case DIAMONDS:
			return "Diamonds";
			break;
		case HEARTS:
			return "Hearts";
			break;
		case SPADES:
			return "Spades";
			break;
		default:
			return "Ugyldig kort";
	}
}

string rankToString(Rank x){
	switch (x){
	case TWO:
		return "Two";
		break;
	case THREE:
		return "Three";
		break;
	case FOUR:
		return "Four";
		break;
	case FIVE:
		return "Five";
		break;
	case SIX:
		return "Six";
		break;
	case SEVEN:
		return "Seven";
		break;
	case EIGHT:
		return "Eight";
		break;
	case NINE:
		return "Nine";
		break;
	case TEN:
		return "Ten";
		break;
	case JACK:
		return "Jack";
		break;
	case QUEEN:
		return "Queen";
		break;
	case KING:
		return "King";
		break;
	case ACE:
		return "Ace";
		break;
	default:
		return "Ugyldig kort";
	}
}

string toString(CardStruct x) {
	string s1 = rankToString(x.r);
	string s2 = suitToString(x.s);
	return s1 + " of " + s2;
}

string toStringShort(CardStruct x){
	string s1 = to_string(x.r);
	string s2 = suitToString(x.s);
		s2 = s2.substr(0, 1);
	return s2+s1;
}

void Card::initialize(Suit suit, Rank rank){
	this->valid = true;
	this->suit = suit ;
	this->rank = rank ;
}

Suit Card::getSuit(){
	return this->suit;
}

Rank Card::getRank(){
	return this->rank;
}

string Card::toString(){
	if (valid == true) {
		string s = suitToString(suit);
		string r = rankToString(rank);
		return r + " of " + s;
	}
	else{
		return "Ugyldig kort";
	}
}

string Card::toStringShort(){
	if (valid == true) {
		string s1 = to_string(this->rank);
		string s2 = suitToString(this->suit);
		s2 = s2.substr(0, 1);
		return s2 + s1;
	}
	else {
		return "Ugyldig kort";
	}
}

Card::Card(){
	valid = false;
}

Card::Card(Suit suit, Rank rank){
	this->suit = suit;
	this->rank = rank;
	valid = true;
}

CardDeck::CardDeck(){
	for (int i = 0; i<4;i++) {
		for (int j = 2; j < 15; j++) {
			Card card((Suit) i,(Rank) j);
			cardvector.push_back(card);
		}
	}
	currentCardIndex=0;
}

void CardDeck::print(){
	for (int i = 0; i <52 ; i++) {
		cout << cardvector[i].toString() << endl;
	}
}

void CardDeck::printShort() {
	for (int i = 0; i < 52; i++) {
		cout << cardvector[i].toStringShort() << endl;
	}
}
void CardDeck::shuffle(){
	
	for (int i = 0; i < 100; i++) {
		int a = rand() % 52;
		int b = rand() % 52;
		swap(a,b);
		
		
	}
}

Card CardDeck::drawCard(){
	int originalIndex = this->currentCardIndex;
	this->currentCardIndex++;
	return cardvector[originalIndex];
}

void CardDeck::swap(int a, int b){
	Card temp = cardvector[a];
	cardvector[a] = cardvector[b];
	cardvector[b] = temp;

}

bool Blackjack::isAce(Card c) {
	if ((c).getRank() == ACE) {
		return true;
	}
	else{
		return false;
	}
}

int Blackjack::getCardValue(Card  c){
	switch ((c).getRank()) {
	case TWO:
		return 2;
		break;
	case THREE:
		return 3;
		break;
	case FOUR:
		return 4;
		break;
	case FIVE:
		return 5;
		break;
	case SIX:
		return 6;
		break;
	case SEVEN:
		return 7;
		break;
	case EIGHT:
		return 8;
		break;
	case NINE:
		return 9;
		break;
	case TEN:
		return 10;
		break;
	case JACK:
		return 10;
		break;
	case QUEEN:
		return 10;
		break;
	case KING:
		return 10;
		break;
	case ACE:
		return -1;
		break;
	}
}

int Blackjack::getPlayerCardValue(Card  c){
	if (isAce(c)){
		cout << "Du kan velge mellom verdien 1 og 11" << endl;
		int x = 0;
		while (x != 1 && x != 11) {
			cin >> x;
		}
		return x;
	}
	else {
		int x = getCardValue(c);
		return x;
	}
}

int Blackjack::getDealerCardValue(Card  c, int dealerHand){
	if (isAce(c) && 11 + dealerHand > 21) {
		return 1;
	}
	else if (isAce(c) && 11 + dealerHand <= 21) {
		return 11;
	}
	else{
		return getCardValue(c);
	}
}

bool Blackjack::askPlayerDrawCard() {
	cout << "Vil du trekke et kort?" << endl;
	cout << "Tast inn 1 for ja eller 0 for nei" << endl;
	int x = 2;
	while (x != 1 && x != 0) {
		cin >> x;
		if (x == 1) {
			return true;
		}
		else if (x == 0) {
			return false;
		}
		else {
			cout << "Skriv inn gyldig svar" << endl;
		}
	}
}

void Blackjack::drawInitialCards() {
	Card kort;
	cout << "Dine to første kort :" << endl;
	kort = this->deck.drawCard();
	this->playerCardDrawn++;
	this->playerHand += getPlayerCardValue(kort);
	cout << kort.toString() << " og ";
	kort = this->deck.drawCard();
	this->playerCardDrawn++;
	this->playerHand += getPlayerCardValue(kort);
	cout << kort.toString() << endl;
	cout << "Dealeren sine to første kort : Hemmelig og ";
	while (dealerHand < 17){
		kort = this->deck.drawCard();
		this->dealerCardDrawn++;
		this->dealerHand += getDealerCardValue(kort,dealerHand);
}

	cout << kort.toString() << endl;
	
	
}

void Blackjack::playGame(){
	Card kort;
	this->deck.shuffle();
	this->drawInitialCards();
	bool svar;
	svar=askPlayerDrawCard();
	while (svar) {
		kort = this->deck.drawCard();
		this->playerCardDrawn++;
		this->playerHand += getPlayerCardValue(kort);
		cout << "Du trakk: " << kort.toString()<<endl;
		svar=askPlayerDrawCard();
	}
	if (playerHand >= dealerHand && playerHand <= 21) {
		cout << "Gratulerer, du vant!" << endl;
	}
	else if(playerHand>21){
		cout << "Beklager, du tapte" << endl;
	}
	else if (playerHand < dealerHand) {
		cout << "Beklager,du tapte" << endl;
	}
}

