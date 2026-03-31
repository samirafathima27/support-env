# AI Customer Support Ticket Triage Environment

## Overview
This project simulates a real-world customer support system where an AI agent processes tickets, classifies issues, assigns priority, and resolves them.

## Environment
The environment includes:
- reset() → starts a new ticket
- step(action) → processes an action
- state() → returns current ticket

## State
Each ticket contains:
- text
- category
- priority
- resolved status

## Actions
0 → Billing  
1 → Technical  
2 → General  
3 → High Priority  
4 → Low Priority  
5 → Resolve  

## Tasks
- Easy → Classification only  
- Medium → Classification + Priority  
- Hard → Full pipeline  

## Reward
- Correct → positive reward  
- Wrong → negative reward  

## Run
python inference.py

## Output
Displays scores for all tasks and final score.
