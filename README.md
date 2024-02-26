# selafin speed bench

to install the selafin benchmark: 
```
mamba create -n selafin_benchmark python=3.11
mamba activate selafin_benchmark
poetry install
```

to enable hermes: 

```
mamba create -n telemac -c tomsail opentelemac
mamba create -n selafin_benchmark python=3.11
mamba activate telemac
mamba activate --stack selafin_benchmark
poetry install
```

result for the 3D file in `tests/data/r3d_tidal_flats.slf`: 
```
Warning: Using SerafinFile. It is recommended to compile Hermes api
Time taken by pyTelTools: 0.0059587955474853516 seconds
Time taken by ppUtils: 0.025746583938598633 seconds
Warning: Using SerafinFile. It is recommended to compile Hermes api
Time taken by telemac: 0.05089855194091797 seconds
Time taken by selafin: 0.04546236991882324 seconds
```
with HERMES
```
Time taken by pyTelTools: 0.00857234001159668 seconds
Time taken by ppUtils: 0.02410888671875 seconds
Time taken by telemac: 0.0050008296966552734 seconds
Time taken by selafin: 0.04771304130554199 seconds
```
---
results for a ERA5 monthly wind file (size: 9 GB):
```
Time taken by pyTelTools: 6.695765495300293 seconds
Time taken by ppUtils: 1.4621760845184326 seconds
Warning: Using SerafinFile. It is recommended to compile Hermes api
Time taken by telemac: 85.85983943939209 seconds
Time taken by selafin: 98.93528032302856 seconds
```
with HERMES:
```
Time taken by pyTelTools: 6.644935131072998 seconds
Time taken by ppUtils: 529.0695465195996 seconds
Time taken by telemac: 9.467883110046387 seconds
Time taken by selafin: 98.02847123146057 seconds
```