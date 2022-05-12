This simulation is an example of how boolean models can be integrated into Paul Macklin's team PhysiCell simulation using PhysiBoSS, in order to integrate more mechanistic details into cell-specific intracellular models.

### Run in nanoHUB : work in progress

### Run in Binder : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcorusc/Invasion_GUI/HEAD)

### Run locally with Docker and Docker-compose

'''
git clone https://github.com/marcorusc/Invasion_GUI
cd Invasion_GUI
docker-compose up -d
'''

And then open your browser to this url : http://localhost:8888/notebooks/Invasion_GUI.ipynb
### Run locally with Docker
'''
git clone https://github.com/marcorusc/Invasion_GUI
cd Invasion_GUI
docker build -t Invasion_GUI .
docker run -p 8888:8888 -d Invasion_GUI
'''
And then open your browser to this url : http://localhost:8888/notebooks/Invasion_GUI.ipynb
