#include <iostream>
#include <unordered_map>
#include <string>
 
using namespace std;
 
int main() {
    int n, m;
    cin >> n >> m;
 
    // maps each first-language word to the word we will write
    unordered_map<string, string> words;
 
    // read the dictionary
    for (int i = 0; i < m; i++) {
        string first, second;
        cin >> first >> second;
 
        // if the second-language word is shorter,
        // use it. Otherwise (including equal length),
        // keep the first-language word.
        if (second.length() < first.length()) {
            words[first] = second;
        } else {
            words[first] = first;
        }
    }
 
    // process the lecture
    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
 
        cout << words[word];
 
        // avoid printing an extra space at the end
        if (i != n - 1) {
            cout << " ";
        }
    }
 
    cout << endl;
 
    return 0;
}