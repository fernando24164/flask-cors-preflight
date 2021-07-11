# CORS preflight example

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Other interesting projects](#projects)

## About <a name = "about"></a>

Have you ever found problem with CORS preflight?
Do you want to know how to deal with it with Flask framework?
Well maybe, you are in the right place.

## Getting Started <a name = "getting_started"></a>

Sometimes you deploy and REST API but suddenly when you test on develop environment you found something like
[CORS Preflight](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request)

### Prerequisites

Create a python virtualenv and install requirements.txt

```shell
virtualenv --python=/usr/bin/python3 <path/to/new/virtualenv/>
```

### Installing

Once created virtualenv install the requirements file

```shell
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

To avoid this CORS preflight problem we need to implement an OPTIONS endpoint that return an Access-Control-Allow-Origin set to * to allow the request.

This OPTIONS endpoint is defined here

```python
from flask import Blueprint, Response

cat_options = Blueprint('cats', __name__)

@cat_options.route('/cats', methods=["OPTIONS"])
def cats():
    return Response(status=200, headers=[('Access-Control-Allow-Origin', '*')])

```

Launch Flask API

```shell
python src/wsgi.py
```

How to test on local

```shell
curl \
--verbose \
--request OPTIONS \
http://localhost:5000/cats \
--header 'Origin: http://localhost' \
--header 'Access-Control-Request-Headers: Origin, Accept, Content-Type' \
--header 'Access-Control-Request-Method: GET'
```

## Other interesting projects <a name = 'projects'></a>

[flask-cors](https://github.com/corydolphin/flask-cors)