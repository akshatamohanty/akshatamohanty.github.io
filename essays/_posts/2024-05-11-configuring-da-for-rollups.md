---
title: Should the data availability layer for blockchains be configurable?
description:
date: 2024-05-11
published: false
---

The argument for mass adoption of blockchains is often impeded by the concerns around scalability. The blockchain trilemma states a mandatory trade-off between security, scalability and decentralization for any blockchain.

However, more recently, modular blockchains have evolved to offer an alternative option to this trade-off. The core functions for a distributed ledger can be divided into the following:

- execution, i.e the ordering and execution of the transactions to reach new states
- settlement, i.e when a miner includes a transaction into a block, ensuring transaction immutability
- consensus, i.e the process by which all nodes establishes a shared agreement on the validity of transactions and the chain state,
- data availability, i.e refers to the confidence a user can have that the data required to verify a block is really available to all network participants.
  Modular blockchains propose to split the core layers, with separate components being responsible for their own function, thereby allowing parallel processing and higher throughput without compromising decentralization and security.

Layer 2 roll ups have quickly gained popularity in accordance with the modular design, i.e solutions where the execution layer is offloaded to its own network. The general mechanism of a rollup is to introduce a separate network or layer of nodes, which receives transactions and acts as a proxy between the main chain and clients. This layer then batches the transactions into groups and anchors them to Layer 1, thereby achieving settlement and consensus. To ensure data availability, i.e, the guarantee that the data of the rolled-up transactions, rollups execute transactions outside of Ethereum, but post transaction data to Mainnet as calldata or in blobs.

However, furthering this idea of modular blockchains, there have been multiple solutions to offer off-chain data availability layers also. Solutions like EigenDA, Celestia and Avail allow the transaction data to be posted off-chain.

In this ecosystem, the dApp developer now has the following choices:

- Use a monolithic blockchain.
- Create your own app-chain or deploy your own rollup, using a rollup-as-a-service
- Use a rollup, where
  the rollup chooses their mechanism for data availability
  where the rollup offers an option to choose the data availability layer

The first two options are the most straightforward for the developer. The developer may either choose to go with an existing monolith blockchain, or decide to build their own separate ecosystem, picking each layer of their blockchain stack as per their choice.

However, the option where a developer chooses to build atop an existing rollup is where there could potentially be two options.

**Use a rollup, and the rollup chooses the data availability layer.**
From our understanding, this is the current mode of operation. The smart contract developer building on a general-purpose L2 has the exact same experience as a smart contract developer building on a monolithic chain. The data availability concern is abstracted away from the dApp developer and a roll up natively decides to integrate with a data availability solution it assesses best. Given that data availability is practically pertinent to only L2 validator nodes and challengers, the responsibility of ensuring the availability, security and consistency of the DA layer remains the responsibility of the roll up.

However, there are concerns which could be highlighted here. In the previous setup, where rollups committed data to the underlying layer, data availability was a guarantee that required no additional thought and derived its guarantees from the underlying layer. Given that a developer chose a rollup based on an L1 they chose, the developer subtly attested the DA layer also. However, this solution now implies that the developer need not be mindful of the guarantees offered by the data availability solution chosen by the rollup but treat a layer-2 solution as layer-1 equivalent.

It should be highlighted that even though these might seem to be protocol-level problems, they don't mean that dApp developers are unaffected by them. In terms of tactical concerns, a dApp developer may be deeply affected and thereby concerned about collusion across the execution and DA layers, the scalability of the rollup stack, potential backups, downtimes and migration concerns in case the DA fails.

Developers who understand these nuances, might be able to make informed decisions but might also be restricted by this architecture.

**Use a rollup, and the developer chooses the data availability layer.**
This scenario is an alternative that might be considered, wherein, the rollup offers a choice to the developer herself as to which data availability solution to use. This might be by way of a directive or a config in the smart contract.

Obviously, this complicates the development processes for the rollup itself, which might now need to integrate with multiple DA layers, orchestrate dispersal and retrieval of transactions and synchronize data across them. However, it also preserves the isolation in the key function of a rollup i.e to only scale transaction processes and throughout, without making guarantees on data availability itself.

An argument could be made that a developer could choose to build their own stack to allow for the stated granularity and control. However, this could potentially deprive the developer of the user base that has already been established with an existing on a L2 rollup, the potential for collaboration across existing protocols and modular development.

Another argument, favoring this approach is that even though the most popular use-case currently for the data availability layer is guaranteeing the existence of rolled-up transactions, there might be a time in the future, where other data is off-loaded to data availability layers, as a data store, by the smart contract developer. Hence, having a roll-up use the choice of the data availability layer as configured by the developer would ensure that all related data is available at the same source.
