import pytholog as pl

set_nb = pl.knowledge_base("murderer")
set_nb(["man(dr_black)",
        "man(reverend_green)",
        "man(miss_scarlett)",
        ])
print(set_nb.query(pl.Expr("man(dr_black)")))
