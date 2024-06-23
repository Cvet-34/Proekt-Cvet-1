class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


mng = Building(35, 'многоэтажка жилое')
ofis_ = Building(35, 'офисное')


print(mng == ofis_)
mng.buildingType = 'офисное'
print(mng == ofis_)
