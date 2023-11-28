class Solution:
    def largestVariance(self, s: str) -> int : 
        char_frequency = collections.defaultdict(int)
        char_indices = collections.defaultdict(list)
        for index, char in enumerate(s) : 
            char_frequency[char] += 1 
            char_indices[char].append(index)
        char_keys = list(char_frequency.keys())
        char_keys_major = sorted(char_keys, key = lambda char_key : char_frequency[char_key], reverse=True)
        char_keys_minor = sorted(char_keys, key = lambda char_key : char_frequency[char_key])
        global_max = 0 
        for major_char in char_keys_major : 
            if char_frequency[major_char] - 1 <= global_max : 
                break
            for minor_char in char_keys_minor :
                if major_char == minor_char : 
                    continue 
                else : 
                    major_count = 0 
                    minor_count = 0 
                    remaining_minor = char_frequency[minor_char]
                    remaining_major = char_frequency[major_char]
                    total_indices = sorted([index_1 for index_1 in char_indices[major_char]] + [index_2 for index_2 in char_indices[minor_char]])
                    for index in total_indices : 
                        if s[index] == major_char : 
                            major_count += 1 
                            remaining_major -= 1 
                        else : 

                            minor_count += 1 
                            remaining_minor -= 1 
                        
                        global_max = max(global_max, major_count-minor_count) if minor_count > 0 else global_max

                        if (major_count < minor_count) : 
                            if remaining_major - 1 <= global_max : 
                                break 
                            elif remaining_minor > 0 : 
                                major_count = 0 
                                minor_count = 0 
                            else : 
                                global_max = max(global_max, (major_count + remaining_major) - minor_count)
                                break
                        else : 
                            continue 
        return global_max


        