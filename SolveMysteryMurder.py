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

        "room_number(miss_scarlett, room_21)",
        "room_number(madam_rose, room_21)",
        "room_number(dr_black, room_22)",
        "room_number(professor_plum, room_22)",
        "room_number(mrs_peacock, room_23)",
        "room_number(mrs_white, room_23)",
        "room_number(reverend_green, room_24)",
        "room_number(colonel_mustard, room_24)",

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

        "suspect(x):- man(x), \+victim(x)",
        "suspect(x):- woman(x), \+victim(x)",


    ])





