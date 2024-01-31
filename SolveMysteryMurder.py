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

        "stayed_in_doors(professor_plum)",
        "stayed_in_doors(miss_scarlett)",
        "stayed_in_doors(madam_rose)",
        "stayed_in_doors(mrs_white)",

        "gardening(mrs_white)",
        "gardening(reverend_green)",

        ])
