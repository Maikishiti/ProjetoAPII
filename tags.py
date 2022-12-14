import database.database as db
    

def get_all_groups():
    return db.get_all_tables("database/tag_groups.db")


def create_tag_group(tag_group_name):
    db.create_table("database/tag_groups.db", tag_group_name, ["tag TEXT NOT NULL PRIMARY KEY"])


def remove_tag_group(tag_group_name):
    db.remove_table("database/tag_groups.db", tag_group_name)

def remove_tag(tag_group_name, tag):
    db.remove_element_where("database/tag_groups.db", tag_group_name, "tag", tag)

def get_tag_group(tag_group_name):
    return db.get_table("database/tag_groups.db", tag_group_name)


def edit_tag_group(tag_group_name, what, to, where):
    db.edit_element("database/tag_groups.db", tag_group_name, what, to, where)


def add_tags_to_group(tag_group_name, tag):
    db.add_to_db("database/tag_groups.db", tag_group_name, {"tag": tag})
    
    

if __name__ == "__main__":
    create_tag_group("tamanho")
    create_tag_group("cor")

    print(get_all_groups())
    
    print(repr(get_tag_group("tamanho")))
    print(repr(get_tag_group("cor")))
