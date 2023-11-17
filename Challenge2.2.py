


#Define the base class player
class player:

  def play(self):
    print("The player is playing cricket.")


#Define the derived class Batsman
class Batsman(player):

  def play(self):
    print("The batsman is batting.")


#Define the dervied class Bowler
class Bowler(player):

  def play(self):
    print("The bowler is bowling.")


#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()