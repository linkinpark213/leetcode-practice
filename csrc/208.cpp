#include <iostream>
#include <unordered_map>

using namespace std;

struct Node {
    char letter;
    bool isLeaf;
    unordered_map<char, Node*> *children;
    Node() {
        letter = ' ';
        isLeaf = false;
        children = new unordered_map<char, Node*>();
    }
};

class Trie {
    unordered_map<char, Node*> *children;
public:    
    Trie () {
        this->children = new unordered_map<char, Node*>();
    }
    /** Inserts a word into the trie. */
    void insert(string word) {
        Node* ptr;
        unordered_map<char, Node*>* children = this->children;
        for (int i = 0; i < word.size(); i++) {
            if ((*children)[word[i]] == NULL) { 
                (*children)[word[i]] = new Node();
            }
            ptr = (*children)[word[i]];
            ptr->letter = word[i];
            children = ptr->children;
        }
        ptr->isLeaf = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        if (word.size() == 0) return false;
        Node* ptr;
        unordered_map<char, Node*>* children = this->children;
        for (int i = 0; i < word.size(); i++) {
            ptr = (*children)[word[i]];
            if (ptr == NULL) return false;
            children = ptr->children;
        }
        return ptr->isLeaf;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        if (prefix.size() == 0) return true;
        Node* ptr;
        unordered_map<char, Node*>* children = this->children;
        for (int i = 0; i < prefix.size(); i++) {
            ptr = (*children)[prefix[i]];
            if (ptr == NULL) return false;
            children = ptr->children;
        }
        return ptr->children->size() > 0 || ptr->isLeaf;
    }
};

int main() {
    Trie* obj = new Trie();
    obj->insert("word");
    cout << obj->search("word");
    cout << obj->startsWith("wo");
    return 0;
}