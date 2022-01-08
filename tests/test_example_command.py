from foo.commands.example import foo


def test_example_command():
    assert foo() == "foo"
