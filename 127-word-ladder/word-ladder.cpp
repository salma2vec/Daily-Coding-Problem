class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());

        if (wordSet.find(endWord) == wordSet.end()) {
            // The endWord is not in the wordList, so no transformation sequence is possible.
            return 0;
        }

        queue<string> q;
        q.push(beginWord);
        int level = 0;

        while (!q.empty()) {
            int size = q.size();
            level++;

            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();

                for (int j = 0; j < word.length(); j++) {
                    char originalChar = word[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == originalChar) {
                            continue;
                        }
                        word[j] = c;

                        if (word == endWord) {
                            return level + 1;
                        }

                        if (wordSet.find(word) != wordSet.end()) {
                            q.push(word);
                            wordSet.erase(word);
                        }

                        word[j] = originalChar;
                    }
                }
            }
        }

        return 0; // No transformation sequence found.
    }
};
