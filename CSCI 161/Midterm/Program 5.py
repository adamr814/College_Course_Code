'''
Adam Roy
CSCI 161
MIDTERM Program 5
'''
def aircraft():
    plane = {}
    tn = input("Enter plane tail number: ")
    plane['tail_number'] = tn
    lat = input("Enter plane latitiude: ")
    plane['latitude'] = lat
    lon = input("Enter plane longitude: ")
    plane['longitude'] = lon
    hed = input("Enter plane heading: ")
    plane['heading'] = hed
    spd = input("Enter plane speed: ")
    plane['speed'] = spd
    return plane

def print_plane(airplanes):
    for i in range(0, len(airplanes)):
        print(airplanes[i])
    
def main():
    airplanes = []
    p1 = aircraft()
    p2 = aircraft()
    p3 = aircraft()
    airplanes.append(p1)
    airplanes.append(p2)
    airplanes.append(p3)
    
    
    print_plane(airplanes)
main()
    
