from nose.tools import *
from exercise49.parser import *

def test_peek():
    assert_equal(peek([]), None)
    assert_equal(peek([('token', 'word')]), 'token')
    assert_equal(peek([('token', 'word'), ('token2', 'word2')]), 'token')

def test_match():
    assert_raises(MatchError, match, [], 'token')
    assert_raises(MatchError, match, [('token', 'word')], 'token2')
    assert_raises(MatchError, match, [('token', 'word'), ('token2', 'word2')], 'token2')
    assert_equal(match([('token', 'word')], 'token'), ('token', 'word'))
    assert_equal(match([('token', 'word'), ('token2', 'word2')], 'token'), ('token', 'word'))

def test_skip():
    word_list1 = []
    skip(word_list1, 'token')
    assert_equal(word_list1, [])

    word_list2 = [('token1', 'word1')]
    skip(word_list2, 'token1')
    assert_equal(word_list2, [])

    word_list2 = [('token1', 'word1')]
    skip(word_list2, 'token2')
    assert_equal(word_list2, [('token1', 'word1')])

    word_list3 = [('token1', 'word1'), ('token2', 'word2')]
    skip(word_list3, 'token1')
    assert_equal(word_list3, [('token2', 'word2')])

    word_list3 = [('token1', 'word1'), ('token2', 'word2')]
    skip(word_list3, 'token2')
    assert_equal(word_list3, [('token1', 'word1'), ('token2', 'word2')])

    word_list4 = [('token1', 'word1'), ('token1', 'word2')]
    skip(word_list4, 'token1')
    assert_equal(word_list4, [])

    word_list4 = [('token1', 'word1'), ('token1', 'word2')]
    skip(word_list4, 'token2')
    assert_equal(word_list4, [('token1', 'word1'), ('token1', 'word2')])

    word_list5 = [('token1', 'word1'), ('token1', 'word2'), ('token2', 'word3')]
    skip(word_list5, 'token1')
    assert_equal(word_list5, [('token2', 'word3')])

    word_list5 = [('token1', 'word1'), ('token1', 'word2'), ('token2', 'word3')]
    skip(word_list5, 'token2')
    assert_equal(word_list5, [('token1', 'word1'), ('token1', 'word2'), ('token2', 'word3')])

def test_parse_subject():
    assert_equal(parse_subject([('stop', 'word1'), ('stop', 'word1'), ('noun', 'word2'), ('token', 'word3')]), ('noun', 'word2'))
    assert_equal(parse_subject([('stop', 'word1'), ('verb', 'word2'), ('token', 'word3')]), ('noun', 'player'))
    assert_equal(parse_subject([('verb', 'word1'), ('token', 'word2')]), ('noun', 'player'))
    assert_raises(MatchError, parse_subject, [('token1', 'word1'), ('token2', 'word2')])
    assert_raises(MatchError, parse_subject, [('stop', 'word')])
    assert_raises(MatchError, parse_subject, [])

def test_parse_verb():
    assert_equal(parse_verb([('stop', 'word1'), ('stop', 'word1'), ('verb', 'word2')]), ('verb', 'word2'))
    assert_equal(parse_verb([('verb', 'word2')]), ('verb', 'word2'))
    assert_raises(MatchError, parse_verb, [('stop', 'word1')])
    assert_raises(MatchError, parse_verb, [])

def test_parse_object():
    assert_equal(parse_object([('stop', 'word1'), ('stop', 'word1'), ('noun', 'word2')]), ('noun', 'word2'))
    assert_equal(parse_object([('stop', 'word1'), ('stop', 'word1'), ('direction', 'word2')]), ('direction', 'word2'))
    assert_equal(parse_object([('noun', 'word2')]), ('noun', 'word2'))
    assert_equal(parse_object([('direction', 'word2')]), ('direction', 'word2'))
    assert_raises(MatchError, parse_object, [])
    assert_raises(MatchError, parse_object, [('stop', 'word')])
    assert_raises(MatchError, parse_object, [('verb', 'word')])

def test_parse_sentence():
    assert_equal(parse_sentence([('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')]).subject,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')).subject)
    assert_equal(parse_sentence([('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')]).verb,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')).verb)
    assert_equal(parse_sentence([('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')]).object,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')).object)

    assert_equal(parse_sentence([('verb', 'word2'), ('noun', 'word3')]).subject,
                 Sentence(('noun', 'player'), ('verb', 'word2'), ('noun', 'word3')).subject)
    assert_equal(parse_sentence([('verb', 'word2'), ('noun', 'word3')]).verb,
                 Sentence(('noun', 'player'), ('verb', 'word2'), ('noun', 'word3')).verb)
    assert_equal(parse_sentence([('verb', 'word2'), ('noun', 'word3')]).object,
                 Sentence(('noun', 'player'), ('verb', 'word2'), ('noun', 'word3')).object)

    assert_equal(parse_sentence([('stop', 'word'), ('noun', 'word1'), ('verb', 'word2'), ('stop', 'word'), ('noun', 'word3')]).subject,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')).subject)
    assert_equal(parse_sentence([('stop', 'word'), ('noun', 'word1'), ('verb', 'word2'), ('stop', 'word'), ('noun', 'word3')]).verb,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')).verb)
    assert_equal(parse_sentence([('stop', 'word'), ('noun', 'word1'), ('verb', 'word2'), ('stop', 'word'), ('noun', 'word3')]).object,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('noun', 'word3')).object)

    assert_equal(parse_sentence([('noun', 'word1'), ('verb', 'word2'), ('direction', 'word3')]).subject,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('direction', 'word3')).subject)
    assert_equal(parse_sentence([('noun', 'word1'), ('verb', 'word2'), ('direction', 'word3')]).verb,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('direction', 'word3')).verb)
    assert_equal(parse_sentence([('noun', 'word1'), ('verb', 'word2'), ('direction', 'word3')]).object,
                 Sentence(('noun', 'word1'), ('verb', 'word2'), ('direction', 'word3')).object)

    assert_raises(MatchError, parse_sentence, [('stop', 'word')])
