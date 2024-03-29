---
name: composite_distance
title: Local authority composite distance
description: "This comparison set combines all the other measures into a single list\
  \ of similar councils.\nCouncils may be highly rated because they are very similar\
  \ in one degree, or because they are slightly similar across several.\n"
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
  build: local_authority_similarity.__main__:build_composite
  tests:
  - test_local_authority_similarity
  dataset_order: 1
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
      \ authorities based on a composite of our other measures\n' to 'This comparison\
      \ set combines all the other measures into a single list of similar councils.\n\
      Councils may be highly rated because they are very similar in one degree, or\
      \ because they are slightly similar across several.\n'"
    1.0.0: lock data schema
    1.1.0-futurecouncils: ''
    1.1.0: release 2023 data
    1.2.0: 'Change in data for resource(s): distance_map,la_labels'
  datasette:
    about: Info & Downloads
    about_url: https://pages.mysociety.org/local_authority_similarity/datasets/composite_distance/1_2_0
  formats:
    csv: true
    parquet: true
resources:
- title: Local Authority Composite Similarity
  description: "Dataset of distance calculations based on other measures of distance\
    \ data.\nThis distance is based on:\n* Emissions profile\n* IMD profile\n* Rural-ruban\
    \ profile\n* Physical distance\n"
  custom:
    row_count: 154842
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/local_authority_similarity/datasets/composite_distance/1_2_0#distance_map
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
      example: 0.6017390960095425
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
  hash: d4e3e4faf5be7ba74eade2a06ca2c72c
- title: Local authority composite profile labels
  description: A short category based on composite profile for each local authority
  custom:
    row_count: 395
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/local_authority_similarity/datasets/composite_distance/1_2_0#la_labels
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
      description: Label to describe composite profile of authority.
      constraints:
        unique: false
      example: 'East Midlands; Emissions: Agriculture; 4th IMD quintile; Urban with
        rural areas'
  hash: 5c7f3fabe4c73ad429c9c5b1051988a3
- title: Local authority composite labels
  description: Map of short labels to longer descriptions for composite categories.
  custom:
    row_count: 1441
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/local_authority_similarity/datasets/composite_distance/1_2_0#label_desc
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
      description: Short label for composite profile.
      constraints:
        unique: true
      example: 'East Midlands; Emissions: Agriculture; 1st IMD quintile; Rural'
    - name: desc
      type: string
      description: Longer description of composite profile.
      constraints:
        unique: false
      example: Above average agriculture, domestic score; in least deprived quintile
        (20%); Local authority mostly made up of urban neighbourhoods, but with a
        significant number of rural neighbourhoods
  hash: 27dae1251fbfea28220f3ac942facf13
full_version: 1.2.0
permalink: /datasets/composite_distance/latest
---
