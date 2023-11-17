class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def hamming_distance(w1: str, w2: str) -> int:
            return sum(1 for k in range(6) if w1[k] != w2[k])

        current_guess = wordlist[0]
        curr_distance = 6 - Master.guess(master, current_guess)
        while curr_distance != 0:
            wordlist = [w for w in wordlist if hamming_distance(current_guess, w) == curr_distance]
            current_guess = wordlist.pop()
            curr_distance = 6 - Master.guess(master, current_guess)
