#CHECK TABLE ORDER FOR PROPERLY 
#REFERENCE FORMAT,ATTRIBUTES ARGUMENTS AND MORE


db.define_table("entidad_1",
    Field("nombre", "varchar(16)"), 
    format="%(id)s"
)

db.define_table("entity2",
    Field("entidad_1_id", "reference entidad_1"), 
    Field("entity3_id", "reference entity3"), 
    format="%(id)s"
)

db.define_table("entity3",
    format="%(id)s"
)

db.define_table("entity4",
    Field("entity2_id", "reference entity2"), 
    format="%(id)s"
)