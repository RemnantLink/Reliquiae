#!/usr/bin/env python3
# Copyright (c) 2020 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Test error messages for 'getaddressinfo' and 'validateaddress' RPC commands."""

from test_framework.test_framework import BitcoinTestFramework

from test_framework.util import (
    assert_equal,
    assert_raises_rpc_error,
)

BECH32_VALID = 'ert1qtmp74ayg7p24uslctssvjm06q5phz4yr7gdkdv'
BECH32_INVALID_BECH32 = 'ert1p0xlxvlhemja6c4dqv22uapctqupfhlxm9h8z3k2e72q4k9hcz7vqugsf3u'
BECH32_INVALID_BECH32M = 'ert1qw508d6qejxtdg4y5r3zarvary0c5xw7kfqwaud'
BECH32_INVALID_VERSION = 'ert130xlxvlhemja6c4dqv22uapctqupfhlxm9h8z3k2e72q4k9hcz7vq4q68pj'
BECH32_INVALID_SIZE = 'ert1s0xlxvlhemja6c4dqv22uapctqupfhlxm9h8z3k2e72q4k9hcz7v8n0nx0muaewav25pltc58'
BECH32_INVALID_V0_SIZE = 'ert1qw508d6qejxtdg4y5r3zarvary0c5xw7kqq2287l0'
BECH32_INVALID_PREFIX = 'bc1pw508d6qejxtdg4y5r3zarvary0c5xw7kw508d6qejxtdg4y5r3zarvary0c5xw7k7grplx'

BASE58_VALID = '2dcjQH4DQC3pMcSQkMkSQyPPEr7rZ6Ga4GR'
BASE58_INVALID_PREFIX = '17VZNX1SN5NtKa8UQFxwQbFeFc3iqRYhem'

INVALID_ADDRESS = 'asfah14i8fajz0123f'

# ELEMENTS
BLECH32_VALID = 'el1qq0umk3pez693jrrlxz9ndlkuwne93gdu9g83mhhzuyf46e3mdzfpva0w48gqgzgrklncnm0k5zeyw8my2ypfsmxh4xcjh2rse'
BLECH32_INVALID_BLECH32 = 'el1pq0umk3pez693jrrlxz9ndlkuwne93gdu9g83mhhzuyf46e3mdzfpva0w48gqgzgrklncnm0k5zeyw8my2ypfsxguu9nrdg2pc'
BLECH32_INVALID_BLECH32M = 'el1qq0umk3pez693jrrlxz9ndlkuwne93gdu9g83mhhzuyf46e3mdzfpva0w48gqgzgrklncnm0k5zeyw8my2ypfsnnmzrstzt7de'
BLECH32_INVALID_VERSION = 'ert130xlxvlhemja6c4dqv22uapctqupfhlxm9h8z3k2e72q4k9hcz7vq4q68pj'
BLECH32_INVALID_SIZE = 'el1pq0umk3pez693jrrlxz9ndlkuwne93gdu9g83mhhzuyf46e3mdzfpva0w48gqgzgrklncnm0k5zeyw8my2ypfsqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpe9jfn0gypaj'
BLECH32_INVALID_V0_SIZE = 'ert1qw508d6qejxtdg4y5r3zarvary0c5xw7kqq2287l0'
BLECH32_INVALID_PREFIX = 'lq1qq0umk3pez693jrrlxz9ndlkuwne93gdu9g83mhhzuyf46e3mdzfpva0w48gqgzgrklncnm0k5zeyw8my2ypfscmm3q74jvv3r'


class InvalidAddressErrorMessageTest(BitcoinTestFramework):
    def set_test_params(self):
        self.setup_clean_chain = True
        self.num_nodes = 1

    def skip_test_if_missing_module(self):
        self.skip_if_no_wallet()

    def test_validateaddress(self):
        node = self.nodes[0]

        # Bech32
        info = node.validateaddress(BECH32_INVALID_SIZE)
        assert not info['isvalid']
        assert_equal(info['error'], 'Invalid Bech32 address data size')

        info = node.validateaddress(BECH32_INVALID_PREFIX)
        assert not info['isvalid']
        assert_equal(info['error'], 'Invalid prefix for Bech32 address')

        info = node.validateaddress(BECH32_INVALID_BECH32)
        assert not info['isvalid']
        assert_equal(info['error'], 'Version 1+ witness address must use Bech32m checksum')

        info = node.validateaddress(BECH32_INVALID_BECH32M)
        assert not info['isvalid']
        assert_equal(info['error'], 'Version 0 witness address must use Bech32 checksum')

        info = node.validateaddress(BECH32_INVALID_V0_SIZE)
        assert not info['isvalid']
        assert_equal(info['error'], 'Invalid Bech32 v0 address data size')

        info = node.validateaddress(BECH32_VALID)
        assert info['isvalid']
        assert 'error' not in info

        # Base58
        info = node.validateaddress(BASE58_INVALID_PREFIX)
        assert not info['isvalid']
        assert_equal(info['error'], 'Invalid prefix for Base58-encoded address')

        info = node.validateaddress(BASE58_VALID)
        assert info['isvalid']
        assert 'error' not in info

        # Invalid address format
        info = node.validateaddress(INVALID_ADDRESS)
        assert not info['isvalid']
        assert_equal(info['error'], 'Invalid address format')

        # ELEMENTS
        info = node.validateaddress(BLECH32_INVALID_SIZE)
        assert not info['isvalid']
        assert_equal(info['error'], 'Invalid Blech32 address data size')

        info = node.validateaddress(BLECH32_INVALID_PREFIX)
        assert not info['isvalid']
        assert_equal(info['error'], 'Invalid prefix for Blech32 address')

        info = node.validateaddress(BLECH32_INVALID_BLECH32)
        assert not info['isvalid']
        assert_equal(info['error'], 'Version 1+ witness address must use Blech32m checksum')

        info = node.validateaddress(BLECH32_INVALID_BLECH32M)
        assert not info['isvalid']
        assert_equal(info['error'], 'Version 0 witness address must use Blech32 checksum')

        info = node.validateaddress(BLECH32_VALID)
        assert info['isvalid']
        assert 'error' not in info

    def test_getaddressinfo(self):
        node = self.nodes[0]

        assert_raises_rpc_error(-5, "Invalid Bech32 address data size", node.getaddressinfo, BECH32_INVALID_SIZE)

        assert_raises_rpc_error(-5, "Invalid prefix for Bech32 address", node.getaddressinfo, BECH32_INVALID_PREFIX)

        assert_raises_rpc_error(-5, "Invalid prefix for Base58-encoded address", node.getaddressinfo, BASE58_INVALID_PREFIX)

        assert_raises_rpc_error(-5, "Invalid address format", node.getaddressinfo, INVALID_ADDRESS)

        # ELEMENTS
        assert_raises_rpc_error(-5, "Invalid Blech32 address data size", node.getaddressinfo, BLECH32_INVALID_SIZE)

        assert_raises_rpc_error(-5, "Invalid prefix for Blech32 address", node.getaddressinfo, BLECH32_INVALID_PREFIX)

    def run_test(self):
        self.test_validateaddress()
        self.test_getaddressinfo()


if __name__ == '__main__':
    InvalidAddressErrorMessageTest().main()
