# Streamlit - Sidemenu

A streamlit component to implement collapsible menu on st_sidebar. Currently only child level, does not support grand-child level or lower level descendents.

## Installation

```
pip install streamlit-sidemenu
```

## Usage

Refer to [this file](https://github.com/ais-one/favv/blob/master/streamlit/test_sidemenu.py) for example usage.

## Custom Styling

You can customize the menu styling from the example below (which is the default styling). Pass the customized style into the component `styles` argument.

```python
styles = """
body {
  margin: 0;
}

#app {
  margin: 0;
}

/* Fixed sidenav, full height */
.sidenav {
  font-family: Arial;
  height: 100%;
  width: 100%;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  /* padding-top: 20px; */
}

/* Style the sidenav links and the dropdown button */
.sidenav a, .dropdown-btn {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 20px;
  color: #818181;
  display: block;
  border: none;
  background: none;
  width:100%;
  text-align: left;
  cursor: pointer;
  outline: none;
}

/* On mouse-over */
.sidenav a:hover, .dropdown-btn:hover {
  color: #f1f1f1;
}

/* Main content */
.main {
  margin-left: 200px; /* Same as the width of the sidenav */
  font-size: 20px; /* Increased text to enable scrolling */
  padding: 0px 10px;
}

/* Add an active class to the active dropdown button */
.sidenav a.selected {
  background-color: green;
  color: white;
}

/* Dropdown container (hidden by default). Optional: add a lighter background color and some left padding to change the design of the dropdown content */
.dropdown-container {
  display: none;
  background-color: #262626;
  padding-left: 8px;
}

/* Optional: Style the caret down icon */
.fa-caret-down {
  float: right;
  padding-right: 8px;
}
"""
```
