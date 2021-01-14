class Baseball_Team:
    def __init__(self, name, win, lose, draw):
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw

    def calc_win_rate(self):
        return self.win/(self.win + self.lose)
        
    def show_team_result(self):
        print(f'{self.name:<8} {self.win:>3} {self.lose:>4} {self.draw:>4} {self.calc_win_rate():.3f}')

giants = Baseball_Team("Giants", 77, 64, 2)
bayStars = Baseball_Team("BayStars", 71, 69, 3)
tigers = Baseball_Team("Tigers", 69, 68, 6)
carp = Baseball_Team("Carp", 70, 70, 3)
dragons = Baseball_Team("Dragons", 68, 73, 2)
swallows = Baseball_Team("Swallows", 59, 82, 2)

print("team     win lose draw rate")
giants.show_team_result()
bayStars.show_team_result()
tigers.show_team_result()
carp.show_team_result()
dragons.show_team_result()
swallows.show_team_result()