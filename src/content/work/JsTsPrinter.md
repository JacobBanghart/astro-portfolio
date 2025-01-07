---
title: TS/JS webpage printer
publishDate: 2024-12-30 00:00:00
img: /assets/print.webp
img_alt: An image of the google chrome print to pdf dialog
description: |
  When complicated problems meets the intersection of low time and budget you have to get creative
tags:
  - Open Source
  - Docker
  - Node
  - Vanilla JS
  - Typescript
  - Puppeteer
---

## Projects
- https://gitlab.com/jacobmbanghart/jsprinter
- https://gitlab.com/jacobmbanghart/tsprinter

## Printing to pdf
Printing a webpage to a pdf is generally a solved problem 
- https://github.com/dompdf/dompdf
- https://weblog.west-wind.com/posts/2024/Mar/26/Html-to-PDF-Generation-using-the-WebView2-Control  

But some of these solutions didn't exist when I made this and didn't have the additional limitation of having a runtime that was essentially locked down to php 5.4.   
### So why did I even need this?
Back in my first job we ran a LAMP stack (Linux, Apache, Mysql, and PHP). This type of stack was fairly common throughout the 2010s and still powers a majority of the web. But one of the things, especially in the days before PHP 8.0, that was notoriously hard was the ability to multiprocess/multithread PHP. The more specific issue was not that it was impossible or hard it was that people just wrote bad code that made parallel execution hard. One of these things was HTML to PDF conversion. 
### HTML to PDF
If you are tasked with this today I highly recommend looking at the above alternatives to what I show you but still getting a little creative can be fun!  
The short problem description is that if more than a small handful of users generated a PDF invoices at once it would slow our poor server to a crawl affecting more than just the users who were generating PDFs. At worst your users should experience that the ones generating the PDFs should be slowed down and to that end its generally a user expectation. That wasn't good enough for me. I wanted to make it so that even the people who were downloading invoices on our platform would have a good experience no matter what they were doing. 
## Externalization
From a very high level it is known that if you have a long running process you should try to externalize it and tell the client where to pick it up when the conversion is complete. So I got to work. I always had wondered about how chrome was able to do it so fast and if I could replicate that. I found 3 different frameworks to attempt this: selenium, cypress, puppeteer. Selenium seemed like the clear choice as it has been an industry standard for automating web interactions. Cypress and puppeteer on the other hand were the new kids on the block. So I wanted to give them a fair shake so I chose one at random and ran with it!
## Results
The project was shelved for a number of reasons from maintenance budget, security, and general inexperience of the staff in hosting and securing node services. In addition higher priority work came down the line which made us shelve the bug anyways. As far as I am aware even several years after having left the company I would wagger good money the problem still exists.