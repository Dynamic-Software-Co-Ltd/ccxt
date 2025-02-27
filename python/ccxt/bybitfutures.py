# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
from ccxt import bybit


#TEALSTREET: THIS IS DEPRECATED
class bybitfutures(bybit):

    def describe(self):
        return self.deep_extend(super(bybitfutures, self).describe(), {
            'id': 'bybitfutures',
            'name': 'ByBit Futures',
            'urls': {
                'test': {
                    'ws': 'wss://stream-testnet.bybit.com/realtime',
                },
                'api': {
                    'ws': 'wss://stream.bybit.com/realtime',
                },
            },
            'options': {
                'defaultType': 'futures'
            }
        })
