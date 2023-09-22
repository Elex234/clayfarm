from itertools import chain
import sys

from ObjectInfo import ObjectInfo
from CSRandom import CSRandom

def getTravelingMerchantStock(gameID, dayNumber):
    def _invalid_idx(index):
        invalid = True if index in [158, 159, 160, 161, 162, 163, 326, 341, 413, 437, 439, 454, 460, 645, 681, 682,
                                    688, 689, 690, 774, 775] else False
        return invalid

    def _invalid_str(strArray):
        conditions = strArray[3].find('-') == -1 or int(strArray[1]) <= 0 or strArray[3].find('-13') != -1 or strArray[3] == 'Quest' or strArray[0] == 'Weeds' or strArray[3].find('Minerals') != -1 or strArray[3].find('Arch') != -1
        return conditions

    rand = CSRandom(gameID+dayNumber)
    stock = {}
    for i in range(10):
        index = rand.Next(2, 790)
        while True:
            index = (index+1) % 790
            if index not in ObjectInfo or _invalid_idx(index):
                continue
            strArray = ObjectInfo[index].split('/')
            if _invalid_str(strArray):
                continue
            break
        stock[i] = [strArray[0], max(rand.Next(1, 11)*100, int(strArray[1])*rand.Next(3, 6)),
                    1 if (rand.Sample() > 0.1) else 5]
    return stock


def checkDay(gameID,day,itemList):
    a = getTravelingMerchantStock(gameID, day)
    vals = [s[0] for s in list(a.values())]
    return list(set(vals) & set(itemList))

def dayToYear(day):
	return (day-1) // 112

def findItem(gameID, item):
    day = 0
    counter = 1
    itemList = [item]
    while day == 0:
        cur_day = 7*counter - 2
        a = checkDay(gameID, cur_day, itemList)
        if a:
            day = cur_day
            break
        cur_day = 7*counter
        a = checkDay(gameID, cur_day, itemList)
        if a:
            day = cur_day
            break
        counter = counter+1
    cost = [a[1] for a in getTravelingMerchantStock(gameID, day).values() if a[0] in itemList]
    year = dayToYear(day) + 1
    return year

def checkItem(gameID, item):
    if(findItem(gameID, item) == 1):
        return True
    else:
        return False

def checkSeed(id):
    if (not checkItem(id, 'Red Cabbage') or
        not checkItem(id, 'Truffle') or
        not checkItem(id, 'Rabbit\'s Foot') or
        not checkItem(id, 'L. Goat Milk') or
        not checkItem(id, 'Large Milk') or
        not checkItem(id, 'Duck Egg')):
        return False
    return True

if __name__ == '__main__':
    id = 1412

    # How many seeds do you want? (at least)
    num_of_seeds = 10
    seedsFound = 0

    bundleAnimal    = ['L. Goat Milk', 'Large Milk', 'Large EggW', 'Large EggB', 'Duck Egg', 'Wool']
    bundleArtisan   = ['Truffle Oil', 'Cloth', 'Goat Cheese', 'Cheese', 'Honey', 'Jelly', 'Apple', 'Apricot', 'Orange', 'Peach', 'Pomegranate', 'Cherry', 'Milk', 'Goat Milk']
    bundleChef      = ['Maple Syrup', 'Fiddlehead Fern', 'Truffle', 'Poppy', 'Maki Roll', 'Fried Egg']
    bundleDye       = ['Red Mushroom', 'Sea Urchin', 'Sunflower', 'Duck Feather', 'Aquamarine', 'Red Cabbage']
    bundleEnchanter = ['Oak Resin', 'Wine', 'Rabbit\'s Foot', 'Pomegranate Sapling']
    bundleFodder    = ['Wheat', 'Hay', 'Apple Sapling']
    bundleList = [bundleAnimal, bundleChef, bundleDye, bundleEnchanter, bundleArtisan, bundleFodder]

    while(seedsFound < num_of_seeds):
        if(checkSeed(id)):
            print(id)
            seedsFound += 1
        if(checkSeed(id + 1)):
            print(id + 1)
            seedsFound += 1

        if (checkSeed(id + 758)):
            print(id + 758)
            seedsFound += 1
        if (checkSeed(id + 758 + 1)):
            print(id + 758 + 1)
            seedsFound += 1

        if (checkSeed(id + 1516)):
            print(id + 1516)
            seedsFound += 1
        if (checkSeed(id + 1516 + 1)):
            print(id + 1516 + 1)
            seedsFound += 1

        id += 689890
