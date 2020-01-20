#include <iostream>

using namespace std;

class Solution {
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        return longUrl;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return shortUrl;
    }
};

int main() {
    Solution solution;
    cout << solution.decode(solution.encode("http://www.baidu.com"));
    return 0;
}