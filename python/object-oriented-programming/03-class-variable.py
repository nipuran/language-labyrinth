class SteamGame:
    # class variables
    platform: str = 'Steam'

    # steam takes 30 % cut of the revenue from each game sold.
    revenue_share: float = 0.3

    added_game: int = 0

    def __init__(self, name: str, revenue: float):
        self.name = name
        self.revenue = revenue
        SteamGame.added_game += 1

    def net_profit(self):
        net_p = self.revenue - (self.revenue * SteamGame.revenue_share)
        print(f'Net profit of {self.name}: ${net_p}')

def main():
    id_1 = SteamGame('Stardew Valley', 131.8e6)
    id_2 = SteamGame('Vampire Survivors', 21e6)

    id_1.net_profit()
    id_2.net_profit()

    print(f'Total Games: {SteamGame.added_game}')

if __name__ == '__main__':
    main()
