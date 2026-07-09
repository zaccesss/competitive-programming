#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct Team {
    string name;
    int points = 0;
    int goalsFor = 0;
    int goalsAgainst = 0;
};

int main() {

    int n;
    cin >> n;

    vector<Team> teams(n);
    unordered_map<string, int> id;

    // read the team names
    for (int i = 0; i < n; i++) {
        cin >> teams[i].name;
        id[teams[i].name] = i;
    }

    // process every match
    for (int i = 0; i < n * (n - 1) / 2; i++) {

        string match;
        cin >> match;

        int g1, g2;
        char colon;
        cin >> g1 >> colon >> g2;

        int dash = match.find('-');

        string t1 = match.substr(0, dash);
        string t2 = match.substr(dash + 1);

        int a = id[t1];
        int b = id[t2];

        teams[a].goalsFor += g1;
        teams[a].goalsAgainst += g2;

        teams[b].goalsFor += g2;
        teams[b].goalsAgainst += g1;

        // update the points
        if (g1 > g2) {
            teams[a].points += 3;
        }
        else if (g1 < g2) {
            teams[b].points += 3;
        }
        else {
            teams[a].points++;
            teams[b].points++;
        }
    }

    // sort by the tournament rules
    sort(teams.begin(), teams.end(), [](const Team &a, const Team &b) {

        if (a.points != b.points)
            return a.points > b.points;

        int diffA = a.goalsFor - a.goalsAgainst;
        int diffB = b.goalsFor - b.goalsAgainst;

        if (diffA != diffB)
            return diffA > diffB;

        return a.goalsFor > b.goalsFor;
    });

    vector<string> qualified;

    // collect the qualified teams
    for (int i = 0; i < n / 2; i++) {
        qualified.push_back(teams[i].name);
    }

    // output in lexicographical order
    sort(qualified.begin(), qualified.end());

    for (string name : qualified) {
        cout << name << "\n";
    }

    return 0;
}