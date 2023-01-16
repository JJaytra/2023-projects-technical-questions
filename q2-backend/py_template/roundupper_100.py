from dataclasses import dataclass
from enum import Enum
from json import dumps
from math import sqrt
from typing import Union, NamedTuple, List
from flask import Flask, request

# from entity import create_entity_v1

# SpaceCowboy models a cowboy in our super amazing system


@dataclass
class SpaceCowboy:
    name: str
    lassoLength: int

# SpaceAnimal models a single animal in our amazing system


@dataclass
class SpaceAnimal:
    # SpaceAnimalType is an enum of all possible space animals we may encounter
    class SpaceAnimalType(Enum):
        PIG = "pig"
        COW = "cow"
        FLYING_BURGER = "flying_burger"

    type: SpaceAnimalType

# SpaceEntity models an entity in the super amazing (ROUND UPPER 100) system


@dataclass
class SpaceEntity:
    class Location(NamedTuple):
        x: int
        y: int

    metadata: Union[SpaceCowboy, SpaceAnimal]
    location: Location


# ==== HTTP Endpoint Stubs ====
app = Flask(__name__)
space_database: List[SpaceEntity] = []

# the POST /entity endpoint adds an entity to your global space database


@app.route('/entity', methods=['POST'])
def create_entity():
    # TODO: implement me
    info = request.get_json()
    # get information from json package
    entities = info['entities']
    for entity in entities:
        type = entity['type']
        location = entity['location']
        metadata = entity['metadata']
    # create_entity_v1(type, location, metadata)
        if (type == 'space_cowboy'):
            entity_meta = SpaceCowboy(
                metadata['name'], metadata['lassoLength'])
        elif (type == 'space_animal'):
            entity_meta = SpaceAnimal(metadata['type'])

        new_entity = SpaceEntity(entity_meta, location)

        space_database.append(new_entity)
    return dumps({})


# lasooable returns all the space animals a space cowboy can lasso given their name
@app.route('/lassoable', methods=['GET'])
def lassoable():
    # TODO: implement me
    ...
    name = str(request.args.get("cowboy_name"))
    # get specified space cowboy

    loc_x = 0
    loc_y = 0
    lasso_length = 0

    for entity in space_database:
        data = entity['metadata']
        if (isinstance(data, SpaceAnimal)):
            if (data['name'] == name):
                location = entity['location']
                loc_x = location['x']
                loc_y = location['y']
                lasso_length = data['lasso_length']
                break

    animals = []

    for entity in space_database:
        data = entity['metadata']
        if (isinstance(data, SpaceAnimal)):
            location = entity['location']
            x_diff = location['x'] - loc_x
            y_diff = location['y'] - loc_y
            # use pytha to get distance
            if (sqrt(pow(x_diff, 2) + pow(y_diff, 2)) <= lasso_length):
                animals.append(entity)

    return dumps({
        'space_animals': animals})


# DO NOT TOUCH ME, thanks :D
if __name__ == '__main__':
    app.run(debug=True, port=8080)
