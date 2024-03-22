class Character:
    round = 3 

    def __init__(self, maxHealth, recovery, moveSpeed):
        self.maxHealth = maxHealth
        self.recovery = recovery
        self.moveSpeed = moveSpeed

    def set_max_health(self, mxhealth):
        self.maxHealth = mxhealth

    def set_round(self, rnd):
        self.round = rnd

    def set_round_two(self, rnd):
        Character.round = rnd

    @classmethod
    def set_round_cls(cls, rnd):
        cls.round = rnd

    @classmethod
    def create(cls, string):
        maxHealth, recovery, moveSpeed = string.split()
        return cls(maxHealth, recovery, moveSpeed)

def main():
    characterOne = Character(20, 30, 50)
    characterTwo = Character.create('32 42 45')
    print(characterOne.__dict__)
    print(characterTwo.__dict__)

if __name__ == '__main__':
    main()
