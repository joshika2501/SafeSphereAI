from pydantic import BaseModel

class SensorInput(BaseModel):

    Temperature: float
    GasLevel: float
    Pressure: float
    Humidity: float
    WorkerCount: int

    Maintenance: str
    Permit: str
    MachineStatus: str
    Zone: str