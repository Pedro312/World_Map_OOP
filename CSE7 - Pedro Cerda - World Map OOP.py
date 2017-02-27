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
 
hw = Room('Hallway', 'ftl', 'jail', 'hw2', 'mentr', None, None, ' It\'s a long hallway.')

food = Room('Foodcourt', None, 'wfr', 'mentr', 'bath', None, None, ' There are\
tons of empty tables. The light is flickering.')

elev = Room('Elevator', None, 'mentr', None, None, None, None, ' It\'s an elevator. The\
power is down.')

wfr = Room('Wet Floor', None, None, 'food', None, None, None, ' The floor is significantly\
moist.')

bath = Room('Bathroom', 'food', None, None, None, None, None, ' It\'s a bathroom. The stalls\
are locked and the mirrors are shattered.')

jail = Room('Mall Jail', None, None, 'hw', None, None, None, ' This is the mall jail. It is\
extremely cold, and a badge is gleaming on the desk.')

ftl = Room('Footlocker', None, None, None, 'hw', None, None, ' It\'s a store. There are\
shoes thrown all over the ground and fairly large footprints,')

hw2 = Room('Hallway', None, 'hw', None, None, None, None, ' It\'s a long hallway.')

node = mentr

#try:
     #   node = world_map[node['PATHS'][command]]
 #   except:
  #      print 'You can\'t'