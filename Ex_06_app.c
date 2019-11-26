#include <stdio.h>    
#include <sys/types.h>    
#include <sys/stat.h>    
#include <sys/ioctl.h>    
#include <fcntl.h>    
#include <unistd.h>    
#include "Ex_06.h"
#include <string.h>

#define DEVICE_FILENAME  "/dev/Ex_06"    
        
int main(int argc, char* argv[])    
{    
    int dev, ret;    
    ledCtl ledctl;

    memset(&ledctl, 0, sizeof(ledCtl));    
    int size = sizeof(ledctl);    
        
    //printf( "device file open\n");     
    dev = open( DEVICE_FILENAME, O_RDWR|O_NDELAY );    
        
    if( dev >= 0 )
    {  
        
        if (!strcmp(argv[2], "ON"))
        {
            printf("led ON!\n");
            ledctl.ledmode = 1;
        }
        else if(!strcmp(argv[2], "OFF"))
        {
            printf("led OFF!\n");
            ledctl.ledmode = 0;
        }
        else {
            //printf("parameter error!\n");
            return -1;
        }
        
        //ledctl.pin = 21; // pin 21
        ledctl.pin = atoi(argv[1]);
        printf("pin: %d\n", ledctl.pin);
        ledctl.funcNum = 1; // output
        // ledctl.act.count = 10;
        // ledctl.act.interval = 2;

        /* 
        printf( "App : write something\n");    
        ret = write(dev, (char *)&ledCtl, size);    
        printf( "%s %dbytes\n", buf, ret );    
        
        printf( "App : read something\n");    
        ret = read(dev, buf2, 100 );    
        printf( "%s %dbytes\n", buf2, ret );    
        */
        //printf( "ioctl function call\n");
        ret = ioctl(dev, MY_IOCSQSET, &ledctl ); // 커널로 데이터 가져오기   
        //printf( "ret = %d\n", ret );    

        ret = ioctl(dev, MY_IOCSQ_GPIO_SETFUNC); // GPIO 포트 설정
        //printf( "ret = %d\n", ret );    

        ret = ioctl(dev, MY_IOCSQ_GPIO_ACTIVE);    
        //printf( "ret = %d\n", ret );    
       
        //printf( "device file close\n");    
        ret = close(dev);    
        //printf( "ret = %d\n", ret );    
    }    
        
    return 0;    
}
