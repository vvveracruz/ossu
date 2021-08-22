#   using tuples as dict keys can be convenient
#   ex: airplane flights

flight_data = {}

def add_flight_data(flight_number, day, departure_time):
    flight_data[(flight_number, day)]=departure_time

def delete_flight_data(flight_number, day):
    flight_data((flight_number, day))=None

if __name__=="__main__":
    add_flight_data('FR2567', '23 Sept', '7am')
    print(flight_data)
    print(flight_data[('FR2567', '23 Sept')])