from django.core.validators import validate_email
import dns.resolver


# pip install dnspython
def validate_email_dns(address):
    """
    Verify that the domain part of the email address has an MX record.
    If not, the email address has a very high chance of being invalid.
    """
    try:
        localpart, domain = address.split('@')
        # Add a dot to the domain-name to make it absolute, independent of
        # /etc/resolv.conf search value.  This also flags email addresses
        # ending with a dot as faulty, which is good.
        domain += "."
        answers = dns.resolver.query(domain, 'MX')
        assert answers, 'Domain has no MX records'
    except:
        # can't raise ValidationError as we have our own here...
        validate_email('xxx')


def validate_email_address(address):
    validate_email(address)  # from django.core, regex based
    validate_email_dns(address)
