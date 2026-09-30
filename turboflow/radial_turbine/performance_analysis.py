from .. import pysolver_view as psv
from . import geometry_model as geom

def compute_performance(
    config
):

    # Check if geometry is provided
    if config["geometry"] is None:
        raise ValueError("Geometry is not provided")

    # Compute geometry
        geometry = compute_single_operation_point(
            config["geometry"]
        )

    return geometry

def compute_single_operation_point(
    geometry
):
    # Initialize problem object
    problem = RadialTurbineProblem(geometry)

    return problem.geometry

class RadialTurbineProblem(psv.NonlinearSystemProblem):
    def __init__(self, geometry):
        """
        Initialize a RadialTurbineProblem.

        Parameters
        ----------
        config : dict
            A dictionary containing case-specific data.
        """

        # Process turbine geometry
        self.geometry = geom.calculate_full_geometry(geometry)