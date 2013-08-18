# include <iostream>

using namespace std;

int main (int argc, char** argv) {
    int exclamations;
    bool goOn = true;

    do {
        if (cin >> exclamations) {
            cout << "Hello world";

            for (int i = 0; i < exclamations; ++i) {
                cout << "!";
            }

            cout << endl;
        } else {
            goOn = false;
        }
    } while (goOn);

    return 0;
}
