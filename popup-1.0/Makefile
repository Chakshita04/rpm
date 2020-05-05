all: suid
suid: main.c
       gcc -o popup main.c
install: suid
       mkdir -p ${RPM_BUILD_ROOT}/usr/bin
       cp popup ${RPM_BUILD_ROOT}/usr/bin
~                                          

