'''test the flask app'''
import requests
import json

def test_add():
    print('test add')
    url = 'http://localhost:5000/add'
    data = {'x': 1, 'y': 2}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 3

    '''test string input as x'''
    print('test string input as x')
    data = {'x': '1', 'y': 2}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 3


    '''test invalid input'''
    print('test invalid input')
    data = {'x': 'a', 'y': 2}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 'Invalid Input'

    '''test wrong endpoint'''
    print('test wrong endpoint')
    url = 'http://localhost:5000/adds'
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 404

'''write more tests for subtract, multiply, and divide'''

def test_substract():
    print('test substract')
    url = 'http://localhost:5000/subtract'
    data = {'x': 1, 'y': 2}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == -1

    '''test invalid input'''
    print('test invalid input')
    data = {'x': 'a', 'y': 2}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 'Invalid Input'

    '''test wrong endpoint'''
    print('test wrong endpoint')
    url = 'http://localhost:5000/subtracts'
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 404

def test_multiply():
    print('test multiply')
    url = 'http://localhost:5000/multiply'
    data = {'x': 1, 'y': 2}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 2

    '''test invalid input'''
    print('test invalid input')
    data = {'x': 'a', 'y': 2}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 'Invalid Input'

    '''test wrong endpoint'''
    print('test wrong endpoint')
    url = 'http://localhost:5000/multiplies'
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 404

def test_divide():
    print('test divide')
    url = 'http://localhost:5000/divide'
    data = {'x': 1, 'y': 2}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 0.5

    '''test invalid input'''
    print('test invalid input')
    data = {'x': 'a', 'y': 2}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 'Invalid Input'

    '''test zero division'''
    print('test zero division')
    data = {'x': 1, 'y': 0}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 'Cannot divide by zero'

    '''test zero division as string'''
    print('test zero division as string')
    data = {'x': 1, 'y': '0'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    assert r.json() == 'Cannot divide by zero'

    '''test wrong endpoint'''
    print('test wrong endpoint')
    url = 'http://localhost:5000/divides'
    r = requests.post(url, data=json.dumps(data), headers=headers)
    assert r.status_code == 404

if __name__ == '__main__':
    test_add()
    test_substract()
    test_multiply()
    test_divide()

'''run the tests'''
# $ python test-flask.py
