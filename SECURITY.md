# Security and privacy notes

This project runs an AI agent unattended every night. That deserves a few minutes of thought before you switch it on.

## The main risk: reading the web while holding access to your accounts

The agent reads news pages to find a seed for the story. A web page can contain text written to look like instructions. If the same agent can also reach your files, email or calendar, a malicious page could try to steer it into reading or sharing them.

The design here keeps that risk small:

- **Delivery is in-app only.** The story and the MP3 are returned in the agent's own session. Nothing is written to cloud storage, email or any other account.
- **The prompt forbids connected apps.** It names the tools the run may use and tells the agent to ignore instructions found in web pages.
- **This is an instruction, not a technical lock.** If your agent platform attaches connectors to scheduled runs automatically, the safest setup is one where those connectors are not attached to this task at all. Check what your task has access to after you create it.

## Downloaded code and models

- Speech packages are pinned to exact versions.
- The voice model is downloaded from a public GitHub release and verified against a recorded SHA-256 checksum. If the checksum does not match, setup stops.
- Everything runs in the agent's sandbox, not on your own computer.
- Pinning protects you from a file changing later. It does not vouch for the upstream project. Review it yourself if that matters to you.

## Content

The prompt rules out real named people, real deaths and real disasters as plot, and anything about the listener, their family or their employer. Stories are fiction seeded by one small real detail, and each one ends with a line stating what was real.

Treat the stories as private listening. If you share one, read it first.

## Failure behaviour

If a step fails, the agent sends one short notice and stops. It does not retry repeatedly or look for another route.

## Cost

Each run searches the web, writes about a thousand words and renders several minutes of audio. Try it for a week and check your usage before leaving it on.

## Before you enable it

- [ ] The task has no access to storage, email or calendar, or you accept that risk.
- [ ] It runs under a personal account, not a work account.
- [ ] You have read the prompt and changed the genres and rules to suit you.
- [ ] You know how to pause or delete the task.
