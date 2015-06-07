# Site Map and Main Sections

## Homepage
**Path: ./**

Big search field and the main categories for the repository. Google Search style.


## Repository Page
**Path: ./repository.html**

- Search field
- Top level categories
- Search Results (Tiles/Isotopes)
- Advanced FIlters (Isotopes filters with && functionality)
*Have an autocomplete for the search. Suggesting Titles, Authors*


### Organization Pages
**Path: ./organizations/{{organization_name}}.html**

- Organization page for each ORGANIZATION in the database. 
- This page will show the basic information for that organization, with a specific design template.
- This page will list all the PUBLICATIONS filed under that ORGANIZATION.
- We will have a specific yaml file to list the organizations.


#### Basic Yaml structure

- Organization Name
- Logo URL
- Custom color
- Organization Blurb
- Organization Members/Publishers
- Organization Authors (pulled from the publications)


### Publication Pages
**Path: ./publications/{{publication_name}}.html**

Show all the information for each PUBLICATION.

- Title
- Authors
- Abstract
- Tags
- Action links (Download, Datasets, Github, PDF, etc)


### Category Page | *Release #2*
**Path: ./categories/{{category_name}}.html**

A specific design for each category, with a big title on the top, and its list of PUBLICATIONS.
We will also have the advanced filters panel.


## About
**Path: ./about.html**

Simple static page


## Blog
**Path: ./blog.html**

Probably, will fetch the blogposts from a thumblr website. We will use the tumblr CMS to make things easier for the admins.
3 options for this:

- Do a simple tumblr theme
- Fetch everything from tumblr using RSS or an API, and display the posts in our website.
- Do a small blog engine using firebase.


## Digest
**Path: ./digest.html**

Fecth the post list using JQuery/RSS. Each post links to thegovlab.org website. 





