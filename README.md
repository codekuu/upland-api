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
>>> from upland.developers import UplandDevelopersAPI
>>> 
>>> api = UplandDevelopersAPI('your-api-key', server='development/ production')
```

## Available Resources

```python
>> api.auth
>> api.user
>> api.containers
>> api.tracks
>> api.buildings
>> api.cities
>> api.properties
>> api.neighborhoods
>> api.collections
>> api.treasures_history
```

### Get properties

* Get properties in San Francisco (City ID: 1)
```python
>>> r = api.properties.get(cityId=1)
>>> r
```

### Get Neighborhoods

* Get neighborhoods in San Francisco (City ID: 1)
```python
>>> r = api.neighborhoods.get(cityId=1)
>>> r
```

* Get all neighborhoods
```python
>>> r = api.neighborhoods.get()
>>> r
```

* Get neighborhoods by name
```python
>>> r = api.neighborhoods.get(textSearch="Financial")
>>> r
```

* Get neighborhoods by city and name
```python
>>> r = api.neighborhoods.get(cityId=1, textSearch="Financial")
>>> r
```
