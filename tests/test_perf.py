import time
from selafin_benchmark.selafin import Selafin
from selafin_benchmark.telemac_file import TelemacFile
from selafin_benchmark.selafin_io_pp import ppSELAFIN
from selafin_benchmark import Serafin
import pytest


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken by {func.__name__}: {end - start} seconds")
        return result
    return wrapper

PERF = pytest.mark.parametrize(
    "f",
    [
        pytest.param("tests/data/r3d_tidal_flats.slf", id="3D"),
        pytest.param("tests/data/r2d_tidal_flats.slf", id="2D"),
    ],
)

# selafin
@PERF 
@timer
def selafin(f):
    slf = Selafin(f)
    slf.get_series([10])

# telemacFile
@timer
@PERF 
def telemac(f):
    tel = TelemacFile(f)
    for i_var in range(len(tel.varnames)):
        tel.get_data_value(i_var, 10)

# ppUtils
@timer
@PERF 
def ppUtils(f):
    ppslf = ppSELAFIN(f)
    ppslf.readHeader()
    ppslf.readVariables(10)

# PyTelTools
@timer
@PERF
def pyTelTools(f):
    with Serafin.Read(f, 'en') as resin:
        resin.read_header()  # fills resin.header (reads mesh)
        # resin.get_time()  # fills resin.time but not compulsory here
        resin.read_vars_in_frame(10)  # read all variables of a specific record
