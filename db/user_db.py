from typing import Dict
from pydantic import BaseModel
from pydantic.errors import EmailError
from pprint import pprint

class User(BaseModel):
    usr_id: int
    name: str
    email: str

database_users = Dict[str, User]

database_users = {
    1026755874:User(**{
		"usr_id" : 1026755874,
		"name" : "Holly",
		"email" : "holly@company.com"
	}),
    1056344563:User(**{
		"usr_id" : 1056344563,
		"name" : "Ryan",
		"email" : "ryan@company.com"
	}),
    1074555278:User(**{
		"usr_id" : 1074555278,
		"name" : "Kelly",
		"email" : "kelly@company.com"
	}),
    1559377264:User(**{
		"usr_id" : 1559377264,
		"name" : "Michel",
		"email" : "mich@company.com"
	}),
    1759333562:User(**{
		"usr_id" : 1759333562,
		"name" : "Jim",
		"email" : "jim@company.com"
	}),
    1849300289:User(**{
		"usr_id" : 1849300289,
		"name" : "Andy",
		"email" : "andy@company.com"
	}),
    1856388256:User(**{
		"usr_id" : 1856388256,
		"name" : "Dwight",
		"email" : "dwig@company.com"
	}),
    1857633545:User(**{
		"usr_id" : 1857633545,
		"name" : "Angela",
		"email" : "angela@company.com"
	}),
    1860462977:User(**{
		"usr_id" : 1860462977,
		"name" : "Pam",
		"email" : "pam@company.com"
	}),
    1946733975:User(**{
		"usr_id" : 1946733975,
		"name" : "Kevin",
		"email" : "kevin@company.com"
	}),
    1954388765:User(**{
		"usr_id" : 1954388765,
		"name" : "Stanley",
		"email" : "stanley@company.com"
	}),
}

def get_usr_id(user_id: str):
    if user_id in database_users.keys():
        return database_users[user_id]
    else:
        return None