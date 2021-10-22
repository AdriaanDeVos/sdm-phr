FROM debian:buster-slim

RUN apt-get update && apt-get install -y python3.7 python3-pip git libgmp-dev libssl-dev wget flex bison sudo
RUN git clone https://github.com/JHUISI/charm ~/charm
RUN cd ~/charm && pip3 install -r requirements.txt && ./configure.sh
RUN cd ~/charm/deps/pbc && make && ldconfig
RUN cd ~/charm && make && make install && ldconfig
#RUN git clone https://github.com/zeutro/openabe ~/openabe
#RUN cd ~/openabe && ./deps/install_pkgs.sh
#RUN cd ~/openabe && . ./env && make
RUN git clone https://github.com/sagrawal87/ABE ~/abe
RUN cd ~/abe && make && pip3 install .