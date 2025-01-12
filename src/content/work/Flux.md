---
title: My Homelab
publishDate: 2025-01-01 00:00:00
img: /assets/flux-icon.webp
img_alt: The flux logo
description: |
  How did we get here and what is it I am running
tags:
  - FluxCD
  - Kubernetes
  - GitOps
  - GitLab
  - CI/CD
  - K3s
  - Traefik
---

## Introduction
Over the last few years I have hosted a plethora of services from Minecraft (MC) servers to recipe hosting with [Mealie](https://mealie.io/). With the set of frequent complains about the MC server going down when I went to bed it set me on the path of starting my own server.   
My first box was just a Raspberry Pi 3 hooked up to our router. This taught me networking and what it meant to host "something" for myself and my friends. It was shortly after that in which the complaints turned from availability to performance and I knew even if it were only for me that I wanted something more.

## Platform
Ever since I really started getting into hosting my own servers, I use [Unraid](https://unraid.net/). It was highly recommended at the time and I was building my homelab/nas so I wanted the best available on the market but still make for consumers. At the beginning I was able to just spin up a VM running Ubuntu 16.04 headless and the one single app that I wanted running. This worked. Until it didn't.

## Growth
Fast forward a few months and I was on a tirade of hosting. 3 MC servers, 2 terraria servers, and some other random junk and I found out very quickly why people get paid for this. After looking through some of the screens in Unraid thinking to myself "this has to be easier somehow." I stumbled upon Unraid apps. I found the MC servers I wanted to host in there and looked at the publisher and sent it. I tested it and the docker containers associated spun to life and I was amazed. So much of the pain and suffering I went through to keep OSs up to date and make sure packages were installed and etc. It was all just taken care of. And that worked for a good while. Until I got bored.

## Experimentation
While my setup worked, the amount of MC and terraria my friends were playing dwindled and thus uprose my want to learn something new. I had liked the fact that each of these containers had direct access to shares on my NAS and that was a feature for me for a while until one of my friends decided to get a little malicious and ballooned the size of the world file for the sole reason of because he could. This caused me to realize two fatal flaws.   
1. I did not put a cap on the storage space of that share where the MC files were being written
2. My friend was kind of a jerk
So to combat this I tried to put a cap on the share but quickly found the Unraid UI lacking in a max share size option. So back to VMs I go. Armed with my previous knowledge of what went wrong with a bunch of VMs I set out on trying to now dockerize all of my services. With it I learned nginx and how to manually configure a reverse proxy how to do port forwarding and generally cleaned up my unraid box by moving it to a vm where it lived happily for about 2 years. Until I felt like writing nginx config files was annoying.

## DNS and Why It Made Me Switch to K8s
Anyone who has spent a decent amount of time writing nginx config files will tell you its quite annoying. Poor intellisense and hard to find and read docs were some of the issues I ran into. Whats more is that at this point I had started to work in AWS and I had seen what you can really do with Route 53 and knew that my homelab hosting should not be this hard, or rather annoying to deal with. I wanted something dynamic and flexible so that I can deploy what I want, when I want, and not have to remember to place a specifically formatted file in a very specific spot on my server. I had seen K8s in the wild its not like it was new technology at this point but I really had not experimented with what it was why it was until I came across a Youtube video (sorry can't link don't remember exactly which one) that was touting the DevX of deploying to EKS over ECS and or EC2. It was at that point that I knew it was a blind spot for me and I needed to at least know what it was capable of.  
So I got to work. At this point I had a small portfolio site and some other Single Page Applications (SPA) that I wanted to port over as they were already dockerized and had 0 dependencies. After much trial and error and many many more Youtube videos, shout out [TechWorld With Nana](https://youtu.be/X48VuDVv0do) for the full K8s tutorial. I set my heart on K3s for its simple single combined control plane and operator setup. I then wanted to try something new and a coworker had recommended [Traefik](https://traefik.io/) so I figured why not. With Traefik as my ingress controller I have been able to move each route to its own file and keep it organized and add new routes super easy. Since I rolled this out, I have never looked back. Between easy auto scaling or just writing an Ingress to route traffic to a new hosted site, I am hooked. 

## So Whats in the Works
- Longhorn: I have been recently experimenting with Longhorn for being able to provide better storage for my nodes and including backups rather than just relying on my stateful services to just live on one box forever with parodic updates. 
- FluxCD: After playing around with longhorn I found that my namespaces were becoming cluttered and it was hard to discern and create a reproducible state should I ever lose my node. This lack of redundancy has made me rethink how my K3s cluster is deployed but more over how I manage the applications inside. So I looked around and found [fluxcd](https://fluxcd.io/) and started deploying it. It allows GitOps for your projects and most importantly for me a reproducible state for your cluster so that in the event that I want to recreate my cluster, I can do it easily. 

## Conclusion
My journey has been long with many tools and projects that have been in the works but at this point I am satisfied with how things are. New apps are simple, stateful apps have backups, and DNS and its associated TLS certs are easy to manage and modify. Did I miss some easy wins 1000% but did I learn some things the hard way to really appreciate the ease of use also 1000%. 


Lastly, I wont be keeping this page up to date so please see the [work section](https://jacobbanghart.com/work/) of this site for more projects. 