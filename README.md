# Upland API Wrapper

**upland-api** is a Python wrapper for the Upland.me API endpoints.
**upland-api** do currently only support the Developers API.
**upland-api** works with Python >= 3.6

# Installation

```bash
$ pip install upland-api
```

# Usage

```python
>>> from upland_api import UplandDevelopersAPI
>>> from upland_api import UplandPublicAPI
>>>
>>> UplandDevAPI = UplandDevelopersAPI(api_key="XXXX", logging=True)
>>> UplandPubAPI = UplandPublicAPI(api_key="XXXX", logging=True)
```

## Available Resources

```python
>> UplandDevAPI.auth
>> UplandDevAPI.buildings
>> UplandDevAPI.cities
>> UplandDevAPI.collections
>> UplandDevAPI.containers
>> UplandDevAPI.neighborhoods
>> UplandDevAPI.properties
>> UplandDevAPI.tracks
>> UplandDevAPI.treasures_history
>> UplandDevAPI.user


>> UplandPubAPI.feature
>> UplandPubAPI.settings
```

## Examples

### Get properties

- Get properties in San Francisco (City ID: 1)

```python
>>> r = UplandDevAPI.properties.get_properties(cityId=1)
>>> r
```

### Get Neighborhoods

- Get neighborhoods in San Francisco (City ID: 1)

```python
>>> r = UplandDevAPI.neighborhoods.get_neighborhoods(cityId=1)
>>> r
```

- Get all neighborhoods

```python
>>> r = UplandDevAPI.neighborhoods.get_neighborhoods()
>>> r
```

- Get neighborhoods by name

```python
>>> r = UplandDevAPI.neighborhoods.get_neighborhoods(textSearch="Financial")
>>> r
```

- Get neighborhoods by city and name

```python
>>> r = UplandDevAPI.neighborhoods.get_neighborhoods(cityId=1, textSearch="Financial")
>>> r
```
