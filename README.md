## Spanning Cidr

Function that accepts a sequence of IP addresses returning a single subnet that is large enough to span the lower and upper bound IP addresses with a possible overlap on either end.

### Installation

Run `pip install spanning-cidr`

### How To Use

```Python
from spanning_cidr import spanning_cidr

spanning_cidr(['192.168.1.1','192.168.1.2', '192.168.1.3', '192.168.1.4'])
>> '192.168.1.0/29'

spanning_cidr(['192.168.2.10', '192.168.1.10'])
>> '192.168.0.0/22'
```
