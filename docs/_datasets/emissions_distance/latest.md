---
name: emissions_distance
title: Local authority emissions distance
description: "This comparison set shows councils who have a similar emissions profile\
  \ to each other. \nThe goal is to try and draw comparisons between similar emissions\
  \ in similar circumstances. The five different categories in the BEIS dataset are\
  \ adjusted in different ways, and then councils are positioned on how different\
  \ they are to each other. \n"
version: latest
licenses:
- name: CC-BY-4.0
  path: https://creativecommons.org/licenses/by/4.0/
  title: Creative Commons Attribution 4.0 International License
contributors:
- title: mySociety
  path: https://mysociety.org
  role: author
custom:
  build: local_authority_similarity.__main__:build_emissions
  tests:
  - test_emissions_distance
  dataset_order: 0
  download_options:
    gate: default
    survey: default
    header_text: default
  composite:
    xlsx:
      include: all
      exclude: none
      render: true
    sqlite:
      include: all
      exclude: none
      render: true
    json:
      include: all
      exclude: none
      render: true
  change_log:
    0.1.0: Initial load of data
    0.1.1: "description changed from 'Rankings, match-scores and labels for local\
      \ authorities based on BEIS 2020 emissions data\n' to 'This comparison set shows\
      \ councils who have a similar emissions profile to each other. \nThe goal is\
      \ to try and draw comparisons between similar emissions in similar circumstances.\
      \ The five different categories in the BEIS dataset are adjusted in different\
      \ ways, and then councils are positioned on how different they are to each other.\
      \ \n'"
    1.0.0: lock data schema
    1.1.0-futurecouncils: ''
    1.1.0: release 2023 data
    1.2.0: 'Change in data for resource(s): distance_map,la_labels'
  datasette:
    about: Info & Downloads
    about_url: https://pages.mysociety.org/local_authority_similarity/datasets/emissions_distance/1_2_0
  formats:
    csv: true
    parquet: true
resources:
- title: Local Authority Emissions Similarity
  description: "Dataset of distance calculations based on BEIS Emissions data.\nThis\
    \ distance is based on:\n* Winsorized population density\n* Public Sector emissions\
    \ per person (winsorised)\n* Transport Emissions per person (winsorised)\n* Domestic\
    \ emissions per person\n* Industrial emissions per unit of GDP\n* Commerical emissions\
    \ per unit of GDP\n* Agriculture emissions per unit of GDP\n"
  custom:
    row_count: 154842
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/local_authority_similarity/datasets/emissions_distance/1_2_0#distance_map
  path: distance_map.csv
  name: distance_map
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: local-authority-code_A
      type: string
      description: A three/four letter code for the local authority
      constraints:
        unique: false
      example: ABC
    - name: local-authority-code_B
      type: string
      description: A three/four letter code for the local authority
      constraints:
        unique: false
      example: ABC
    - name: distance
      type: number
      description: The distance between the two local authorities (not meaningful
        except for comparisons)
      constraints:
        unique: false
      example: 0.2663379651760705
    - name: match
      type: number
      description: A score between 0 and 100 indicting how similar a council is (based
        on all known distances for a council)
      constraints:
        unique: false
      example: 0.0
    - name: position
      type: number
      description: The rank of how much local authority B is similar to local authority
        A (1 is most similar).
      constraints:
        unique: false
      example: 1.0
  hash: 47361a4b9168248f5222738f004b7197
- title: Local authority emissions profile labels
  description: A short category based on emissions profile for each local authority
  custom:
    row_count: 395
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/local_authority_similarity/datasets/emissions_distance/1_2_0#la_labels
  path: la_labels.csv
  name: la_labels
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: local-authority-code
      type: string
      description: 3/4 letter local authority code.
      constraints:
        unique: true
      example: ABC
    - name: label
      type: string
      description: Label to describe emissions profile of authority.
      constraints:
        unique: false
        enum:
        - Agriculture
        - City of London
        - Industry/Commerical/Domestic
        - Public sector
        - Transport/Domestic
        - Urban Mainstream
      example: Agriculture
  hash: a65f860231a948495e2fc92e75422025
- title: Local authority emissions labels
  description: Map of short labels to longer descriptions for emissions categories.
  custom:
    row_count: 7
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/local_authority_similarity/datasets/emissions_distance/1_2_0#label_desc
  path: label_desc.csv
  name: label_desc
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: label
      type: string
      description: Short label for emissions profile.
      constraints:
        unique: true
        enum:
        - Agriculture
        - City of London
        - Industry/Commerical/Domestic
        - Public sector
        - Transport/Domestic
        - Urban Mainstream
      example: Agriculture
    - name: desc
      type: string
      description: Longer description of emissions profile.
      constraints:
        unique: true
        enum:
        - Above average agriculture, domestic score
        - Above average for industry/domestic/doemestic, below average public sector
          emissions.
        - Above average transport/domestic score
        - Below average for all emissions scores
        - City of London does not have a comparable emissions profile
        - Well above average public sector (government, education, health), below
          average in other areas.
      example: Above average agriculture, domestic score
  hash: 5c5b45d7a967ca4b2783394d38fe55b2
full_version: 1.2.0
permalink: /datasets/emissions_distance/latest
---
