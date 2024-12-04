def demonstrate_tuples_for_coordinates():
    point_1 = (3, 5)
    point_2 = (7, 8)
    print("Point 1 coordinates:", point_1)
    print("Point 2 coordinates:", point_2)
    x1, y1 = point_1
    x2, y2 = point_2
    print(f"Point 1: x = {x1}, y = {y1}")
    print(f"Point 2: x = {x2}, y = {y2}")
    import math
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance between Point 1 and Point 2: {distance:.2f}")
demonstrate_tuples_for_coordinates()
