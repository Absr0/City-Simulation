from cs1graphics import *
import time

# Create a canvas
canvas = Canvas(1200, 800, 'lightblue', 'City Scene with Helicopter, Cars, and Stadium')

# Horizontal road
horizontal_road = Rectangle(1200, 200, Point(600, 400))
horizontal_road.setFillColor('gray')
canvas.add(horizontal_road)

# Vertical road
vertical_road = Rectangle(200, 800, Point(600, 400))
vertical_road.setFillColor('gray')
canvas.add(vertical_road)

# Road markings (horizontal)
for i in range(50, 1200, 100):
    line = Rectangle(40, 5, Point(i, 400))
    line.setFillColor('white')
    canvas.add(line)

# Road markings (vertical)
for i in range(50, 800, 100):
    line = Rectangle(5, 40, Point(600, i))
    line.setFillColor('white')
    canvas.add(line)

# Sidewalks
sidewalk_top = Rectangle(1200, 50, Point(600, 350))
sidewalk_top.setFillColor('lightgray')
canvas.add(sidewalk_top)

sidewalk_bottom = Rectangle(1200, 50, Point(600, 450))
sidewalk_bottom.setFillColor('lightgray')
canvas.add(sidewalk_bottom)

sidewalk_left = Rectangle(50, 800, Point(550, 400))
sidewalk_left.setFillColor('lightgray')
canvas.add(sidewalk_left)

sidewalk_right = Rectangle(50, 800, Point(650, 400))
sidewalk_right.setFillColor('lightgray')
canvas.add(sidewalk_right)

# Crosswalks
for i in range(370, 430, 20):  # Horizontal crosswalk
    crosswalk = Rectangle(20, 50, Point(600, i))
    crosswalk.setFillColor('white')
    canvas.add(crosswalk)

for i in range(570, 630, 20):  # Vertical crosswalk
    crosswalk = Rectangle(50, 20, Point(i, 400))
    crosswalk.setFillColor('white')
    canvas.add(crosswalk)

# Stadium 
stadium = Rectangle(300, 200, Point(150, 600))
stadium.setFillColor('green')
canvas.add(stadium)

# Stadium field
field = Rectangle(260, 160, Point(150, 600))
field.setFillColor('darkgreen')
canvas.add(field)

# Stadium boundary
boundary = Rectangle(260, 160, Point(150, 600))
boundary.setBorderColor('white')
canvas.add(boundary)

# Stands
stands = Rectangle(300, 30, Point(150, 510))
stands.setFillColor('brown')  # Representing concrete stands
canvas.add(stands)


#pole
pole = Rectangle(15, 4, Point(28, 580))
pole.setFillColor('white')  # Representing concrete stands
canvas.add(pole)

pole1=pole.clone()
pole1.moveTo(28,610)
canvas.add(pole1)

pole2=pole.clone()
pole2.moveTo(270,580)
canvas.add(pole2)

pole3=pole.clone()
pole3.moveTo(270,610)
canvas.add(pole3)

p= Rectangle(5, 30, Point(36, 595))
p.setFillColor('white')  
canvas.add(p)

p1=p.clone()
p1.moveTo(263,595)
canvas.add(p1)
  
# Helicopter and Helipad
helipad = Circle(50, Point(400, 620))
helipad.setFillColor('yellow')
helipad_label = Text("H", 20, Point(400, 620))
canvas.add(helipad)
canvas.add(helipad_label)

# Helicopter starting position fixed to the top right near the helipad
helicopter = Layer()
heli_body = Rectangle(60, 20, Point(0, 0))
heli_body.setFillColor('blue')
rotor = Rectangle(100, 5, Point(0, -15))
rotor.setFillColor('black')
heli_tail = Rectangle(40, 5, Point(-50, 0))
heli_tail.setFillColor('blue')
helicopter.add(heli_body)
helicopter.add(rotor)
helicopter.add(heli_tail)
helicopter.moveTo(400, 620)  # Fixed start position on the helipad
canvas.add(helicopter)

# Create skyscrapers
def create_skyscraper(position, width, height, color, windows, window_size=10):
    building = Rectangle(width, height, position)
    building.setFillColor(color)
    canvas.add(building)
    
    # Adding windows with more realistic arrangement
    for i in range(0, height - window_size, window_size * 2):  # Correct window positions
        for j in range(0, width - window_size, window_size * 2):  # Avoid windows being too close
            window = Rectangle(window_size, window_size, Point(position.getX() + j - width / 2, position.getY() - height / 2 + i))
            window.setFillColor('lightyellow')
            canvas.add(window)

