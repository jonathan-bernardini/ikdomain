import logging
import re
import whois
from whois import TLD_RE
from whois._3_adjust import DATE_FORMATS

import tld_regexpr_extended

DATE_FORMATS.append('%d/%m/%Y %H:%M:%S')
logging.debug(DATE_FORMATS)


def get_tld_re_extended(tld):
    if tld in TLD_RE:
        return TLD_RE[tld]
    v = getattr(tld_regexpr_extended, tld)
    extend = v.get('extend')

    if extend:
        e = get_tld_re_extended(extend)
        tmp = e.copy()
        tmp.update(v)
    else:
        tmp = v

    if 'extend' in tmp:
        del tmp['extend']

    TLD_RE[tld] = dict((k, re.compile(v, re.IGNORECASE) if isinstance(v, str) else v) for k, v in tmp.items())
    return TLD_RE[tld]


[get_tld_re_extended(tld) for tld in dir(tld_regexpr_extended) if tld[0] != '_']

logging.debug(TLD_RE.keys())
