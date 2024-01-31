import pytholog as pl

set_nb = pl.knowledge_base("murderer")
set_nb([
        "victim(dr_black)"

        "man(dr_black)",
        "man(reverend_green)",
        "man(colonel_mustard)",
        "man(professor_plum)",
        "woman(miss_scarlett)",
        "woman(mrs_peacock)",
        "woman(madam_rose)",
        "woman(mrs_white)",

        "smokers(dr_black)"
        "smokers(miss_scarlett)"
        "smokers(colonel_mustard)"
        "smokers(mrs_peacock)"
        "smokers(mrs_white)"

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

        "playing_cards(colonel_mustard)",
        "playing_cards(colonel_mustard)",
        "playing_cards(colonel_mustard)",

        "gardening(mrs_white)",
        "gardening(reverend_green)",

        "played_golf(colonel_mustard)",
        "played_golf(professor_plum)",

        "owns_revolver(reverend_green)",
        "owns_revolver(colonel_mustard)",
        "owns_revolver(madam_rose)",

        "has_alibi(X):- suspect(X), playing_cards(X)"

        "suspect(X) :- man(X)",
        "suspect(X) :- woman(X)",

        # "access_to_revolver(x, y): owns_revolver(x), "

        "went_outside(X) :- smokers(X)",
        "went_outside(X) :- played_golf(X)",
        "went_outside(X) :- gardening(X)", 

        "share_room(X, Y):- room_number(Z), stay_in(X, Z), stay_in(Y, Z), neq(X, Y)",
        "has_access_to_revolver(X) :- owns_revolver(X)",
        "has_access_to_revolver(X) :- share_room(X, Y), owns_revolver(Y)",
        "guilty(X) :- suspect(X), has_access_to_revolver(X), went_outside(X)",


    ])

guilty_query = "guilty(X)"
result = set_nb.query(guilty_query)
print("Guilty individuals:")
for solution in result:
    print(solution['X'])

# print(set_nb.query(pl.Expr("guilty(mrs_white, reverend_green)")))



