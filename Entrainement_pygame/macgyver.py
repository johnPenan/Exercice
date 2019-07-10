class MacGyver:
    """This class define the position and the characteristic of the hero MacGyver"""


    def __init__(self, labyrinth):
        """This method is the constructor of the class MacGyver"""
        self.labyrinth = labyrinth
        self.position = self.labyrinth.departure
        self.labyrinth.macgyver = self
        self.items = []
        


    def move(self, direction):
        """This method determine the different movements of MacGyver."""
        new_position = getattr(self.position, direction)()
        if self.labyrinth.is_streets(new_position) and new_position not in self.labyrinth.object_positions:
            if new_position != self.labyrinth.arrival:
                self.position = new_position
            elif new_position == self.labyrinth.arrival and len(self.items) ==3:
                print("Bien joue. Vous avez gagne !")
                return False
            elif new_position == self.labyrinth.arrival and len(self.items) !=3:
                print("Vous avez perdu.\n La vie d'un hero est cruelle !")
                return False

        elif new_position in self.labyrinth.object_positions:
            self.items.append(new_position)
            self.position = new_position
        
        return True
       





    

    



            




        

       