class GroupError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self) -> str:
        return self.val
