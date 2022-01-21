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

pip install streamlit-aggrid

### upgrading

**IMPORTANT!!!** pip install streamlit --upgrade

## Running

```
cd app
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

## Custom Components

see [component-template/README.md](component-template/README.md)


## Streamlit Resources

- https://github.com/TangleSpace/hydralit
- https://github.com/PablocFonseca/streamlit-aggrid
- https://awesome-streamlit.org/
- https://streamlit.io/components
