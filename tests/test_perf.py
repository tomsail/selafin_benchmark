import time
import numpy as np
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


# selafin@PERF
@timer
def selafin(f):
    slf = Selafin(f)
    data = np.zeros((len(slf.tags["times"]), len(slf.varnames), slf.npoin3))
    for it, t_ in enumerate(slf.tags["times"]):
        data[it] = slf.get_values(it)


# telemacFile
@timer
@PERF
def telemac(f):
    tel = TelemacFile(f)
    data = np.zeros((len(tel.times), len(tel.varnames), tel.npoin3))
    for it, t_ in enumerate(tel.times):
        for iv, varname in enumerate(tel.varnames):
            data[it, iv] = tel.get_data_value(varname, it)


# ppUtils
@timer
@PERF
def ppUtils(f):
    ppslf = ppSELAFIN(f)
    ppslf.readHeader()
    ppslf.readTimes()
    data = np.zeros((len(ppslf.time), len(ppslf.vars), ppslf.NPOIN))
    for it, t_ in enumerate(ppslf.time):
        data[it] = ppslf.readVariables(it)


# PyTelTools
@timer
@PERF
def pyTelTools(f):
    with Serafin.Read(f, "en") as resin:
        resin.read_header()  # fills resin.header (reads mesh)
        resin.get_time()  # fills resin.time but not compulsory here
        data = np.zeros(
            (resin.header.nb_frames, len(resin.header.var_IDs), resin.header.nb_nodes)
        )
        for it in range(resin.header.nb_frames):
            data[it] = resin.read_vars_in_frame(it)
