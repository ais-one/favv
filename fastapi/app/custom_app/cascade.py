from fastapi import APIRouter, Query, HTTPException
from typing import List

router_custom_app_cascade = APIRouter(
  tags=["custom_app_cascade"],
  prefix="/cascade"
)

## cascading combobox multiple selection in vitevue example web application

countriesEastMasterList = {
  "Asia": ["Russia", "Japan", "Burma", "Indonesia", "Afghanistan"],
  "Europe": ["Russia", "Germany", "France", "Poland", "Sweden", "Italy"],
  "Africa": ["Egypt", "Nigeria", "Kenya", "Liberia"],
  "ME": ["Egypt", "Saudi Arabia", "Afghanistan"],
}

countriesWestMasterList = {
  "NA": ["United States", "Canada"],
  "SA": ["Brazil", "Argentina", "Ecuador"],
}

westCountryStatesMasterList = {
  "United States": ["California", "New York", "Ohio", "Utah", "Texas"],
  "Canada": ["Ontario", "Quebec", "BC", "Alberta"],
  "Brazil": ["B1", "B2"],
  "Argentina": ["A1", "A2", "A3"],
  "Ecuador": ["EC1", "EC2"],
}

@router_custom_app_cascade.get("/continents")
def get_continents():
  continents = ["Asia", "Europe", "NA", "SA", "Africa", "ME"]
  continents.sort()
  return continents

@router_custom_app_cascade.get("/countries")
def get_coountries_by_continents(continents: str = Query(None)):
  countriesEastList = []
  countriesWestList = []
  try:
    continents_list = continents.split(",")
    for continent in continents_list:
      countries = countriesEastMasterList.get(continent)
      if countries != None:
        countriesEastList = countriesEastList + countries
      countries = countriesWestMasterList.get(continent)
      if countries != None:
        countriesWestList = countriesWestList + countries
    return {
      "countriesEastList": countriesEastList,
      "countriesWestList": countriesWestList
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router_custom_app_cascade.get("/states")
def get_states_by_countries(countries: str = Query(None)):
  states_list = []
  try:
    countries_list = countries.split(",")
    for country in countries_list:
      states = westCountryStatesMasterList.get(country)
      if states != None:
        states_list = states_list + states
    # states_list.sort()
    return states_list
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
