from spanning_cidr import spanning_cidr


def test_empty_array():
    assert spanning_cidr([]) == None


def test_empty_item():
    assert spanning_cidr(['']) == None


def test_single_ip():
    assert spanning_cidr(['127.0.0.1']) == '127.0.0.1/32'


def test_empty_none():
    assert spanning_cidr(['127.0.0.1', '', None]) == '127.0.0.1/32'


def test_case1():
    assert spanning_cidr(['192.168.2.10', '192.168.1.10']
                         ) == '192.168.0.0/22'


def test_case2():
    assert spanning_cidr(['192.168.1.1', '192.168.1.2',
                          '192.168.1.3', '192.168.1.4']
                         ) == '192.168.1.0/29'


def test_case3():
    assert spanning_cidr(['92.244.247.8', '92.244.8.247']
                         ) == '92.244.0.0/16'


def test_case4():
    assert spanning_cidr(['192.168.10.10', '10.20.10.10',
                          '127.0.0.1']) == '0.0.0.0/0'


def test_case5():

    assert spanning_cidr(['10.220.1.1', '10.221.1.2',
                          '10.222.1.3', '10.223.1.5']) == '10.220.0.0/14'


def test_case6():
    assert spanning_cidr(['10.0.0.1', '10.0.0.2',
                          '10.0.0.3', '10.0.0.4']) == '10.0.0.0/29'
