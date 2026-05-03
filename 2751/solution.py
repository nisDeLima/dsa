class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []
        for i in range(len(positions)):
            health = healths[i]
            position = positions[i]
            direction = directions[i]
            robots.append((position, health, direction, i))

        robots.sort()

        scaped = []
        stack = []

        for position, health, direction, idx in robots:
            if not stack and direction == "L":
                scaped.append((idx, health))
                continue
            elif direction == "L":
                survived = True
                curr_health = health
                while stack and survived:
                    top_position, top_health, top_idx = stack[-1]

                    if curr_health > top_health:
                        # left robot wins, destroy right, lose 1 health, keep going
                        stack.pop()
                        curr_health -= 1
                    elif curr_health == top_health:
                        # both destroyed
                        stack.pop()
                        # CHANGED: fixed typo — you had "survided" instead of "survived"
                        survived = False
                    else:
                        # left robot loses, right robot survives with -1 health
                        stack[-1] = (top_position, top_health - 1, top_idx)
                        survived = False

                if survived and curr_health > 0:
                    scaped.append((idx, curr_health))
            else:
                stack.append((position, health, idx))

        all_survivors = []
        for orig_idx, h in scaped:
            all_survivors.append((orig_idx, h))

        for _, h, orig_idx in stack:
            all_survivors.append((orig_idx, h))

        all_survivors.sort()
        return [h for _, h in all_survivors]
