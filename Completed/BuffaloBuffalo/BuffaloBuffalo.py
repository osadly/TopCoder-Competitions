class BuffaloBuffalo:
    def check(self, s):
        lst=list(set(s.split()))
        if len(lst) != 1:
            return "Not good"
        elif lst[0] != "buffalo":
            return "Not good"
        elif s.count(' ') != len(s.split())-1:
            return "Not good"
