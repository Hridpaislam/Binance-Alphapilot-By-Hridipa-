# Binance AlphaPilot Architecture

## Overview

Binance AlphaPilot is an AI-agent workflow designed for the Binance
Agent OS Mini Hackathon.

The system separates:

1. Data collection
2. Market research
3. Portfolio risk analysis
4. Strategy generation
5. Human approval
6. Execution

## Workflow

User
↓
Agent OS
↓
Market Data
↓
Research Agent
↓
Risk Engine
↓
Strategy Agent
↓
Human Approval
↓
Action

## Safety

The prototype does not automatically execute trades.

Any consequential action should require explicit user approval.

## Components

### Market Data

Collects Binance market information.

### Research Agent

Transforms raw market information into an explainable summary.

### Risk Engine

Evaluates portfolio concentration.

### Strategy Agent

Creates a market hypothesis without automatically executing it.

### Human Approval

A future Agent OS integration should require user confirmation
before consequential actions.