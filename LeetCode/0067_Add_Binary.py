class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sumnum = int(a,2) + int(b,2)
        print(bin(sumnum)[2:])