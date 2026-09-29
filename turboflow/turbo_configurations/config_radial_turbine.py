from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
)
from typing import List, Literal
from enum import Enum
from typing_extensions import Annotated

CascadeTypeEnum = Enum('CascadeTypes', dict(zip([model.upper() for model in ["stator", "rotor"]], ["stator", "rotor"])))

class GeometryPerformanceAnalysis(BaseModel):
    """
    Model describing geometry parameters for performance analysis.

    Attributes
    ----------
    cascade_type : list[str]
        Types of cascades, either 'stator' or 'rotor'.
    blade_inlet_width : list[float]
        Width of the cascades inlet (each must be greater than 0).
    blade_exit_width : list[float]
        Width of the cascades exit (each must be greater than 0).
    blade_axial_length : list[float]
        Axial length of the cascades (each must be greater than 0).
    splitter_blade_axial_length : list[float]
        Axial length of the splitter blades in the cascades (each must be greater than or equal 0).
    rotational_speed : list[float]
        Rotational speed of the cascades (each must be greater than or equal 0).
    throat_opening : list[float]
        Throat opening of the cascades (each must be greater than 0).
    inlet_radius : list[float]
        Radius of the cascades inlet (each must be greater than 0).
    exit_mean_radius : list[float]
        Mean radius of the cascades exit (each must be greater than 0).
    trailing_edge_thickness : list[float]
        Thickness of the trailing edge of the cascades (each must be greater than 0).
    number_of_blades : list[float]
        Number of blades in the cascades (each must be greater than 0).
    number_of_splitter_blades : list[float]
        Number of splitter blades in the cascades (each must be greater than or equal 0).
    disk_housing_clearance_gap : list[float]
        The clearance between the disk and the housing (each must be greater than or equal 0).
    blade_casing_inlet_clearance_gap : list[float]
        The clearance between the casing and the cascades inlet (each must be greater than or equal 0).
    blade_casing_exit_clearance_gap : list[float]
        The clearance between the casing and the cascades exit (each must be greater than or equal 0).
    inlet_blade_angle : list[float]
        Edge angle of the cascades inlet, in degrees (each must be between -90 and 90).
    exit_blade_angle : list[float]
        Edge angle of the cascades exit, in degrees (each must be between -90 and 90).

    Configurations
    --------------
    extra : str, optional
        Indicates that no extra input is allowed. Default is "forbid".
    """

    model_config = ConfigDict(extra="forbid", use_enum_values=True)
    cascade_type: List[CascadeTypeEnum]
    blade_inlet_width: List[Annotated[float, Field(gt=0)]]
    blade_exit_width: List[Annotated[float, Field(gt=0)]]
    blade_axial_length: List[Annotated[float, Field(gt=0)]]
    splitter_blade_axial_length: List[Annotated[float, Field(ge=0)]]
    rotational_speed: List[Annotated[float, Field(ge=0)]]
    throat_opening: List[Annotated[float, Field(gt=0)]]
    inlet_radius: List[Annotated[float, Field(gt=0)]]
    exit_mean_radius: List[Annotated[float, Field(gt=0)]]
    trailing_edge_thickness: List[Annotated[float, Field(gt=0)]]
    number_of_blades: List[Annotated[float, Field(gt=0)]]
    number_of_splitter_blades: List[Annotated[float, Field(ge=0)]]
    disk_housing_clearance_gap: List[Annotated[float, Field(ge=0)]]
    blade_casing_inlet_clearance_gap: List[Annotated[float, Field(ge=0)]]
    blade_casing_exit_clearance_gap: List[Annotated[float, Field(ge=0)]]
    inlet_blade_angle: List[Annotated[float, Field(le=90), Field(gt=-90)]]
    exit_blade_angle: List[Annotated[float, Field(le=90), Field(gt=-90)]]

class RadialTurbine(BaseModel):
    """
    Model describing an radial turbine.

    Attributes
    ----------
    turbomachinery : str
        The type of turbomachinery, which for this class is "radial_turbine".
    geometry : GeometryPerformanceAnalysis, optional
        Object containing geometry performance analysis data. Default is None.

    Configurations
    --------------
    extra : str, optional
        Indicates that no extra input is allowed. Default is "forbid".
    """
    model_config = ConfigDict(extra="forbid")
    turbomachinery: Literal["radial_turbine"]
    geometry: GeometryPerformanceAnalysis = None