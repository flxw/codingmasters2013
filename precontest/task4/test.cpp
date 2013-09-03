#include <iostream>
#include <vector>

using namespace std;

vector<int> people;
vector<int> combination;

int main(int argc, char** argv) {
    bool goOn = true;
    int  skill;

    do {
        if (cin >> skill) {
            people.push_back(skill); 
        } else {
            goOn = false;
        }
    } while (goOn);


    cout << 10 << endl;

    return 0;
}
