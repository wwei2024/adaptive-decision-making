# Adaptive Decision-Making

Decision-making in non-stationary environments, requiring both behavioral control on short timescales and reinforcement learning over longer timescales.

## Overview

This repository contains code for training recurrent neural network (RNN) agents on an operant bandit task with changing reward probabilities.

The agent is trained using average-reward reinforcement learning. On short timescales, the RNN learns the behavioral structure of the task, including engagement, movement, and port-entry actions. Over longer timescales, it integrates reward history to adapt its choices as reward contingencies change across blocks.

The trained network provides a model for studying how behavioral control, reward learning, and internal state representations can operate simultaneously across different timescales.

## Bandit Task

On each trial, the agent chooses between two alternatives with independently specified reward probabilities. Reward probabilities remain fixed within a block and change without warning between blocks.

The model must therefore use recent reward history to adapt its behavior to the current reward environment.

## Model

The model consists of an LSTM-based actor-critic network trained using an average-reward reinforcement-learning objective.

Analyses include:

- Adaptive choice behavior across changing reward contingencies
- Reward prediction errors (RPEs) and value estimates
- Dependence of RPEs on recent reward rate
- Population dynamics of the recurrent network
- Representations of reward history and choice preference

## Documentation

A detailed description of the bandit task, model, training procedure, and analyses is provided in [`bandit_task.pdf`](bandit_task.pdf).
