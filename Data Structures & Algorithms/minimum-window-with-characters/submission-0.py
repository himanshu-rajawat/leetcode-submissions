class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_substring(str_count,substr_count):
            is_substring = True
            for key in substr_count.keys():
                is_substring = is_substring and substr_count[key] <= str_count.get(key, 0)
            return is_substring

        def get_minimum_window(window, s_window_counter, t_counter):
            while True:
                char = window[0]
                s_window_counter[char]-=1

                if is_substring(s_window_counter, t_counter):
                    window = window[1:]
                else:
                    s_window_counter[char]+=1
                    break;
            return window

        # create frequency counter for t
        t_counter = {}
        for char in t:
            t_counter[char] = t_counter.get(char,0)+1

        # sliding window s

        s_window_counter = {}
        window = ""
        min_window = ""

        # build window from left to right
        for i in range(len(s)):
            char = s[i]
            window+=char
            s_window_counter[char]=s_window_counter.get(char,0)+1

            if is_substring(s_window_counter, t_counter):
                window = get_minimum_window(window, s_window_counter, t_counter)
                min_window = window if (min_window=="" or len(window)<len(min_window)) else min_window
        

        return min_window