class Solution {
public:
    int maximumsSplicedArray(vector<int>& nums1, vector<int>& nums2) {
    int kd[2] = {}, res[2] = {}, sum[2] = {};
    for (int i = 0; i < nums1.size(); ++i) {
        kd[0] = max(nums2[i] - nums1[i], kd[0] + nums2[i] - nums1[i]);
        res[0] = max(res[0], kd[0]);
        kd[1] = max(nums1[i] - nums2[i], kd[1] + nums1[i] - nums2[i]);
        res[1] = max(res[1], kd[1]);
        sum[0] += nums1[i];
        sum[1] += nums2[i];        
    }    
    return max(sum[0] + res[0], sum[1] + res[1]);       
    }
};