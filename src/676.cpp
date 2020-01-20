#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class MagicDictionary {
    unordered_set<string> words;
public:
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        for (auto it = dict.begin(); it != dict.end(); it++)
            words.insert(*it);
    }

    bool similar(string word1, string word2) {
        if (word1.size() != word2.size()) return false;
        int diff = 0;
        for (int i = 0; i < word1.size(); i++) 
            if (word1[i] != word2[i]) diff++;
        return diff == 1;
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        for (auto it = this->words.begin(); it != this->words.end(); it++)
            if (similar(word, *it)) return true;
        return false;
    }
};

int main() {
    MagicDictionary* obj = new MagicDictionary();
    obj->buildDict({"hello", "leetcode"});
    cout << obj->search("hell");
    return 0;
}