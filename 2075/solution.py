class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        ROWS, COLS = rows, len(encodedText) // rows
        matrix = [[" "] * COLS for _ in range(ROWS)]

        encoded_idx = 0
        for row in range(ROWS):
            for col in range(COLS):
                matrix[row][col] = encodedText[encoded_idx]
                encoded_idx += 1
        
        decoded = []

        for col in range(COLS):
            for row in range(ROWS):
                if row + col >= COLS:
                    break
                decoded.append(matrix[row][col + row])
        
        return "".join(decoded).rstrip()
