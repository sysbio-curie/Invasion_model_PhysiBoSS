This simulation is an example of how boolean models can be integrated into Paul Macklin's team PhysiCell simulation using PhysiBoSS, in order to integrate more mechanistic details into cell-specific intracellular models.

### Run locally :

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

it could be necessary to export the CACHEDIR, if so :

```
export CACHEDIR=~/Invasion_GUI/tmpdir
```

### Run in nanoHUB : work in progress

### Run in Binder : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcorusc/Invasion_GUI/HEAD)

### Run locally with Docker and Docker-compose
```
git clone https://github.com/marcorusc/Invasion_GUI
cd Invasion_GUI
docker-compose up -d
```

And then open your browser to this url : http://localhost:8888/notebooks/Invasion_GUI.ipynb

### Run locally with Docker
```
git clone https://github.com/marcorusc/Invasion_GUI
cd Invasion_GUI
docker build -t invasion_gui .
docker run -p 8888:8888 -d invasion_gui
```
And then open your browser to this url : http://localhost:8888/notebooks/Invasion_GUI.ipynb
