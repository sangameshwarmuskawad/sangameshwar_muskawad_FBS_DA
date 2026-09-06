#1. to make parameter optional
def emp(id, name='', sal=20000, dept='backoffice'):
    print('ID',id)
    print('NAME',name)
    print('SALARY',sal)
    print('DEPARTMENT',dept)

emp(101, 'ABC', 50000, 'IT')
print('#####')
emp(102, 'XYZ', 70000)
print('#######')
emp(103)    