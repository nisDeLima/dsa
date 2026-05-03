MOD = 10 ** 9 + 7
class Fancy_rmvd:
    def __init__(self):
        self.epoch = 0
        self.sequence = [] # (val, epoch)
        self.operations = [] # (type, val, epoch)

    def append(self, val: int) -> None:
        self.sequence.append((val, self.epoch))

    def addAll(self, inc: int) -> None:
        self.epoch += 1
        self.operations.append(("inc", inc, self.epoch))

    def multAll(self, m: int) -> None:
        self.epoch += 1
        self.operations.append(("mult", m, self.epoch))

    def getIndex(self, idx: int) -> int:
        if len(self.sequence) <= idx:
            return -1
        val, epoch = self.sequence[idx]
        if len(self.operations) == 0 or epoch == self.operations[-1][2]:
            return val

        for kind, op_val, op_epoch in self.operations[epoch::]:
            if kind == "inc":
                new_val = (self.sequence[idx][0] + op_val) % MOD
                self.sequence[idx] = (new_val, op_epoch)
            elif kind == "mult":
                new_val = (self.sequence[idx][0] * op_val) % MOD
                self.sequence[idx] = (new_val, op_epoch)
        
        return self.sequence[idx][0]

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
MOD = 10 ** 9 + 7

class Fancy:
    def __init__(self):
        self.sequence = []
        self.ops = [(1, 0)]  # (cumulative_mult, cumulative_add)

    def append(self, val: int) -> None:
        # store val AND which op index it was born at
        self.sequence.append((val, len(self.ops) - 1))

    def addAll(self, inc: int) -> None:
        a, b = self.ops[-1]
        self.ops.append((a, (b + inc) % MOD))

    def multAll(self, m: int) -> None:
        a, b = self.ops[-1]
        self.ops.append((a * m % MOD, b * m % MOD))  # mult hits BOTH

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        val, born = self.sequence[idx]
        old_a, old_b = self.ops[born]
        cur_a, cur_b = self.ops[-1]
        # delta transform: what happened from born to now
        inv_old_a = pow(old_a, MOD - 2, MOD)
        a_delta = cur_a * inv_old_a % MOD
        b_delta = (cur_b - cur_a * inv_old_a % MOD * old_b) % MOD
        return (a_delta * val + b_delta) % MOD
