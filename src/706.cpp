//
// Created by linkinpark213 on 5/21/19.
//

#include <iostream>
#include <vector>

using namespace std;

class MyHashMap {
    vector<int> keys;
    vector<int> values;
public:
    /** Initialize your data structure here. */
    MyHashMap() {

    }

    int find(int key) {
        int i = -1;
        for (i = 0; i < keys.size(); i++) {
            if (keys[i] == key) break;
        }
        if (i == keys.size()) return -1;
        return i;
    }

    /** value will always be non-negative. */
    void put(int key, int value) {
        int i = find(key);
        if (i > 0) {
            values[i] = value;
        } else {
            keys.push_back(key);
            values.push_back(value);
        }
    }


    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int i = find(key);
        if (i < 0)
            return -1;
        return values[i];
    }

    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int i = find(key);
        if (i < 0)
            return;
        keys.erase(keys.begin() + i);
        values.erase(values.begin() + i);
    }
};

int main() {
    MyHashMap hashMap;
    hashMap.put(1, 1);
    hashMap.put(2, 2);
    cout << hashMap.get(1);            // returns 1
    cout << hashMap.get(3);            // returns -1 (not found)
    hashMap.put(2, 1);          // update the existing value
    cout << hashMap.get(2);            // returns 1
    hashMap.remove(2);          // remove the mapping for 2
    cout << hashMap.get(2);            // returns -1 (not found)
}