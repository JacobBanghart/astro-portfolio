---
title: NIJII Map
publishDate: 2024-12-31 00:00:00
img: /assets/nijii.webp
img_alt: An image of the NIJII tribes map
description: |
  A super quick low budget high impact OpenStreetMaps
tags:
  - Open Source
  - GitHub Pages
  - Static Site Generation
  - Vanilla JS
  - Vite
  - NIJII
  - Open Layers
  - Open Street Maps
  - Headless Wix
---
## Contracting work for National Indigenous Justice Information Inclusion (NIJII)
NIJII contacted me about doing some minor contracting work for them. They wanted a map that put pins on the locations of the groups affiliated with the NIJII. Their current solution was a Wix site that while it had a map they did not like it for the purpose as it had some rigid stylistic choices that made it difficult to work with.  
After talking about the things we didn't like we settled on this custom solution but with a focus on maintainability even after the contract is complete. An integration with the existing wix system for ease of updating then became paramount.  
## Tech
Given the above requirements we decided to skip google maps as it would be a reoccurring cost after a limited number of free views. Instead we started using [OpenStreetMaps](https://www.openstreetmap.org/) tiling and using [OpenLayers](https://openlayers.org/) for displaying and plotting the icons on the map. From there it was a matter of exposing a Wix Dataset from and endpoint to fetch the data into. This gives the flexibility of management of data being controlled from Wix and allowing little to no changes to the map itself after the initial deployment.

### Vanilla JS vs React/Other
One of the notable aspects of this project is that it is using Vite and vanilla Javascript which seems like a strange combo in our modern day of React, Vue, Svelt, and other ui frameworks/libraries. The choice here was made to keep this very light weight to avoid additional rendering overhead to keep it fast and clean. This project also gains the benefit of no TypeScript overhead so no additional transpilation during final build. 