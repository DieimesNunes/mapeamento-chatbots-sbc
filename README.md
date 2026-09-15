# Chatbots Mapping in SBC OpenLib

This repository contains supporting material for research on chatbots, Artificial Intelligence, and programming education, developed in the context of a master's degree project.

## Objective

This repository gathers data, scripts, and documentation used during the investigation of chatbots and educational tools related to programming education in publications available through SBC OpenLib.

The search strategy and research scope are still being defined and refined.

## Data Collection Tool

Bibliographic records were collected from SBC OpenLib using [pySol](https://gitlab.com/nszchagas/pySol), a third-party tool designed to automate searches and bibliographic data retrieval from SBC OpenLib.

The original pySol source code is not part of this repository.

During the execution of the searches, local adaptations were required to address UTF-8 character encoding issues and HTTP request timeouts.

These modifications are preserved as a patch at:

`patches/pysol_request.patch`

A copy of the original pySol MIT License is available at:

`licenses/pySol-LICENSE.txt`

## Exploratory Search

An exploratory search was performed on September 15, 2026, using SBC OpenLib.

Search parameters:

- Search term: `chatbot`
- Search field: `query`
- Publication type: `anais` (conference proceedings)
- Search tool: pySol

Command used:

```powershell
python pySol --query_string "chatbot" --field query --publication_type anais --bib_dest chatbot_anais.bib