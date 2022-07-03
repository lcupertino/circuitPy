class Capacitor:

    def __init__(self, name, fillable, nodename, aliases):
        self.name = name
        self.fillable = fillable
        self.nodedanem = nodename
        self.aliases = aliases
    
    def obtain_parameters(self):
        list_of_parameters = self.__dir__()

        for i, elem in enumerate(list_of_parameters):
            if("_" in elem.split()):
                list_of_parameters.pop(i)

        return list_of_parameters

    def write_point(self, coordinate):
        return "("+str(coordinate["x"]) + "," + str(coordinate["y"])  +")"
   
    def write_parameters(self):
        parameters = "["
        list_of_parameters = this.__
        
        for key in list_of_parameters:
            parameters += str(key) + "=" + str(list_of_parameters[key]) + ", "
        
        parameters += "]"

        return parameters
    
    def draw(self, first_coord, second_coord):
        return self.write_point(first_coord) + " to " + self.write_point(second_coord)


test_capacitor = Capacitor("capacitor", True, True, "C")
first_coord = {"x": 1, "y": 2}
second_coord = {"x": 1, "y": 3}

print(test_capacitor.write_point(first_coord))
print(test_capacitor.draw(first_coord, second_coord))
print(test_capacitor.obtain_parameters())
