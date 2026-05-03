class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)]) # position, speed, step

        while queue:
            pos, speed, step = queue.popleft()

            if pos == target:
                return step

            queue.append((pos + speed, speed * 2, step + 1))

            if pos + speed > target and speed > 0:
                queue.append((pos, -1, step + 1))
            elif pos + speed < target and speed < 0:
                queue.append((pos, 1, step + 1))
