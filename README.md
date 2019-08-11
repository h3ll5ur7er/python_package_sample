# Python packaging example
[TOC]

## Project structure
```
├─ mylib
│  ├─ mypack
│  │  ├─ __init__.py
│  │  └─ another_module.py
│  │
│  ├─ __init__.py
│  └─ some_module.py
│
├─ mylib_tests
│  ├─ mypack_tests
│  │  ├─ __init__.py
│  │  └─ test_another_module.py
│  │
│  ├─ __init__.py
│  └─ test_some_module.py
│
├─ README.md
└─ setup.py
```

## Installation
```
python setup.py install
```

## Testing
```
python setup.py test
```
