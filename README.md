We present here a model of tumor cell invasion simulated within PhysiBoSS, a multiscale framework which combines agent-based  modeling and continuous time Markov processes applied on Boolean networks. With this model, we aim to study the different modes of cell migration through an extracellular matrix by considering both spatial information obtained from the agent-based simulation and intracellular regulation obtained from the solutions of the Boolean model.

We present multiple options to run this simulation, ordered by increasing complexity :

## Run in Binder : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcorusc/Invasion_GUI/master?labpath=Invasion_GUI.ipynb)

This is the simplest, one click version to run this notebook. Note that binder is a free service, and performances of the machines might be limited. 

## Run in nanoHUB : [https://nanohub.org/resources/invasiongui](https://nanohub.org/resources/invasiongui)

nanoHub is similar to Binder, but with better machines, although it requires a free registration.

## Run locally with Docker and Docker-compose
```
git clone https://github.com/marcorusc/Invasion_GUI
cd Invasion_GUI
docker-compose up -d
```

And then open your browser to this url : http://localhost:8888/notebooks/Invasion_GUI.ipynb

## Run locally with Docker
```
git clone https://github.com/marcorusc/Invasion_GUI
cd Invasion_GUI
docker build -t invasion_gui .
docker run -p 8888:8888 -d invasion_gui
```
And then open your browser to this url : http://localhost:8888/notebooks/Invasion_GUI.ipynb

## Run locally :

Download the git folder using git clone and access the src folder :

```
git clone https://github.com/marcorusc/Invasion_GUI
cd Invasion_GUI/src
```
compile the project and move the executable into the bin folder :

```
make
cp myproj ../bin
```

exit src and run the notebook :

```
cd ..
jupyter notebook
```

### Troubleshooting

Note that by default, on MacOS, the compiler is Clang and it is not providing support for OpenMP. To solve this, please install gcc, and use it to compile the project with these extra parameters : 

```
make PHYSICELL_CPP=<gcc C++ compiler>
```

For example : 
``` 
make PHYSICELL_CPP=g++-12
```

To run the jupyter notebook, some new versions of dependencies are causing issue. To install the proper dependencies, please run the following command : 

```
python3 -m pip install -r requirements.txt
```


In some cases, it could be necessary to export the CACHEDIR before launching the notebook, if so :

```
export CACHEDIR=~/Invasion_GUI/tmpdir
```
