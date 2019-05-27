//
// Created by linkinpark213 on 5/27/19.
//
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Solution {
    vector<int> maxSort(vector<int> &deck) {
        int temp;
        for (int i = 0; i < deck.size(); i++) {
            for (int j = deck.size() - 1; j > i; j--) {
                if (deck[j] > deck[j - 1]) {
                    temp = deck[j];
                    deck[j] = deck[j - 1];
                    deck[j - 1] = temp;
                }
            }
        }
        return deck;
    }

public:
    vector<int> deckRevealedIncreasing(vector<int> &deck) {
        maxSort(deck);
        deque<int> ans;
        ans.push_front(deck[0]);
        for (int i = 1; i < deck.size(); i++) {
            ans.push_front(ans.back());
            ans.pop_back();
            ans.push_front(deck[i]);
        }
        return vector<int>(ans.begin(), ans.end());
    }
};

int main() {
    Solution solution;
    int numbers[] = {17, 13, 11, 2, 3, 5, 7};
    vector<int> deck(numbers, numbers + sizeof(numbers) / sizeof(int));
    vector<int> ans = solution.deckRevealedIncreasing(deck);
    for (int i : ans)
        cout << i << " ";
}