class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<char>> rows(9);
        vector<set<char>> cols(9);
        vector<set<char>> subgrids(9);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char cell = board[i][j];
                if (cell == '.') {
                    continue;
                }

                if (rows[i].count(cell) || cols[j].count(cell) || subgrids[i / 3 * 3 + j / 3].count(cell)) {
                    return false;
                }

                rows[i].insert(cell);
                cols[j].insert(cell);
                subgrids[i / 3 * 3 + j / 3].insert(cell);
            }
        }

        return true;
    }
};
