class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int,int> m;

        for(auto v:nums){
            m[v]++;
        }

        for(auto val:m){
            if(val.second == 1){
                return val.first;
            }
        }

        return -1;
    }
};