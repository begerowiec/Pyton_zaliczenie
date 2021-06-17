from mlist import MList


def test_init():
    my_list_20 = MList(20)
    my_list_0 = MList(0)
    assert my_list_0 != 0
    assert my_list_20.capacity == 20


def test_add_item():
    my_list = MList(4)
    my_list.add_item(10)
    assert my_list.size == 1
    assert my_list.elements[0] == 10
    my_list.add_item(15)
    assert my_list.size == 2
    assert my_list.elements[1] == 15
    my_list.add_item(16)
    my_list.add_item(17)
    assert my_list.size == 4
    my_list.add_item(18)
    assert my_list.size == 4


def test_find():
    my_list = MList(4)
    my_list.add_item(10)
    my_list.add_item(15)
    my_list.add_item(17)
    assert my_list.find(10)
    assert my_list.find(17)
    assert my_list.find(25) is False


def test_download():
    my_list = MList(4)
    my_list.add_item(10)
    my_list.add_item(15)
    my_list.add_item(17)
    assert my_list.download(0)
    assert my_list.download(4) is False


def test_size():
    my_list = MList(4)
    assert my_list.my_size() == 0
    my_list.add_item(10)
    my_list.add_item(15)
    my_list.add_item(17)
    assert my_list.my_size() == 3
    my_list.add_item(17)
    assert my_list.my_size() == 4


def test_capacity():
    my_list = MList(4)
    assert my_list.my_capacity() == 4
    my_list.inc_capacity(10)
    assert my_list.my_capacity() == 10


def test_rem_rep():
    my_list = MList(5)
    my_list.add_item(10)
    my_list.add_item(15)
    my_list.add_item(10)
    my_list.add_item(17)
    my_list.add_item(10)
    assert my_list.my_size() == 5
    my_list.rem_rep(10)
    assert my_list.my_size() == 3
    assert my_list.download(2)


def test_reverse():
    my_list = MList(5)
    my_list.add_item(10)
    my_list.add_item(15)
    my_list.add_item(17)
    assert my_list.download(0)
    my_list.reverse()
    assert my_list.download(0)


def test_inc_capacity():
    my_list = MList(5)
    assert my_list.inc_capacity(0) is False
    assert my_list.inc_capacity(5) is False
    assert my_list.inc_capacity(6)
    assert my_list.capacity == 6
    assert my_list.inc_capacity(6) is False


def test_red_capacity():
    my_list = MList(5)
    assert my_list.red_capacity(0) is False
    assert my_list.red_capacity(5) is False
    assert my_list.red_capacity(6) is False
    assert my_list.red_capacity(3)
    assert my_list.capacity == 3
