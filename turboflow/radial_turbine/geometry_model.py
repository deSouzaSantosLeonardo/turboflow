from turboflow import math

def calculate_full_geometry(geometry):
    """
    Computes the complete geometry of an radial turbine based on input geometric parameters.

    Parameters
    ----------
    geometry : dict
        A dictionary containing the input geometry parameters

    Returns
    -------
    dict
        A dictionary with both the original and newly computed geometry parameters.
    """

    # Create a copy of the input dictionary to avoid mutating the original
    geom = geometry.copy()

    # Get number of cascades
    number_of_cascades = len(geom["cascade_type"])

    # Get number of stages
    if number_of_cascades > 1:
        if math.is_even(number_of_cascades):
            number_of_stages = int(number_of_cascades / 2)
        else:
            number_of_stages = int((number_of_cascades - 1) / 2)
    else:
        number_of_stages = 0

    # Calculate the area
    inlet_area = 2*np.pi*geom["inlet_radius"]*geom["blade_inlet_width"]
    area_at_the_throat = geom["number_of_blades"]*geom["throat_opening"]*geom["blade_exit_width"]
    exit_area = 2*np.pi*geom["exit_mean_radius"]*geom["blade_exit_width"]

    # Calculate the radius
	exit_radius_at_the_hub = geom["exit_mean_radius"] - geom["blade_exit_width"]/2
	exit_radius_at_the_shroud = geom["exit_mean_radius"] + geom["blade_exit_width"]/2

    # Calculate the speed
    inlet_blade_speed = geom["rotational_speed"]*2*np.pi/60*geom["inlet_radius"]
    exit_blade_speed = geom["rotational_speed"]*2*np.pi/60*geom["exit_mean_radius"]

    # Calculate the pitch
    inlet_blade_pitch = 2*np.pi*geom["inlet_radius"]/geom["number_of_blades"]
    exit_blade_pitch = 2*np.pi*geom["exit_mean_radius"]/geom["number_of_blades"]

    # Create a dictionary with the newly computed parameters
    new_parameters = {
        "number_of_stages": number_of_stages,
        "number_of_cascades": number_of_cascades,
        "inlet_area": inlet_area,
        "area_at_the_throat": area_at_the_throat,
        "exit_area": exit_area,
        "exit_radius_at_the_hub": exit_radius_at_the_hub,
        "exit_radius_at_the_shroud": exit_radius_at_the_shroud,
        "inlet_blade_speed": inlet_blade_speed,
        "exit_blade_speed": exit_blade_speed,
        "inlet_blade_pitch": inlet_blade_pitch,
        "exit_blade_pitch": exit_blade_pitch,
    }

    return {**geometry, **new_parameters}
