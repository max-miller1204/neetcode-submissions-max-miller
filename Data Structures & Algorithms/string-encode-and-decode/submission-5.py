class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Read the length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # Read the string of that length
            j += 1  # skip '#'
            decoded.append(s[j:j + length])

            # Move pointer
            i = j + length

        return decoded