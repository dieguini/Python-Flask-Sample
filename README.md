# Python-Flask-Sample

Easy python flask example with Docker

## Usage

### Virtual Environment (Windows)

1. Activate environemnt on [myenv](myvenv/) folder

```PS
PS > .\myvenv\Scripts\activate
(myvenv) PS >
```

**NOTE:** Should return _(myenv)_ prefix 

2. Set VsCode Environment

> View > Command Palette ...
  
> Python: Select Interpeter
  
Select
  
> [myvenv/Scripts/python.exe](myvenv/Scripts/python.exe)

3. Ensure Pip

```PS
py -m ensurepip --upgrade
```

4. Upgrade pip

```PS
(myvenv) PS > python -m pip install --upgrade pip
```

5. Install Flask, already on the [requirements.txt](requirements.txt) file

```PS
(myvenv) PS > python -m pip install -r .\requirements.txt
```

6. (Optional) Run flask application

```PS
(myvenv) PS > python -m flask --app .\flaskr\app.py run
```

7. (Optional) Run tests of application

```PS
(myvenv) PS > python -m pytest
```
