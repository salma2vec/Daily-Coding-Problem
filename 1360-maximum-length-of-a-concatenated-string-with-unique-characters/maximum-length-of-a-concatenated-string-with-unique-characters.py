class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr_masks = []
        for s in arr:
            mask = 0
            uniq = True
            for c in s:
                shift = ord(c) - ord('a')
                if (1 << shift) & mask == 0:
                    mask |= (1 << shift)
                else:
                    uniq = False
                    break
            if uniq:
                arr_masks.append(mask)
        
        res = [0]
        mask = 0
        def dfs(idx, mask, item):
            if idx == len(arr_masks):
                res[0] = max(mask.bit_count(), res[0])
                return
            
            if arr_masks[idx] & mask == 0:
                dfs(idx + 1, arr_masks[idx] | mask, item + [idx])   
            dfs(idx + 1, mask, item)               
                
        dfs(0, 0, [])
        
        return res[0]        