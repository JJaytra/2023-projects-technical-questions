from dataclasses import dataclass
from enum import Enum
from json import dumps
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
    name = str(request.args.get("name"))
    for entity in space_database:

    animals = []

    for entity in space_database:
        if (isinstance(entity['metadata'], SpaceAnimal)):

    return dumps({
        'space_animals':})


# DO NOT TOUCH ME, thanks :D
if __name__ == '__main__':
    app.run(debug=True, port=8080)
