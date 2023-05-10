#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------

# load libraries
import os
import html2image
from html2image import Html2Image
import cv

# -----------------------------------------------------------------------------

# HTML template for signature
html_str="""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
        <div class="row">
            <div class="logo">
                <!-- company logo -->
                <img src="https://www.fathomdata.dev/media/logo.svg" alt="" width="150" />
            </div>
            <div class="profile">
                <div class="row">
                    <h2>Name Surname</h2>
                </div>
                <div class="row">
                    <h3>Job Title</h3>
                </div>
                <div class="row">
                    <h3><a href="mailto:Email"> Email </a></h3>
                </div>
                <div class="row">
                    <h3><a href="https://www.fathomdata.dev/" class="url">https://www.fathomdata.dev</a></h3>
                </div>      
            </div>
        </div>
    </body>
</html>
"""

# -----------------------------------------------------------------------------

# get user input
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
job_title=input("Enter your job title: ")
email=input("Enter your email: ")

# -----------------------------------------------------------------------------

# insert user input into html template
#result = src.substitute(d)
html_signature = html_str.replace("Name", first_name).replace("Surname", last_name).replace("Job Title", job_title).replace("Email", email)

# -----------------------------------------------------------------------------

# write result to an HTML file
fpResult = open(first_name + ".html", 'w')
fpResult.write(html_signature)
fpResult.close()

# -----------------------------------------------------------------------------

# convert html strings to image
hti = Html2Image()
hti.size = (500, 250)
png = first_name + ".png"
hti.screenshot(html_str = html_signature, css_str = "css/style.css", save_as = png, size = hti.size)

# resize image according to max height and width (for Gmail)
size = cv.GetSize(png)
thumbnail = cv.CreateImage( ( size[0] / 10, size[1] / 10), png.depth, png.nChannels)
cv.Resize(png, thumbnail)