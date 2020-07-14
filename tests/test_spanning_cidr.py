from spanning_cidr import spanning_cidr


def test_address_empty():
    assert spanning_cidr([]) == None


def test_address_empty():
    assert spanning_cidr(['']) == None


def test_address_single():
    assert spanning_cidr(['127.0.0.1']) == '127.0.0.1/32'


def test_address_one_and_empty():
    assert spanning_cidr(['127.0.0.1', '']) == '127.0.0.1/32'


def test_address_has_empty_and_long_range():
    assert spanning_cidr(['127.0.0.1', '', '86.59.118.159']) == '64.0.0.0/2'


def test_address_not_net_incl():
    assert spanning_cidr(['86.59.118.159', '86.59.118.157']
                         ) == '86.59.118.156/30'


def test_address_many_not_net_incl():
    assert spanning_cidr(['86.59.118.147', '86.59.118.159',
                          '86.59.118.157']) == '86.59.118.144/28'


def test_address_equals_included():
    assert spanning_cidr(['86.59.118.144', '86.59.118.147', '86.59.118.159',
                          '86.59.118.157', '86.59.118.149']) == '86.59.118.144/28'


def test_address_first_biggest():
    assert spanning_cidr(['86.59.118.159', '86.59.118.147', '86.59.118.157',
                          '86.59.118.149', '86.59.118.144']) == '86.59.118.144/28'
