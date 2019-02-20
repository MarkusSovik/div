#include <iostream>
#include "Card.h"
#include <string>
#include <time.h>
using namespace std;

int main() {
	srand(time(0));
	
	Blackjack b;
	b.playGame();
	system("Pause");
}