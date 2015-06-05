# GovLab SASS Framework

## Assets

### Foundation
This is the framework I use to create the basic layout structure. Almost everything I use is the grid. I am adding the full docs here too, just in case.

[Foundation Grid](http://foundation.zurb.com/docs/components/grid.html)

[Foundation Main Documentation](http://foundation.zurb.com/docs/)

### Fonts
Adobe Creative Cloud Account gives access to TypeKit. Lauren knows about the Adobe Account.
[How to Setup Typekit](http://help.typekit.com/customer/portal/articles/6780-adding-fonts-to-your-site)

### Icons
We are using [FontAwesome](http://fontawesome.io/icons/) for the icons. Here is a list of all the link. 

### Other Assets
We also use JQuery, Isotopes and JQuery.ZRSSFeed


## Framework Styles

### Basics
I use a simplified BEM methodology to write CSS. These rules will apply to almost all the elements. It still requires a lot of clean-up.

Each style is prefixed by like this:
```
.b-card {
  // Some Styles
  .e-title {
    // Some Styles 
  }
}

.b-card.m-people {
  // Some Styles 
}
```

**.b-card** - it’s block level style.
**.e-title** - is an element level style. The style only exists inside a specific block. In this example, the card block.
**.m-people** - is a modifier. This style only exists when paired with another block or element style. 

This is a great way to mitigate conflicting styles. It adds a bit of complexity to the class names, but once you get the concept it is great.

**Blocks are used inside other blocks.** This makes the conflict mitigation less powerful, but works well.

### Code Organization

[SASS has an import feature](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#import), that works similar to Python Import. With that in mind, each partial file contains a few related blocks. 

In styles.css you will see this:
```
// Shared Modules
  @import "base";
  @import "text-blocks";
  @import "colors";
  @import "header";
  @import "off-canvas-menu";
  @import "footer";
  @import "messages";
  @import "layout";
  @import "pop-buttons";
  @import "form";
  @import "list";

// Site specific Styles
  @import "homepage";
  @import "about";
```

- The **shared modules** pulls the standard blocks. 
- The **site specific styles** pulls the the customizations for each page. In most cases, all the specific page styles will be nested inside that page #id, to guarantee a higher specificity.


### Usage
We build the sections using a mix of govlab styles and foundation grid styles.

Most of the Foundation styles are: .row, .column, .large-XX, .medium-XX, .small-XX


### Basic Page Structure

```
{% extends "layout/base.html" %}
{% block content %}
<div id="page-id" class="b-content-page">

{# we start most pages with this block #}
  <div class="b-page-title">
    <div class="row">
      <div class="large-12 column">
        <h2>Page Title</h2>
        <p>Optional Tagline or Paragraph</p>
      </div>
    </div>
{# end of starting block #}
  
{# This is a repeatable block #}
    <section class="row b-content-section">
      <div class="row">
        <div class="large-6 column">
          // content in the left column
        </div>
        <div class="large-6 column">
            // content in the right column
        </div>
      </div>
    </section>
{# end of repeatable block #}

</div> <!-- closing .b-content-page -->
{% endblock %}
```

# Basic Blocks

## List of content items
Example: Academy Courses. Follow the use of classes and the specific HTML elements. 

```
{# list container #}
<section class="b-project-list row b-content-section">
  <ul class="column large-12">
    
{# repeatable block #}
    <li class="b-project-list-item">
      <h3 class="e-project-name"></h3>
      <h4></h4>
      <div class="e-project-description">
        <p></p>
      </div>
    </li>
{# end of repeatable block #}
  </ul>
</section>
```

## Top Nav

```
<header class="b-top-navigation-wrapper">
  <div class="b-top-navigation">
    <div class="row">
      <h1 class="b-logo"><a href="./index.html" class="e-home" title="Home"><img src="static/img/govlab-logo-white.png" alt="Smarter State"><span>Site Name</span></a></h1>
      <nav class="b-main-nav-container">
        <ul class="b-main-nav">
          <span class="e-mainnav-trigger"><i class="fa-bars fa"></i></span>
          <h2>Menu</h2>
          <li><a href=“#”>Simple Menu Item</a></li>
          <li class="e-submenu"><a href="#">Submenu</a>
            <ul>
              <li><a class="e-sub-item" href=“#”>Submenu Item</a></li>
            </ul>
          </li>
          {# This is an example of a grayed out menu item. #}
          <!-- <li><a class="m-disabled" href="#">Library</a></li> -->
        </ul>
      </nav>
    </div>
  </div>
  </header>
```

## Basic Card Template

```
<div class="b-card">
  <div class="b-wrapper">
    <div class="e-card-content">
      <h4></h4>
      <p></p>
    </div>
  </div>
</div>
``` 

## Card + Project Modifier

Card template with Project Modifier. The modifier adds a header with a picture. 
We also switch the h4 by an h3.

```
<article class="b-card m-project m-clinic" data-filter="{% for tag in card.tags %}{{tag}}{% endfor %}">
  <a class="b-go-to" href="project-page.html#{{card.slug}}">
    <div class="b-wrapper">
      {% if card.links.image %}      
      <header class="b-card-header">
        <div class="e-project-pic" style="background-image: url(static/projects/{{card.slug}}/{{card.links.image}})" title=""></div>
      </header>
      {% endif %}
      <div class="e-card-content">
        <h3 title="{{card.title}}">{{card.title}}</h3>
        <p>By: {% for author in card.authors %}<span>{{author.first_name}} {{author.last_name}}, </span>{% endfor %} </p>
      </div>
    </div>
  </a>
</article>
```

## Card + People Modifier

Card Template with People Modifier. In this case we have 2 modifiers, ".m-people" and ".m-govlab-True/False"

".m-people" adds the header with the picture and the person name on top of the image with a subtle gradient background.

".m-govlab-True" - overwrides the color of the top bar to purple. 

```
<article class="b-card m-people m-govlab-{{person.is_govlab}}" data-filter="{{person.tags}}">
  <a href="faculty-members.html#{{person.name.slug}}">
    <div class="b-wrapper">
      <header class="b-card-header">
        <div class="e-person-pic" style="background-image: url(static/img/faculty/{{person.name.slug}}.jpg)" title="{{person.name.first}} {{person.name.last}}"></div>
        <h3 data-category="{{person.name.last}}" title="{{person.name.first}} {{person.name.last}}">{{person.name.first}} {{person.name.last}}</h3>
      </header>
      <section class="e-card-content"> 
        <h4>{{person.job}}</h4>
        <p>{{person.description}}</p>
      </section>
    </div>
  </a>
</article>
```

## Detail Page - Card-like Panel

EX: govlabacademy.org/project-page.html

".b-link-fix" - this is quick hack to make the #id position the viewport correctly in the scroll.
".m-clinic" - modifies the color of the top boder to yellow (template color for clinics)

```
{% for project in projects %}
<div id="{{project.slug}}" class="b-link-fix">
  <article  class="b-project-detail m-clinic">
    <header>
      <h2>{{project.title}}</h2>
      <h5>{{project.location}} | {% if project.status %}<span class="e-project-status">{{project.status}}</span>{% endif %}</h5>
    </header>
    <aside class="e-project-detail-aside">
      {% if project.logo %}
      <section class="e-project-logo">
        <img src="static/projects/{{project.slug}}/{{project.logo}}" alt="{{project.title}}">
      </section>
      {% endif %}
      <section>
        <h3>Authors</h3>
        {% for author in project.authors %}
          <p><a href="{{author.url}}">{{author.first_name}} {{author.last_name}}</a></p>
        {% endfor %}
      </section>
      <section>
        <h3>Resources</h3>
        <ul>
        {% for file in project.files %}
          <li class="e-project-files"><a href="static/projects/{{project.slug}}/{{file.filename}}" target="_blank">{{file.label}}</a></li>
        {% endfor %}
        </ul>
      </section>
      <section>
        <h3>Links</h3>
        {% if project.links.truonex %}<a class="e-button" href="{{project.links.truonex}}">Truonex Profile</a>{% endif %}
        {% if project.links.url %}<a class="e-button m-link" href="{{project.links.url}}">Website</a>{% endif %}
        {% if project.links.demo %}<a class="e-button m-play" href="{{project.links.demo}}">Demo</a>{% endif %}
      </section>
    </aside>
    <div class="e-project-detail-main">
      {% if project.summary %}
      <section>
        <h3>Project Summary</h3>
        <p>{{project.summary}}</p>
      </section>
      {% endif %}
      {% if project.problem_statement %}
      <section>
        <h3>Problem Statement</h3>
        <p>{{project.problem_statement}}</p>
      </section>
      {% endif %}
      {% if project.why_compelling %}
      <section>
        <h3>Why is it Compelling</h3>
        <p>{{project.why_compelling}}</p>
      </section>
      {% endif %}
    </div>
  </article>
</div>
{% endfor %}
```


## FAQ Block

FAQ block structure. 
.e-faq-trigger to add a zippy functionality to the title. This functionality toggles the class "m-active" on the .b-faqs element. Leave the .m-active class so the FAQs default is open.

```
<section class="b-faqs m-active">
  <div class="row b-content-section">
    <div class="column large-12">
      <h2 class="e-faq-trigger">Title for th section</h2>
      {# repeatable block #}
      <div class="b-faq-item">
        <p class="e-question">Question in bold</p>
        <p class="e-answer">Answer in regular text</p>
      </div>
      {# end of repeatable block #}
    </div>
  </div>
</section>
```

# Text Blocks

## Button

".e-button" - this is a mistake, button should be a b-button. .e-button can be used anywhere in the html and it will work.

".m-large" is the only modifier it has. 


## Bulleted List
```
<ul class="b-list">
   <li></li>
</ul>
```

this will generate a bulleted list, with green triangles as bullets. Standard style for a bullet list.

## Form
.b-form - this is the class for the <form> element

These are the form elements I styled.
input[type=‘text’]
button
textarea
select
