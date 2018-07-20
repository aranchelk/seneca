'''
    Provide an even easier interface for people to store and retrieve data with Seneca smart contracts. Inspired by ORMs

    balances = orm.new('name', *args)
    balances = orm.get('name')

    wallet = balances.new()
    wallet.amount = 100
    wallet.owner = 'stu'
    wallet.commit()

    The ORM module is really just a wrapper around the Tabular interface to help build queries.

    Options:
        * create an interface like Tabular and KV
        * create a new interface that just makes queries and then executes them against tabular

'''

import seneca.seneca_internal.storage.easy_db as db

ex = None
name_space = None

str_len = db.str_len

def add_name_space(t_name):
    assert name_space is not None, "Tabular module namespace has not been set!"
    return name_space + '$' + t_name

def new(table_name: str, columns):
    # assert that there is a primary key / unique in the first column
    assert len(columns) > 0
    # assert columns[0]

    # build the query



    t = db.Table(add_name_space(name), db.AutoIncrementColumn('id'),
                 [db.Column(*x) for x in columns]
                 )
    t.create_table(if_not_exists=True).run(ex)

    pass

def get(table_name: str):
    pass