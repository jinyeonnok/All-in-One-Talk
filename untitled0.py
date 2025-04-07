# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:42:50 2025

@author: rogio-new
"""

import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files (x86)\Graphviz\bin"

from graphviz import Digraph

dot = Digraph(name="Command ERD", format='png')

dot.node('User', '''User
------------------------
id (PK)
username
email
password
...''')

dot.node('Command', '''Command
------------------------
id (PK, UUID)
user_id (FK)
command_number
message
image
status
created_at''')

dot.node('Command_recipients', '''Command_recipients
------------------------
id (PK)
command_id (FK)
user_id (FK)''')

dot.edge('Command', 'User', label='user_id → User(id)')
dot.edge('Command_recipients', 'Command', label='command_id → Command(id)')
dot.edge('Command_recipients', 'User', label='user_id → User(id)')

dot.render(directory='./', cleanup=True)
