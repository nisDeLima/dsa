class Solution:
    def defangIPaddr(self, address: str) -> str:
        add_list = list(address)

        for i, c in enumerate(add_list):
            if c == ".":
                add_list[i] = "[.]"

        return "".join(add_list)
