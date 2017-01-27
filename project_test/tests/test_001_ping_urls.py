"""
Some dummy pinging to ensure urls are consistent

WARNING: Keep this syncrhonized with enabled urls files
"""
import pytest

from django.core.urlresolvers import reverse


@pytest.mark.parametrize("url_name,url_args,url_kwargs", [
    ('home', [], {}),
    ('crispy-foundation:crispy-demo-form-fieldsets', [], {'foundation_version':5}),
    ('crispy-foundation:crispy-demo-form-tabs', [], {'foundation_version':5}),
    ('crispy-foundation:crispy-demo-form-accordions', [], {'foundation_version':5}),
    ('crispy-foundation:crispy-demo-success', [], {'foundation_version':5}),
    ('crispy-foundation:crispy-demo-form-fieldsets', [], {'foundation_version':6}),
    ('crispy-foundation:crispy-demo-form-tabs', [], {'foundation_version':6}),
    ('crispy-foundation:crispy-demo-form-accordions', [], {'foundation_version':6}),
    ('crispy-foundation:crispy-demo-success', [], {'foundation_version':6}),
])
def test_ping_reverse_urlname(client, url_name, url_args, url_kwargs):
    """Ping reversed url names"""
    response = client.get(reverse(url_name, args=url_args, kwargs=url_kwargs))
    assert response.status_code == 200
