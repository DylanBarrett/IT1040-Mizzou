class Users:
   def __init__(self, user_list , rps_file_name ):
       self.__user_list = user_list
       self.__rps_file_name = rps_file_name.dat
      
   def load_users(self):
      try:
       f = open(self.__rps_user_file, 'wb')
       pickle.dump(self.__user_list, f)
       f.close()
      except:
         print("error file doesnt exist")
      data = line.split()
      user = User(data[0],data[1],data[2],data[3])
      self.__user_list.append(user)
  
   def save_users(self):  
       printer = open(self.__rps_file_name, 'w')
       for user in self.__user_list:
           printer.write(user.display_user())
  
   def create_user(self,name):
       found = false
       for user in self.__user_list:
           if(user.get_username() == name):
               found = true
               break
       if(found):
           print("user already exist")
       else:
           user = User(name,0,0,0)
           self.__user_list.append(user)

   def update_user(self):
      try:
         f = open(self.__rps_user_file, 'wb')
         pickle.dump(self.__user_list, f)
         f.close()
      except:
         print("error file doesnt exist")

   def read_file(self):
    f = open(self).read().split()
    lis = []
    for i in f:
            lis.append(i)
    return lis
   def display_highscore(self):
       highest_scorer = self.__user_list[0].get_username()
       highest_score = self.__user_list[0].get_user_wins()/self.__user_list[0].get_round()
       for user in self.__user_list:
           score = user.get_user_wins()/user.get_round()
           if(score > highest_score):
               highest_score = score
               highest_scorer = user.get_username()
       print("Name: ",highest_scorer," Win percentage: ",highest_score)
