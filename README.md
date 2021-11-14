# Secure Data Management - Personal Health Record System
Provides an implementation of CP-ABE on the assignment for personal health records for the Secure Data Management course on Twente University.

## Running the project
1. Install docker on your system: https://docs.docker.com/engine/install/
2. Build the docker image with: `docker build -t sdm .`
3. Run the docker image with: `docker run -it sdm`

## Configuring the development environment
1. For running and debugging our code you need to do this within the docker container as the libraries are otherwise not installed. Therefore we suggest using Pycharm Professional (available with a student license) and to use their docker integration. https://www.jetbrains.com/pycharm/download/
2. Make sure to configure the docker integration so it can connect to the docker API: https://www.jetbrains.com/help/pycharm/docker-connection-settings.html
3. Configure a remote interpreter to use the `sdm:latest` image and the `python3` interpreter: https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html

For manual testing you could use shared folders: `docker run -it --mount type=bind,source="$(pwd)",target=/sdm-phr sdm`  
If you are using a different operating system than linux you might have to change the `$(pwd)` to the source directory containg the code.  

## Recommendations
During the development of the project our research indicated the following options we could pursue:
1. ABE (2020) with Python 3.7 according to this installation: https://lrusso96.github.io/blog/cryptography/2021/03/04/charm-setup.html
2. open-ABE (2021) building CLI executables within a docker instance
3. Manually trying to copy and import files from https://github.com/JHUISI/charm/blob/dev/charm/toolbox/ to circumvent the library compile
4. Manually rebuilding existing libraries to replace the non-compiling and outdated cryptographic library

## Possible libraries found
These libraries are sorted on their popularity and how recent they have been updated.
- C++ (2021) (171 star): https://github.com/zeutro/openabe
- Rust (2021) (42 star): https://github.com/Fraunhofer-AISEC/rabe
- Python (2020) (90 star): https://github.com/sagrawal87/ABE
- Go (2020) (15 star): https://github.com/marcellop71/mosaic
- C++ (2020) (2 star): https://github.com/babbadeckl/ABE-RestAPI
- C (2020) (0 star): https://github.com/Juve45/abe-cas
- Java (2018) (10 star): https://github.com/rajatks/CP-ABE
- Python (2016) (17 star): https://github.com/jfdm/pyPEBEL

### C++ 2021 (open-ABE)
We were unable to compile this project as the Make process showed errors that we couldnt resolve.

### Python 2020 (ABE)
We were unable to get this project to work as it required the charm-crypto library from 2011 which is incompatible with modern operating systems.
