import datetime

class Anime:
    def __init__(self, name: str, episodes: int, duration: int, air_date: str, end_date: str=None):
        self.name = name
        self.episodes = episodes
        self.duration = datetime.time(0, duration)
        self.air_date = datetime.datetime.strptime(air_date, '%b %d, %Y')

        if end_date is not None:
            self.end_date = datetime.datetime.strptime(end_date, '%b %d, %Y')

    def __str__(self):
        return 'The class object encapsulates various details about a specific anime series'

    def total_duration(self):
        total_m = self.duration.minute * self.episodes
        total_d = datetime.timedelta(minutes=total_m)
        print(f'{total_d}')

    def airing_days(self):
        time = self.end_date - self.air_date
        print(f'{time.days} days')

    def expected_end_date(self):
        days = datetime.timedelta(self.episodes * 7)
        end_date = self.air_date + days
        print(f'expected end date of {self.name}: {end_date:%b %d, %Y}.')

if __name__ == '__main__':

    id_1 = Anime('Solo Leveling', 12, 23,  'Jan 7, 2024',  'Mar 31, 2024')
    id_2 = Anime('Classroom of the Elite III', 13, 23, 'Jan 3, 2024', 'Mar 27, 2024')
    id_3 = Anime('Delicious in Dungeon', 24, 25, 'Jan 4, 2024')

    print(id_2.__dict__)
    print(id_3.__dict__)
    id_3.expected_end_date()
