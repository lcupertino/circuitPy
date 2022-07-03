class Capacitor:

    def __init__(name, fillable, nodename, aliases):
        self.name = name
        self.fillable = fillable
        self.nodedanem = nodename
        self.aliases = aliases

    def write_point(coordinate):
        return "("+str(coordinate["x"]) + "," + str(coordinate["y"])  +")"
   
    def write_parameters():
        parameters = "["
        list_of_parameters = this.__
        
        for key in list_of_parameters:
            parameters += str(key) + "=" + str(list_of_parameters[key]) + ", "
        
        parameters += "]"

        return parameters
    
    def draw(first_coord, second_coord):
        write_point(first_coordinate) + " to " + write_parameters() + write_point(second_coord)
