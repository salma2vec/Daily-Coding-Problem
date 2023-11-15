class TextEditor:
    def __init__(self):
        self.left = deque()
        self.right = deque()
        
    def addText(self, text: str) -> None:
        self.left.extend(list(text))

    def deleteText(self, k: int) -> int:
        tot = 0
        while k and self.left:
            self.left.pop()
            k -= 1
            tot +=1
        return tot
        
    def cursorLeft(self, k: int) -> str:
        while k and self.left:
            self.right.appendleft(self.left.pop())
            k -= 1
        return self.getvals()

    def cursorRight(self, k: int) -> str:
        while k and self.right:
            self.left.append(self.right.popleft())
            k -= 1
        return self.getvals()
        
    def getvals(self):
        N = len(self.left) 
        return "".join(self.left[i] for i in range(max(N-10, 0), N))