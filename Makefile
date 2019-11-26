obj-m+=Ex_06_dev.o  
    
ARCH :=arm  
PWD := $(shell pwd)  
     
all:  
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) ARCH=$(ARCH) modules  
demo:
	gcc -o Ex_06 Ex_06_app.c    
clean:  
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) ARCH=$(ARCH) clean
	rm -rf Ex_06
