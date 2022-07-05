## <div align="center">Quick Start Examples</div>

<details open>
<summary>Install</summary>

Clone repo and install requirements.txt in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/)

```bash
git clone https://github.com/luosaidage/yolov5_server.git  # clone
pip install fastapi
pip install uvicorn[standard]
pip install python-multipart   # install
```

</details>

<details open>
<summary>RunServer</summary>

```bash
uvicorn main:app --reload --host 0.0.0.0
# visit 127.0.0.1:8000/docs(try it out)
```

</details>

## Chaneg weights file
```bash
vi ./det_api.py
# find def(run)
# change weight default path in this def.
```

## option(change pip origin)
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```