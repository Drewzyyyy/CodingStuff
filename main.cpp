/* Created by: Andrew Louis Hermo
   Project name: Programming Exercise 1
   Subject: CMSC 124-H
   Affiliation: University of the Philippines Mindanao
*/
#include <iostream>
#include <stdlib.h>
#include <limits>
#include <iostream>
#include <ios>
#include "validate.h"

using namespace std;

void Display(); // Displays the main menu
void ProgDesc(); // Displays the Program Description
void Eval(char c); // Evaluates the expression inputted by the user and outputs the answer

int main(){
	char choice;
	while(1){
		system("cls");	// Clears the console
		Display();	// Main menu
		cin>>choice;
		cin.ignore(numeric_limits<streamsize>::max(),'\n');
		cin.clear();
		if(choice=='p'||choice=='P') ProgDesc();
		else if(choice=='e'||choice=='E') Eval(choice);
		else if(choice=='x'||choice=='X') break;
		else cout<<"Invalid choice"<<endl;
		system("pause");
	}
	return 0;
}

void Display() {	// Displays the main menu
	cout<<"Welcome to this Expression Evaluator program! Please choose an action to\nperform..."<<endl;
	cout<<"\t[P] Program Description"<<endl;
	cout<<"\t[E] Evaluate Expression"<<endl;
	cout<<"\t[X] Exit"<<endl;
	cout<<"Choice: ";
}

void ProgDesc(){	// Displays the Program Description
	cout<<"Developer: Andrew Louis R. Hermo - 2019-01621"<<endl;
	cout<<"Project started: March 17, 2021\tProject finished: March 18, 2021"<<endl;
	cout<<"[E] Evaluates the arithemetic expressions inputted by the user, and outputs the answer"<<endl;
	cout<<"[X] Exits the program"<<endl;
	cout<<"Sole Programmer: Andrew Louis R. Hermo"<<endl;
	cout<<"LinkedIn: https://www.linkedin.com/in/alrhermo/"<<endl;
}

void Eval(char c){	// Evaluates the expression inputted by the user and outputs the answer
	string exp;	// Stores the expression inputted by the user
	char choice;
	while(1){
		cout<<"Input expression: ";
		getline(cin,exp);
		if(!checkExp(exp)) cout<<"Invalid infix expression"<<endl;
		else{
			exp = ExpAdjust(exp);
			cout<<"Your infix expression: "<<exp<<endl;
			exp = toPostfix(exp);
			cout<<"Converted to postfix: "<<exp<<endl;
			EvalPost(exp);
		}
		cout<<"[1] Input again"<<endl;
		cout<<"[0] Return to main menu"<<endl;
		cout<<"Choice:";
		cin>>choice;
		if(choice!='1') return;
		cin.ignore(numeric_limits<streamsize>::max(),'\n');
		cin.clear();
		system("cls");
		Display();
		cout<<c<<endl;
	}
}
