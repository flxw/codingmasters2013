#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    bool goOn = true;
    int goodCombos = 0;
    int skill;

    vector<int> v;

    do {
        if (cin >> skill) {
            v.push_back(skill); 
        } else {
            goOn = false;
        }
    } while (goOn);

// create selection vector and populate it
    vector<bool> sv(v.size());
    fill(sv.begin() + sv.size() - 6, sv.end(), true);

    do {
        int sum = 0;

        for (int i = 0; i < sv.size(); ++i) {
            if (sv[i]) {
                sum += v[i];
            }
        }

        if (sum == 100)
            goodCombos++;
    } while (std::next_permutation(sv.begin(), sv.end()));

    cout << goodCombos << endl;

    return 0;
}
