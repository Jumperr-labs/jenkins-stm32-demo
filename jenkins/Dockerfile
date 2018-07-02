FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y python-pip gcc-arm-none-eabi
RUN pip install jumper
RUN pip install mbed-cli && mbed config -G ARM_PATH /usr/bin

RUN wget https://github.com/gnu-mcu-eclipse/openocd/releases/download/v0.10.0-8-20180512/gnu-mcu-eclipse-openocd-0.10.0-8-20180512-1921-centos64.tgz \
    && tar xvf gnu-mcu-eclipse-openocd-0.10.0-8-20180512-1921-centos64.tgz \
    && rm gnu-mcu-eclipse-openocd-0.10.0-8-20180512-1921-centos64.tgz

ENV OPENOCD_PATH "/gnu-mcu-eclipse/openocd/0.10.0-8-20180512-1921/"
USER jenkins

RUN pip install pyserial