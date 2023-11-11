class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_moves = sum(len(block) - 2 for block in colors.split('B') if len(block) >= 3)
        bob_moves = sum(len(block) - 2 for block in colors.split('A') if len(block) >= 3)
        return alice_moves > bob_moves    