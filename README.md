Reliquiae blockchain platform
====================================

https://www.reliquiae.org/

This is the integration and staging tree for the Reliquiae blockchain platform,
a collection of feature experiments and extensions to the Bitcoin protocol.
This platform enables anyone to build their own businesses or networks
pegged to Bitcoin as a sidechain or run as a standalone blockchain with arbitrary asset tokens.

Modes
-----

Reliquiae supports a few different pre-set chains for syncing. Note though some are intended for QA and debugging only:

* Liquid mode: `reliquiaed -chain=reliquiae` (syncs with Reliquiae network)
* Bitcoin mainnet mode: `reliquiaed -chain=main` (not intended to be run for commerce)
* Bitcoin testnet mode: `reliquiaed -chain=testnet3`
* Bitcoin regtest mode: `reliquiaed -chain=regtest`
* Reliquiae custom chains: Any other `-chain=` argument. It has regtest-like default parameters that can be over-ridden by the user by a rich set of start-up options.

Confidential Assets
----------------
The latest feature in the Reliquiae blockchain platform is Confidential Assets,
the ability to issue multiple assets on a blockchain where asset identifiers
and amounts are blinded yet auditable through the use of applied cryptography.

 Features of the Reliquiae blockchain platform
----------------

Compared to Bitcoin itself, it adds the following features:
 * [Confidential Assets][asset-issuance]
 * [Confidential Transactions][confidential-transactions]
 * [Federated Two-Way Peg][federated-peg]
 * [Signed Blocks][signed-blocks]
 * [Additional opcodes][opcodes]

Previous elements that have been integrated into Bitcoin:
 * Segregated Witness
 * Relative Lock Time


Additional RPC commands and parameters:
* [RPC Docs](https://www.reliquiae.org/en/doc/)

License
-------
Reliquiae is released under the terms of the MIT license. See [COPYING](COPYING) for more
information or see http://opensource.org/licenses/MIT.

[confidential-transactions]: https://www.reliquiae.org/features/confidential-transactions
[opcodes]: https://www.reliquiae.org/features/opcodes
[federated-peg]: https://www.reliquiae.org/features#federatedpeg
[signed-blocks]: https://www.reliquiae.org/features#signedblocks
[asset-issuance]: https://www.reliquiae.org/features/issued-assets
[schnorr-signatures]: https://www.reliquiae.org/features/schnorr-signatures

What is the Reliquiae Project?
-----------------
Reliquiae is an open source, sidechain-capable blockchain platform. It also allows experiments to more rapidly bring technical innovation to the Bitcoin ecosystem.

Learn more on the [Reliquiae website](https://reliquiae.org)


