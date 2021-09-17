## Introduction

For really rapid prototyping...


### Install env
```
python -m venv dev
```

### activate env in windows

```
dev\Scripts\activate
```
### activate env in linux

```
source dev/bin/activate 
```


### install

pip install streamlit numpy pandas plotly pydeck

### upgrading

pip install streamlit --upgrade

## Running

```
cd app_car_accidents
streamlit run app.py
# --logger.level=debug
```


### Code Profiling
- memory_profiling
- execution time profiling

#### Tools
- cProfile
- memory_profiler
  - memory
- scalene
- line_profiler
  - time

#### Types of Profiling
- deterministic
- statistical

#### Memory Profiling
```
pip install memory_profiler
```