// Copyright eryksun <http://stackoverflow.com/users/205580/eryksun>
// http://stackoverflow.com/questions/15459684/transmission-bytearray-from-python-to-c-and-return-it

#include <Python.h>

static PyObject *fast_xor_inplace(PyObject *self, PyObject *args) {
    PyObject *arg1, *arg2;
    Py_buffer buffer1, buffer2;

    if (!PyArg_ParseTuple(args, "O|O:fast_xor_inplace", &arg1, &arg2))
        return NULL;

    if (PyObject_GetBuffer(arg1, &buffer1, PyBUF_WRITABLE) < 0)
        return NULL;

    if (PyObject_GetBuffer(arg2, &buffer2, PyBUF_WRITABLE) < 0)
        return NULL;

    char *buf1 = (char*)buffer1.buf;
    char *buf2 = (char*)buffer2.buf;
    for(int i = 0; i < buffer1.len; i++)
        buf1[i] ^= buf2[i];

    PyBuffer_Release(&buffer1);
    PyBuffer_Release(&buffer2);
    Py_INCREF(Py_None);
    return Py_None;
}

/*
static PyObject *fast_xor_inplace2(PyObject *self, PyObject *args) {
    PyObject *arg1;
    unsigned char arg2 = 0;
    Py_buffer buffer;

    if (!PyArg_ParseTuple(args, "O|b:fast_xor_inplace", &arg1, &arg2))
        return NULL;

    if (PyObject_GetBuffer(arg1, &buffer, PyBUF_WRITABLE) < 0)
        return NULL;

    char *buf = (char*)buffer.buf;
    for(int i = 0; i < buffer.len; i++)
        buf[i] ^= arg2;

    PyBuffer_Release(&buffer);
    Py_INCREF(Py_None);
    return Py_None;
}
*/

static PyObject *fast_xor(PyObject *self, PyObject *args) {
    PyObject *arg1;
    unsigned char arg2 = 0;
    Py_buffer buffer;

    if (!PyArg_ParseTuple(args, "O|b:fast_xor", &arg1, &arg2))
        return NULL;

    if (PyObject_GetBuffer(arg1, &buffer, PyBUF_SIMPLE) < 0)
        return NULL;

    PyObject *result = PyUnicode_FromStringAndSize(NULL, buffer.len);
    if (result == NULL)
        return NULL;

    char *buf = (char*)buffer.buf;
    char *str = PyBytes_AS_STRING(result);
    for(int i = 0; i < buffer.len; i++)
        str[i] = buf[i] ^ arg2;

    PyBuffer_Release(&buffer);
    return result;
}

static PyMethodDef fastxor_methods[] = {
     {"fast_xor", fast_xor, METH_VARARGS, "fast xor"},
     {"fast_xor_inplace", fast_xor_inplace, METH_VARARGS, "fast inplace xor"},
     {NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3
static PyModuleDef fastxor_module = {
    PyModuleDef_HEAD_INIT,
    "python-fastxor",  // name of module
    NULL, // module documentation, may be NULL
    -1,   // size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
    fastxor_methods
};

PyMODINIT_FUNC PyInit_fastxor(void) {
    return PyModule_Create(&fastxor_module);
}
#else
PyMODINIT_FUNC initfastxor(void) {
    Py_InitModule3("fastxor", fastxor_methods, NULL);
};
#endif
