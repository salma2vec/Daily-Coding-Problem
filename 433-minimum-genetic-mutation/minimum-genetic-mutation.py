class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Find the minimum number of mutations needed to mutate from startGene to endGene using valid genes in the bank.

        Args:
            startGene (str): The starting gene string.
            endGene (str): The target gene string.
            bank (List[str]): List of valid gene strings in the bank.

        Returns:
            int: The minimum number of mutations. Return -1 if it's impossible.
        """
        if endGene not in bank:
            return -1

        def is_valid_mutation(gene1, gene2):
            mutations = 0
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    mutations += 1
                if mutations > 1:
                    return False
            return mutations == 1

        queue = deque([(startGene, 0)])
        visited = set()

        while queue:
            current_gene, mutations = queue.popleft()
            if current_gene == endGene:
                return mutations

            for bank_gene in bank:
                if bank_gene not in visited and is_valid_mutation(current_gene, bank_gene):
                    visited.add(bank_gene)
                    queue.append((bank_gene, mutations + 1))

        return -1        