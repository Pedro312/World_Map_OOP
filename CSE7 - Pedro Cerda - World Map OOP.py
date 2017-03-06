
import sys

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
            node = globals()[getattr(self,direction)]         
#Room1                    
mentr = Room('Mall Entrance', 'hw','food', 'elev', None, None, None, ' You\
 are in the front mall entrance. Behind you are the\
 mall front doors, but they are nailed shut.')
 
 #Room2
hw = Room('Hallway', 'ftl', 'jail', 'hw2', 'mentr', None, None, ' It\'s a long \
hallway.')

#Room3
food = Room('Foodcourt', None, 'wfr', 'mentr', 'bath', None, None, ' There are\
tons of empty tables. The light is flickering.')

#Room4
elev = Room('Elevator', None, 'mentr', None, None, None, None, ' It\'s\
an elevator. The power is down.')

#Room5
wfr = Room('Wet Floor', None, None, 'food', None, None, None, ' The floor is \
significantly moist.')

#Room6
bath = Room('Bathroom', 'food', None, None, None, None, None, ' It\'s a \
bathroom. The stalls are locked and the mirrors are shattered.')

#Room7
jail = Room('Mall Jail', None, None, 'hw', None, None, None, ' This is \
the mall jail. It is extremely cold, and a badge is gleaming on the desk.')

#Room8
ftl = Room('Footlocker', None, None, None, 'hw', None, None, ' It\'s a \
store. There are shoes thrown all over the ground and fairly large footprints,')

#Room9
hw2 = Room('Hallway', 'pp', 'hw', 'pa', 'hg', None, None, ' It\'s a \
long hallway.')

#Room10
pp = Room('Pretzel Palace', 'kc', None, None, 'hw2', None, None,'There is a cold\
 pretzel on the counter, and the cash register is empty.')
 
 #Room11
kc = Room('Kitchen', 'frz', None, None, 'pp', None, None, "It's a kitchen. There\
 is a freezer towards the back and pans on the ground.")

#Room12
hg = Room('Hunting Goods', 'hw2', None, None, 'ws', None, None,\
"It's a hunting shop. There are firearms hung on the walls and on the counters.")

#Room13
ws = Room('Weapon Storage', 'hg', None, None, None, None, None, "There are\
 racks of weapons on the walls and alligned on shelves, and stacks of\
 ammunition in the corner of the room.")
 
#Room14
pa = Room('Play Area', 'ts', 'hw2', 'hw3', 'jwr', None, None, "There are\
 multiple obstacle courses for children, but a few are broken in half\
 and most have spider webs.")
 
#Room15
frz = Room('Freezer', None, None, None, 'kc', None, None, "It is extremely\
 cold (obviously, it's a freezer) and to your right there are frozen\
 water bottles.")
 
#Room16
ts = Room('Toy Store', None, None, None, 'pa', None, None, "This room seems to\
 be oddly clean, compared to the rest. Although some shelves are still snapped.")
 
#Room17
jwr = Room('Jewelry Store', 'pa', None, None, None, None, None, "There are\
 diamond rings in the glass cases, and a sparkling diamond necklace\
 sitting alone on a counter top.")
 
#Room18
hw3 = Room('Hallway', 'fs', 'pa', 'hbp', 'co', None, None, "It's \
the end of a hall the hall continues ahead.")
 
#Room19
hbp = Room('Hli\'s Beauty Products', None, 'hw3', None, None, None, None, "A\
 very neat beauty store, with makeup products on  the shelves,\
 and clothing hanging on racks organized by color. A nametag reading 'Hli'\
 is lying on the counter.")
 
#Room20
co = Room('Clothing Outlet', 'hw3', None, None, None, None, None, "There is \
tons of clothes thrown on the ground, and all the metal racks are flipped over.")

node = mentr

#static variables
is_alive = True
directions = ['north','south','east','west','up','down']
short_directions = ['n','s','e','w','u','d']

while is_alive:
    #Print room name and description
    print node.name
    print node.description

   #Ask for input
    command = raw_input('> ')
    if command in ['quit','exit']:
        sys.exit(0)

   #Allows us to change nodes
    if command in short_directions:
        index = short_directions.index(command)
        command = directions[index]
    try:
        node.move(command)
    except:
        print 'You can\'t'
