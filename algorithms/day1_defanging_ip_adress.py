class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.address = address
        return self.address.replace(".", "[.]")
