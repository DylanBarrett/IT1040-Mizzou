class User:
   usersCount = 0

def __init__(self, name, wins,ties,losses):
       self.name = name
       self.ties = ties
       self.wins = wins
       self.losses - losses
       User.usersCount += 1

       def get_username(self):
           return self.name
       def get_user_wins(self):
           return self.wins
       def set_user_wins(self,wins):
           self.wins = wins
       def get_user_ties(self):
           return self.ties
       def set_user_ties(self,ties):
           self.ties = ties
       def get_user_losses(self):
           return self.losses
       def set_user_losses(self,losses):
           self.losses = losses
       def get_round(self):
           return self.ties+self.losses+self.wins
       def get_age(date):
           d1 = datetime.strptime(d1, "%Y-%m-%d")
           d2 = datetime.strptime(datetime.datetime.time(datetime.datetime.now()), "%Y-%m-%d")
           return abs((d2 - d1).days)  
       def display_user(self):
           print("Name : ", self.name, ", Wins: ", self.wins, ", Losses: ", self.losses, ", Ties: ", self.ties)
