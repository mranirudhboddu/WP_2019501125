from LRU import LRU

def main():

    obj = LRU(5)

    assert obj.put(1,"anirudh") == "Data entered"
    assert obj.put(2,"teja") == "Data entered"
    assert obj.put(3,"sanjana") == "Data entered"
    assert obj.get(1) == "anirudh"
    assert obj.get(2) == "teja"
    assert obj.get(2) == "teja"
    assert obj.put(4,"sreenivas") == "Data entered"
    assert obj.put(5,"rao") == "Data entered"
    assert obj.put(6,"boddu") == "Data entered"
    assert obj.put(7,"bhanu") == "Data entered"
    assert obj.get_cache() == {1: 'anirudh', 2: 'teja', 5: 'rao', 6: 'boddu', 7: 'bhanu'}
    print ("all test cases passed")

main()