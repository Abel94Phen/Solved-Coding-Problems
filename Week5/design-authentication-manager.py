class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.timeToLive = timeToLive
    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            self.tokens[tokenId] = currentTime + self.timeToLive 

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and currentTime < self.tokens[tokenId]:
            self.tokens[tokenId] = currentTime + self.timeToLive            

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.tokens.values():
            if token > currentTime:
                count += 1
        
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)