# Skyscrapers aligned outside the road
create_skyscraper(Point(65, 100), 90, 400, 'gray', 10)
create_skyscraper(Point(165, 100), 70, 400, 'lightgray', 12)
create_skyscraper(Point(265, 100), 80, 400, 'blue', 14)
create_skyscraper(Point(365, 100), 90, 400, 'white', 16)
create_skyscraper(Point(460, 100), 65, 400, 'red', 8)
create_skyscraper(Point(750, 100), 60, 400, 'yellow', 10)
create_skyscraper(Point(840, 100), 70, 400, 'green', 12)
create_skyscraper(Point(950, 100), 80, 400, 'brown', 18)
create_skyscraper(Point(1150, 100), 90, 400, 'darkgray', 16)
create_skyscraper(Point(1050, 100), 90, 400, 'black', 16)


# Draw the house body
house_body = Rectangle(120, 100, Point(1050, 700))  # Adjust position near bottom-right
house_body.setFillColor('white')
canvas.add(house_body)

# Draw the roof (with a smoother triangular appearance)
roof = Polygon(Point(990, 650), Point(1110, 650), Point(1050, 580))  # Sharper peak
roof.setFillColor('darkorange')
roof.setBorderWidth(2)
canvas.add(roof)

# Draw the door (moved to the left end)
door = Rectangle(30, 50, Point(1015, 725))  # Door positioned to the left end of the house
door.setFillColor('brown')
canvas.add(door)

# Draw the windows
window1 = Rectangle(30, 30, Point(1080, 690))  # Single window on the right
window1.setFillColor('green')
canvas.add(window1)

# Add window panes
pane_h = Path(Point(1065, 690), Point(1095, 690))  # Horizontal pane for window
pane_h.setBorderWidth(2)
canvas.add(pane_h)

pane_v = Path(Point(1080, 675), Point(1080, 705))  # Vertical pane for window
pane_v.setBorderWidth(2)
canvas.add(pane_v)

homeroad = Rectangle(290, 30, Point(845, 725))
homeroad.setFillColor('grey')
canvas.add(homeroad)

canvas.wait()


# Cars
def create_car(color, position, speed):
    car = Layer()
    body = Rectangle(60, 30, Point(0, 0))
    body.setFillColor(color)
    car.add(body)
    window = Rectangle(40, 15, Point(0, -10))
    window.setFillColor('lightblue')
    car.add(window)
    wheel1 = Circle(7, Point(-20, 10))
    wheel1.setFillColor('black')
    car.add(wheel1)
    wheel2 = Circle(7, Point(20, 10))
    wheel2.setFillColor('black')
    car.add(wheel2)
    car.moveTo(*position)
    car.speed = speed  # Assign speed to car
    car.has_moved = False  # Track if car has moved
    canvas.add(car)
    return car

# Create cars with more varied speeds
car1 = create_car('red', (200, 400), 20)    # Horizontal car with speed 20
car2 = create_car('blue', (600, 700), 5)    # Vertical car (downwards) with speed 5
car3 = create_car('green', (600, 100), 5)    # Vertical car (upwards) with speed 10

# Traffic lights
traffic_lights = []
light_states = []  # Stores the current state of each traffic light
for x, y in [(570, 370), (570, 430), (630, 370), (630, 430)]:
    traffic_light = Layer()
    pole = Rectangle(10, 30, Point(0, 0))
    pole.setFillColor('black')  
    light = Circle(10, Point(0, -15))
    light.setFillColor('green')  # Start with green light
    traffic_light.add(pole)
    traffic_light.add(light)
    traffic_light.moveTo(x, y)
    canvas.add(traffic_light)
    traffic_lights.append((traffic_light, light))
    light_states.append('green')  # Initial state is green

# Function to check if cars can move
def can_move(light):
    return light.getFillColor() == 'green'

# Animation loop
for step in range(200):
    # Traffic light control: Turn red after step 50, turn green again after step 100
    if step == 50:
        for i, (traffic_light, light) in enumerate(traffic_lights):
            light.setFillColor('red')
            light_states[i] = 'red'
    
    if step == 100:
        for i, (traffic_light, light) in enumerate(traffic_lights):
            light.setFillColor('green')
            light_states[i] = 'green'
    
    # Helicopter movement (always moving smoothly)
    helicopter.move(5, -3)

    # Ensure cars near traffic lights stop at red and move at green
    if can_move(traffic_lights[0][1]) and car1.getReferencePoint().getX() < 1230:
        car1.move(car1.speed, 0)  # Horizontal car moves at its speed
    
    if can_move(traffic_lights[1][1]) and car2.getReferencePoint().getY() > -20:
        car2.move(0, -car2.speed)  # Vertical car moves upwards at its speed
    
    if can_move(traffic_lights[2][1]) and car3.getReferencePoint().getY() < 725:
        car3.move(0, car3.speed)  # Vertical car moves downwards at its speed

    # Pause to create smooth animation
    time.sleep(0.05)

# Move the blue car to the house alongside it
target_position_x = 930  # X-coordinate of the door
while car3.getReferencePoint().getX() < target_position_x or car3.getReferencePoint().getY() < target_position_y:
    # Move horizontally until it reaches the door
    if car3.getReferencePoint().getX() < target_position_x:
        car3.move(car3.speed, 0)  # Move right
    
canvas.wait()
