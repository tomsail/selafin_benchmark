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
Time taken by telemac: 0.04706144332885742 seconds
Time taken by selafin: 0.006855964660644531 seconds
Time taken by ppUtils: 0.04119277000427246 seconds
```
with HERMES
```
Time taken by telemac: 0.0003180503845214844 seconds
Time taken by selafin: 0.007878303527832031 seconds
Time taken by ppUtils: 0.041509151458740234 seconds
```