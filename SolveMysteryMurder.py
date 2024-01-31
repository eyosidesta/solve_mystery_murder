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

        "suspect(x) :- man(x)",
        "suspect(x) :- woman(x)",

        "access_to_revolver(x, y): owns_revolver(x), "

        "went_outside(x) :- smokers(x)",
        "went_outside(x) :- played_golf(x)",
        "went_outside(x) :- gardening(x)", 

        "share_room(x, y):- room_number(z), owns_revolver(x, z), stay_in(y, z), neq(x, y)"
        "guilty(x): suspect(x), \+victim(x), "


    ])

print(set_nb.query(pl.Expr("suspect(colonel_mustard)")))



