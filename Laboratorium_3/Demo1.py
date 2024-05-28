import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

tree = ET.parse("mouse_movements.xml")
root = tree.getroot()

movements = []
for movement_elem in root.findall('movement'):
    x = int(movement_elem.find('x').text)
    y = int(movement_elem.find('y').text)
    timestamp = movement_elem.find('timestamp').text
    movements.append((x, y, timestamp))

plt.figure(figsize=(8, 6))
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')

x_values = [move[0] for move in movements]
y_values = [move[1] for move in movements]

plt.plot(x_values, y_values, 
         marker='o', 
         linestyle='-', 
         color='b')
plt.grid(True)
plt.show()
