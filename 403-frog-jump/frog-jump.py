class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jump_positions = {}
        
        for stone in stones:
            jump_positions[stone] = set()

        jump_positions[0].add(0)

        for stone in stones:
            for jump in jump_positions[stone]:
                for next_jump in range(jump - 1, jump + 2):
                    if next_jump > 0 and stone + next_jump in jump_positions:
                        jump_positions[stone + next_jump].add(next_jump)
        
        return len(jump_positions[stones[-1]]) > 0   