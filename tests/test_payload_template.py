import pytest
from main import load_payload_template


def test_load_payload_template_returns_dict():
    templates = load_payload_template()
    assert isinstance(templates, dict)
    assert 'default' in templates
    default_payload = templates['default']
    assert isinstance(default_payload, dict)
    # Check at least some expected keys
    for key in ('first_name', 'last_name', 'email', 'phone'):
        assert key in default_payload