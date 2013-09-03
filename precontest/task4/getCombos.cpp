#include <iostream>
#include <vector>

using namespace std;

vector<int> people;
vector<int> combination;
int goodCombos = 0;

void checkForGoodCombo(const vector<int>& v) {
    int sum = 0;

    for (vector<int>::const_iterator j=v.begin(); j!=v.end(); ++j)
        sum += *j;

    if (sum == 100)
        ++goodCombos;
}

void combinate(int offset, int k) {
    if (k == 0) {
        checkForGoodCombo(combination);
        return;
    }

    for (int i = offset; i <= people.size() - k; ++i) {
        combination.push_back(people[i]);
        combinate(i+1, k-1);
        combination.pop_back();
    }
}

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

    combinate(0, 6);

    cout << goodCombos << endl;

    return 0;
}
