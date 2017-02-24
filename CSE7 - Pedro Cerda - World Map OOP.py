class Room():
    def __init__(self, the_name, N, W, E, S, U, D, the_description):
        self.name = the_name
        self.description = the_description
        self.north = N
        self.west = W
        self.east = E
        self.south = S
        self.up = U
        self.down = D
    def move(self, direction):
            '''This function allows movement to a different node.
            '''
            global node
            node = globals()[getattr(self.direction)]
            
                    
mentr = Room('Mall Entrance', 'hw','food', 'elev', None, None, None, ' You are in\
 the front mall entrance. Behind you are the\
 mall front doors, but they are nailed shut.')
 
hw = Room('Hallway', 'ftl', 'jai;', 'hw2', 'mentr', None, None, ' It\'s a long hallway.')

food = Room('Foodcourt', None, 'wfr', 'mentr', 'bath', None, None, ' There are\
tons of empty tables. The light is flickering.')

node = mentr

#try:
     #   node = world_map[node['PATHS'][command]]
 #   except:
  #      print 'You can\'t'