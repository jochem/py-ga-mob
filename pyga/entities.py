# -*- coding: utf-8 -*-

from datetime import datetime
from utils import get32bitRandom

__author__ = "Arun KR (kra3) <the1.arun@gmail.com>"
__license__ = "Simplified BSD"

class Campaign(object):
    pass


class CustomVariable(object):
    pass


class Event(object):
    pass


class Item(object):
    '''
    Represents an Item in Transaction

    Properties:
    order_id -- Order ID, will be mapped to "utmtid" parameter
    sku -- Product Code. This is the sku code for a given product, will be mapped to "utmipc" parameter
    name -- Product Name, will be mapped to "utmipn" parameter
    variation -- Variations on an item, will be mapped to "utmiva" parameter
    price -- Unit Price. Value is set to numbers only, will be mapped to "utmipr" parameter
    quantity -- Unit Quantity, will be mapped to "utmiqt" parameter

    '''

    def __init__(self):
        self.order_id = ''
        self.sku = ''
        self.name = ''
        self.variation = ''
        self.price = ''
        self.quantity = 1

    def validate(self):
        if not self.sku:
            raise Exception('sku/product is a required parameter')


class Page(object):
    '''
    Contains all parameters needed for tracking a page

    Properties:
    path -- Page request URI, will be mapped to "utmp" parameter
    title -- Page title, will be mapped to "utmdt" parameter
    charset -- Charset encoding, will be mapped to "utmcs" parameter
    referrer -- Referer URL, will be mapped to "utmr" parameter
    load_time -- Page load time in milliseconds, will be encoded into "utme" parameter.

    '''
    REFERRER_INTERNAL = '0'

    def __init__(self, path):
        self.path = ''
        self.title = ''
        self.charset = ''
        self.referrer = ''
        self.load_time = ''

        if path_val:
            self.path= path

    def __setattr__(self, name, value):
        if name == 'path':
            if value and value != '':
                if value[0] != '/':
                    raise Exception('The page path should always start with a slash ("/").')
        elif name == 'load_time':
            if value and not isinstance(value, int):
                raise Exception('Page load time must be specified in integer milliseconds.')

        object.__setattr__(self, name, value)


class Session(object):
    '''
    You should serialize this object and store it in the user session to keep it
    persistent between requests (similar to the "__umtb" cookie of the GA Javascript client).

    Properties:
    session_id -- A unique per-session ID, will be mapped to "utmhid" parameter
    track_count -- The amount of pageviews that were tracked within this session so far,
                   will be part of the "__utmb" cookie parameter.
                   Will get incremented automatically upon each request
    start_time -- Timestamp of the start of this new session, will be part of the "__utmb" cookie parameter

    '''
    def __init__(self):
        self.session_id = get32bitRandom()
        self.track_count = 0
        self.start_time = datetime.now()

    @staticmethod
    def generate_session_id():
        return get32bitRandom()

    def extract_from_utmb(self, utmb):
        '''
        Will extract information for the "trackCount" and "startTime"
        properties from the given "__utmb" cookie value.
        '''
        parts = utmb.split('.')
        if len(parts) != 4:
            raise Exception('The given "__utmb" cookie value is invalid.')

        self.track_count = parts[1]
        self.start_time = datetime.fromtimestamp(parts[3])

        return self


class SocialInteraction(object):
    pass


class Tracker(object):
    pass


class Transaction(object):
    '''
    Represents parameters for a Transaction call

    Properties:
    order_id -- Order ID, will be mapped to "utmtid" parameter
    affiliation -- Affiliation, Will be mapped to "utmtst" parameter
    total -- Total Cost, will be mapped to "utmtto" parameter
    tax -- Tax Cost, will be mapped to "utmttx" parameter
    shipping -- Shipping Cost, values as for unit and price, will be mapped to "utmtsp" parameter
    city -- Billing City, will be mapped to "utmtci" parameter
    state -- Billing Region, will be mapped to "utmtrg" parameter
    country -- Billing Country, will be mapped to "utmtco" parameter
    items -- @entity.Items in a transaction

    '''
    def __init__(self):
        self.order_id = ''
        self.affiliation = ''
        self.total = ''
        self.tax = ''
        self.shipping = ''
        self.city = ''
        self.state = ''
        self.country = ''
        self.items = []

    def __setattr__(self, name, value):
        if name == 'order_id':
            for itm in items:
                itm.order_id = value
        object.__setattr__(self, name, value)

    def validate(self):
        if len(items) == 0:
            raise Exception('Transaction need to consist of at least one item')

    def add_item(self, item):
        ''' item of type entities.Item '''
        item.order_id = self.order_id
        self.items.append(item)


class Visitor(object):
    pass


class Parameters(object):
    pass