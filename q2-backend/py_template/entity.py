from roundupper_100 import SpaceCowboy, SpaceAnimal, SpaceEntity, space_database


def create_entity_v1(type, location, metadata):
    if (type == 'space_cowboy'):
        entity_meta = SpaceCowboy(metadata['name'], metadata['lassoLength'])
    elif (type == 'space_animal'):
        entity_meta = SpaceAnimal(metadata['type'])

    new_entity = SpaceEntity(entity_meta, location)

    space_database.append(new_entity)
