def flying_new_port(destination, connection):
    # Uppdates a new location to the database where player has flown.
    connect = connection
    flying = (f'UPDATE game SET location = "{destination}";')
    cursor = connect.cursor()
    cursor.execute(flying)
    connect.commit()
    return

def cost_of_flying(fly_cost, connection):
    # Subtracts flying cost from the money player has.
    connect = connection
    moneycost=(f'UPDATE game SET money =( SELECT money -{fly_cost} FROM game ) ')
    cursor = connect.cursor()
    cursor.execute(moneycost)
    connect.commit()
    return
