CC=gcc
CFLAGS=
OBJS=
LDFLAGS=
LDLIBS=-lwiringPi
obj-m+=Ex_06_dev.o  
    
ARCH :=arm  
PWD := $(shell pwd)  
     
all:  
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) ARCH=$(ARCH) modules  

Ex_06_module.so : Ex_06_module.o
	$(CC) -shared -o $@ $^ $(LDLIBS)
	
Ex_06_module.o : Ex_06_module.c
	$(CC) -c -fPIC $^ -I/usr/include/python3.7

clean:  
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) ARCH=$(ARCH) clean
	rm -rf Ex_06 Ex_06_module.o Ex_06_module.so Ex_06_module

