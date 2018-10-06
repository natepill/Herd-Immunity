import random

# TODO: Import the virus clase

class Person(object):
    '''
    Person objects will populate the simulation.



    _____Methods_____:

    __init__(self, _id, is_vaccinated, infected=False):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding parameter
            passed during instantiation.
        - If person is chosen to be infected for first round of simulation, then
            the object should creaon should be set to None.

    did_survive_infection(self):
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's infection
            attribute.
            - If random number is smaller, person has died from disease.
                is_alive is changed to false.
            - If random number is larger, person has survived disease.  Person's
            is_vaccinated attribute is changed to True, and set self.infected to None.
    '''

    def __init__(self, _id, is_vaccinated, infected=None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the corret values for the following attributes.
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected

            # _____Attributes______:
            #
            # _id: Int.  A unique ID assigned to each person.
            #
            # is_vaccinated: Bool.  Determines whether the person object is vaccinated against
            #     the disease in the simulation.
            #
            # is_alive: Bool. All person objects begin alive (value set to true).  Changed
            #     to false if person object dies from an infection.
            #
            # infection:  None/Virus object.  Set to None for people that are not infected.
            #     If a person is infected, will instead be set to the virus object the person
            #     is infected with.
            #

    def did_survive_infection():
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        # If person lives, set is_vaccinated = True, infected = None, return True.

        if self.infected != None:
            random_rate = random.random()

            if random_rate < self.infected:
                self.is_alive = False
                self.infected = None
                return False
            elif random_rate > self.infected:
                self.is_vaccinated = True
                self.infected = None
                return True

     # did_survive_infection(self):
     #     - Only called if infection attribute is not None.
     #     - Takes no inputs.
     #     - Generates a random number between 0 and 1.
     #     - Compares random number to mortality_rate attribute stored in person's infection
     #         attribute.
     #         - If random number is smaller, person as died from disease.
     #             is_alive is changed to false.
     #         - If random number is larger, person has survived disease.  Person's
     #         is_vaccinated attribute is changed to True, and set self.infected to None.