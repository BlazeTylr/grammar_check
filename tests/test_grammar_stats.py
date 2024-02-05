from lib.grammar_stats import *

def test_grammar_stats_check_return_false():
    sentence = GrammarStats()
    actual = sentence.check('Hello there')
    expectedd = False
    assert actual == expectedd

def test_grammar_stats_check_return_true():
    sentence = GrammarStats()
    actual = sentence.check('Hello there!')
    expectedd = True
    assert actual == expectedd

def test_grammar_stats_percentage_true_values():
    to_check = GrammarStats()
    actual = to_check.check('Hello there!')
    actual = to_check.percentage_good()
    expected = '100%'
    assert actual == expected

def test_grammar_stats_percentage_false_values():
    to_check = GrammarStats()
    actual = to_check.check('hello there')
    actual = to_check.percentage_good()
    expected = '0%'
    assert actual == expected

def test_grammar_stats_percentage_mixed_values():
    to_check = GrammarStats()
    actual = to_check.check('hello there')
    actual = to_check.check('Hello there!')
    actual = to_check.percentage_good()
    expected = '50%'
    assert actual == expected