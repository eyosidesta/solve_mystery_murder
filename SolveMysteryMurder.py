import pytholog as pl

class MurderMysterySolver:
    def __init__(self):
        self.set_nb = pl.knowledge_base("murderer")
        self.load_knowledge_base()

    def load_knowledge_base(self):
        self.set_nb([
            "victim(dr_black)",

            "man(dr_black)",
            "man(reverend_green)",
            "man(colonel_mustard)",
            "man(professor_plum)",
            "woman(miss_scarlett)",
            "woman(mrs_peacock)",
            "woman(madam_rose)",
            "woman(mrs_white)",

            "smokers(dr_black)",
            "smokers(miss_scarlett)",
            "smokers(colonel_mustard)",
            "smokers(mrs_peacock)",
            "smokers(mrs_white)",

            "stay_in(miss_scarlett, room_21)",
            "stay_in(madam_rose, room_21)",
            "stay_in(dr_black, room_22)",
            "stay_in(professor_plum, room_22)",
            "stay_in(mrs_peacock, room_23)",
            "stay_in(mrs_white, room_23)",
            "stay_in(reverend_green, room_24)",
            "stay_in(colonel_mustard, room_24)",

            "room_number(room_21)",
            "room_number(room_22)",
            "room_number(room_23)",
            "room_number(room_24)",

            # gusts who stayed in doors (not playing cards)
            "indoors(professor_plum)",
            "indoors(miss_scarlett)",
            "indoors(madam_rose)",
            "indoors(mrs_white)",

            "gardening(mrs_white)",
            "gardening(reverend_green)",

            "played_golf(colonel_mustard)",
            "played_golf(professor_plum)",

            "owns_revolver(reverend_green)",
            "owns_revolver(colonel_mustard)",
            "owns_revolver(madam_rose)",

            "suspect(X) :- man(X)",
            "suspect(X) :- woman(X)",

            "went_outside(X) :- smokers(X)",
            "went_outside(X) :- played_golf(X)",
            "went_outside(X) :- gardening(X)", 

            "share_room(X, Y):- room_number(Z), stay_in(X, Z), stay_in(Y, Z), neq(X, Y)",

            "has_access_to_revolver(X) :- owns_revolver(Y), share_room(X, Y)",

            "guilty(X) :- suspect(X), has_access_to_revolver(X), went_outside(X), indoors(X)",
        ])

    def find_murderer(self, suspects):
        the_murderer = []

        for suspect in suspects:
            result = self.set_nb.query(pl.Expr("guilty(" + suspect + ")"))
            if result is not None and result == ['Yes']:
                the_murderer.append(suspect)

        return the_murderer

    def print_murderer(self, murderers):
        for murderer in murderers:
            print("The murderer is:", murderer)

# Creating an instance of the MurderMysterySolver class
solver = MurderMysterySolver()

# List of suspects
suspects = ["reverend_green", "colonel_mustard", "professor_plum", "miss_scarlett", "mrs_peacock", "madam_rose", "mrs_white"]

# Finding the murderer
murderers = solver.find_murderer(suspects)

# Printing the result
solver.print_murderer(murderers)
