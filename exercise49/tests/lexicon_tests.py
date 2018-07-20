from nose.tools import *
from exercise49.lexicon import *


def test_directions():
    assert_equal(scan("north"), [('direction', 'north')])
    result = scan("north  South   east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(scan("go"), [('verb', 'go')])
    result = scan("go Kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(scan("the"), [('stop', 'the')])
    result = scan('the In of')
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_numbers():
    assert_equal(scan("1234"), [('number', 1234)])
    result = scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(scan("ASDFADFASDF"), [('error', 'asdfadfasdf')])
    result = scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'ias'),
                          ('noun', 'princess')])
