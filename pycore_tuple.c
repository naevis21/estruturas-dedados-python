#include <stdio.h>
#include <stdlib.h>

struct PyTupleObject {
    PyObject_HEAD
    Py_ssize_t ob_size;
    PyObject *ob_item;
};

PyTupleObject *tuple_new(PyTypeObject *type, Py_ssize_t size) {
    PyTupleObject *tuple = PyObject_GC_New(PyTupleObject, type);
    if (tuple == NULL) {
        return NULL;
    }

    tuple->ob_size = size;
    tuple->ob_item = PyMem_Malloc(sizeof(PyObject *) * size);
    if (tuple->ob_item == NULL) {
        Py_DECREF(tuple);
        return NULL;
    }

    return tuple;
}

int tuple_setitem(PyTupleObject *tuple, Py_ssize_t index, PyObject *value) {
    if (index < 0 || index >= tuple->ob_size) {
        return -1;
    }

    tuple->ob_item[index] = value;
    Py_INCREF(value);
    return 0;
}

static PyObject *tuple_iter(PyTupleObject *tuple) {
    Py_ssize_t i;
    Py_ssize_t size = tuple->ob_size;
    PyTupleObject *iter = PyObject_GC_New(PyTupleObject, &PyTupleIter_Type);
    if (iter == NULL) {
        return NULL;
    }

    iter->ob_size = size;
    iter->ob_item = tuple->ob_item;
    iter->ob_cur = 0;

    return (PyObject *)iter;
}

static PyObject *tuple_iter_next(PyTupleObject *iter) {
    if (iter->ob_cur >= iter->ob_size) {
        return NULL;
    }

    PyObject *value = iter->ob_item[iter->ob_cur++];
    Py_INCREF(value);
    return value;
}
