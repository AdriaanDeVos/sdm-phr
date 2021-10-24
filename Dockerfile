# This project uses debian-buster as this version still natively support python 3.7.
FROM debian:buster-slim

# Install all packages required for running and building the project and its dependencies
RUN apt-get update && apt-get install -y python3.7 python3-pip git libgmp-dev libssl-dev wget flex bison sudo

# Clone, compile and install the Charm Crypto Library
RUN git clone https://github.com/JHUISI/charm ~/charm
RUN cd ~/charm && pip3 install -r requirements.txt && ./configure.sh
RUN cd ~/charm/deps/pbc && make && ldconfig
RUN cd ~/charm && make && make install && ldconfig

# Clone, compile and install the ABE library.
RUN git clone https://github.com/sagrawal87/ABE ~/abe
RUN cd ~/abe && make && pip3 install .