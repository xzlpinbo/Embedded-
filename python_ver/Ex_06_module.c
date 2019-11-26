#include <Python.h>
#include <wiringPi.h>
#include <stdio.h>    
#include <sys/types.h>    
#include <sys/stat.h>    
#include <sys/ioctl.h>    
#include <fcntl.h>    
#include <unistd.h>    
#include "Ex_06.h"
#include <string.h>

#define DEVICE_FILENAME  "/dev/Ex_06"   

static PyObject *ledOnOff(PyObject *self, PyObject *args)
{
    int dev, ret;    
    ledCtl ledctl;
    char* temp;
    char* input;

    if(!PyArg_ParseTuple(args, "ss", &temp,&input))
        return NULL;

    memset(&ledctl, 0, sizeof(ledCtl));    
    int size = sizeof(ledctl);    
        
    //printf( "device file open\n");     
    dev = open( DEVICE_FILENAME, O_RDWR|O_NDELAY );    
        
    if( dev >= 0 )
    {  
        
        if (!strcmp(input, "ON"))
        {
            printf("led ON!\n");
            ledctl.ledmode = 1;
        }
        else if(!strcmp(input, "OFF"))
        {
            printf("led OFF!\n");
            ledctl.ledmode = 0;
        }
        else {
            printf("parameter error!\n");
            return NULL;
        }
        
        ledctl.pin = atoi(temp); // pin 21
        ledctl.funcNum = 1; // output

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
        
    Py_RETURN_NONE;
}

static PyMethodDef keywdarg_methods[] = {
    {"ledOnOff", (PyCFunction)ledOnOff, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}   /* sentinel */
};

static struct PyModuleDef keywdargmodule = {
    PyModuleDef_HEAD_INIT,
    "ledOnOff",
    NULL,
    -1,
    keywdarg_methods
};

PyMODINIT_FUNC PyInit_Ex_06_module(void)
{
    return PyModule_Create(&keywdargmodule);
}

