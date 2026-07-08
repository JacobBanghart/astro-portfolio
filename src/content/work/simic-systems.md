---
title: Simic Systems
publishDate: 2026-07-08 00:00:00
img: /assets/simic-home.png
img_alt: The Simic Systems homepage showing the product grid of sealed Magic The Gathering booster displays
description: |
  Building a real e-commerce storefront for selling sealed Magic cards, from Stripe checkout to Cloudflare Workers
tags:
  - Astro
  - React
  - Cloudflare Workers
  - Stripe
  - TypeScript
  - Material UI
  - E-Commerce
---

## Why I Built This

I've been collecting and playing Magic: The Gathering for a long time, and I started buying and reselling sealed product on the side. The trading card market is a mess to sell into. Marketplaces bury you in fees, listings are full of mystery-condition items, and prices swing depending on which platform you're looking at. I wanted a storefront that was just mine: straightforward pricing, only factory-sealed product, and a checkout flow I actually trust.

That's [Simic Systems](https://simic.systems/): a storefront for sealed Magic: The Gathering, and now Avatar: The Last Airbender and Marvel Universe, booster boxes, bundles, and Commander decks.

## What It Does

It's a small, focused catalog store. You land on the homepage, browse a grid of sealed products with live pricing and stock counts, search or sort, and check out through Stripe.

![Simic Systems homepage with product grid](/assets/simic-home.png)

Click into a product and you get a full detail page: description, price, live availability, and an add-to-cart button. These pages are server-rendered and indexable, which matters for a small store trying to show up in search at all.

![Simic Systems product detail page for a Lorwyn Eclipsed Collector Booster Display](/assets/simic-product.png)

Cart state lives in a React context that persists across the site. Checkout is a real Stripe Checkout session, so I never touch card data. There's a contact form with rate limiting and a honeypot field to keep the spam bots out.

![Simic Systems about page describing the store and what it carries](/assets/simic-about.png)

## The Stack

The [repo](https://github.com/JacobBanghart/simic-systems-home) is Astro 5 running in SSR mode, deployed to Cloudflare Workers instead of a traditional Node host. A few pieces I'm particularly happy with:

Most of the site is static-first Astro, with React only where there's real interactivity: the product grid, the cart drawer, the contact form. No client-side JS ships for pages that don't need it. I didn't want to hand-roll a component library for a one-person storefront either, so Material UI handles the UI primitives with a custom dark theme layered on top.

Products, prices, and Checkout sessions all live in Stripe. I don't store payment info anywhere in my own infrastructure. Product data is expensive to pull straight from Stripe on every request, so it's cached in a Cloudflare KV namespace and invalidated by a Stripe webhook whenever something changes. Stock and pricing stay fresh within about a minute of a real update, without hammering the Stripe API.

The whole thing, SSR routes, API endpoints, and static assets, runs on Cloudflare Workers instead of a VM or container. It's a different mental model than the Kubernetes-based hosting I use for [my homelab](/work/homelab/), and it's been a nice change of pace: no cluster to babysit, just deploy and go.

Products are defined in a `catalog/products.mjs` file in the repo rather than clicked together in the Stripe dashboard. I can diff catalog changes before they go live and sync them with a script. "Update three prices" went from a manual dashboard chore to a reviewable code change.

## What I'd Call Out

A few decisions felt worth making deliberately instead of defaulting into. There are no user accounts: with a catalog this size, auth and password resets and an order history UI add real complexity for very little benefit, and orders tracked through Stripe plus shipping confirmations have been enough. There's no product quick-view modal either. It's tempting to add a slick modal so people never leave the grid, but real product detail pages are indexable and support proper metadata, which matters more for a store trying to actually get found.

I keep a `DEFERRED.md` file in the repo where I write down features I considered and talked myself out of, along with why. It's kept scope honest. Orders over $250 require a signature on delivery, since sealed product is genuinely valuable and a lost package on a high-dollar order is a bad day. That's a small tradeoff in delivery friction for a lot less risk.

## Where It's Headed

The catalog is intentionally small right now: current and recent Magic sets plus a couple of crossover products. As it grows, some of the deferred ideas will start to make more sense, things like recently-viewed products or back-in-stock notifications. For now, the goal was a store that's fast, honest about what's in stock, and doesn't get in its own way. If you play Magic and want sealed product from someone who actually shuffles a deck, take a look at [simic.systems](https://simic.systems/).
