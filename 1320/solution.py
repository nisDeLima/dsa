class Solution:
    def minimumDistance(self, word: str) -> int:
        #setup letter pos
        ROWS, COLS = 5, 6
        letter_pos = {}
        letter = 0
        for row in range(ROWS):
            for col in range(COLS):
                letter_pos[chr(ord("A") + letter)] = (row, col)
                letter += 1
                if letter == 26:
                    break

        def calc_dist(prev_pos, new_pos):
            x1, y1 = prev_pos
            x2, y2 = new_pos

            return abs(x1 - x2) + abs(y1 - y2)

        @cache
        def get_min(left_pos, right_pos, i):
            if i == len(word):
                return 0

            new_pos = letter_pos[word[i]]

            use_left = 0
            if left_pos != None:
                use_left = calc_dist(left_pos, new_pos) + get_min(new_pos, right_pos, i + 1)
            else:
                use_left = get_min(new_pos, right_pos, i + 1)

            use_right = 0
            if right_pos != None:
                use_right = calc_dist(right_pos, new_pos) + get_min(left_pos, new_pos, i + 1)
            else:
                use_right = get_min(left_pos, new_pos, i + 1)

            return min(use_left, use_right)
            
        return get_min(None, None, 0)
