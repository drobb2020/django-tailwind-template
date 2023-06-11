<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/drobb2020/django-tailwind-template">
    <img src="dj_tw_template/static/assets/logo.png" alt="Logo" height="100">
  </a>

<h3 align="center">django-tailwind-template</h3>

  <p align="center">
    This is a basic template to integrate tailwindcss with Django instead of using the tailwind cdn, which is not recommended for a production deployment.
    <br />
    <a href="https://github.com/drobb2020/django-tailwind-template/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/drobb2020/django-tailwind-template">View Demo</a>
    ·
    <a href="https://github.com/drobb2020/django-tailwind-template/issues">Report Bug</a>
    ·
    <a href="https://github.com/drobb2020/django-tailwind-template/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `drobb2020`, `django-tailwind-template`, `twitter_handle`, `linkedin_username`, `email`, `email_client`, `django-tailwind-template`, `project_description`

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Django](https://www.djangoproject.com/)
- [npm](https://www.npmjs.com/)
- [Tailwindcss](https://tailwindcss.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is a self contained template for Django 4.2.2, and Tailwindcss 3.3.2. It also includes additional packages I use with every Django project (flake8, black, ruff, and django-extensions).

### Prerequisites

You will need to have node.js installed on your system to build this project. Go to [npmjs](https://www.npmjs.com/) to download and install the latest node.js version. This project was created with node v19.6.0
You will also need Python installed on your system. Go to [python](https://www.python.org) to download and install the latest python version. This project was created with python v3.11.1.

There are two ways to get started with this project:

1. Build by following the <a href="#instructions">instructions</a>
2. Build by cloning this repo

### Instructions

#### Install and Configure a Django Project/Application

You can build this project yourself by doing the following steps:

1. Make sure you have Python and Node.js installed on your system.
2. Create a top-level folder to hold this project.
3. Change into the folder you created and start with creating a python virtual environment.
   1. python3 -m venv venv, you can use any name for the virtual environment, I always use venv.
4. Activate the virtual environment using:

   ```sh
   source venv/bin/activate
   or
   venv\Scripts\Activate
   ```

5. Run the following command to install Django and the supporting modules:

   ```sh
   pip install Django django-extensions flake8 flake8-django black ruff
   ```

6. Create a new Django project:

   ```sh
   django-admin startproject <your_project_name>
   ```

7. Now create a new Django application:

   ```sh
   python manage.py startapp core
   ```

8. Go into your project's settings.py and make the following changes to INSTALLED_APPS:

   ```sh
    ...
    # Applications
    'core.apps.CoreConfig',
    # Modules
    'django_extensions',
   ```

9. Still in settings.py, go down to TEMPLATES and add the path to the templates folder:

    ```sh
    'DIRS': [BASE_DIR / 'templates'],
    ```

10. Go down to the static files section of settings.py and add the following lines below the STATIC_URL entry:

    ```sh
    STATICFILES_DIRS = [BASE_DIR / 'static']
    STATIC_ROOT = BASE_DIR.parent / 'cdn' / 'static'
    ```

11. In the django project folder create a static folder, and a templates folder.
12. under the static folder I typically create these folders:
    1. assets - holds static images and the favicon
    2. css - holds the css file for the project
    3. js - holds the javascript file for the project
    4. src - holds the main.css file for tailwindcss
13. Copy your favicon.ico file the the assets folder (can be a png, or svg - your choice)
14. Create a file named custom.min.css in the css folder (or whatever name you prefer)
15. Create a file named main.js in the js folder (or whatever name you prefer)
16. In the src folder create a file named main.css, or use any name you want. Put the following content in this file:

    ```sh
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

17. Go back up to the parent folder of the project and create the folder cdn, and inside that a static folder.
18. Back in the django project open the urls.py file, and add the following to configure static files:

    ``` sh
    from django.conf import settings
    ...
    # Add below urlpatterns
    if settings.DEBUG:
        from django.conf.urls.static import static
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```

19. Under templates create a base.html file, add the basic html boilerplate to the file and don't forget to put {% load static %} at the top of the file.
20. Add links for favicon, css, and javascript using the static tag to denote the location of the files
21. In the core application open views.py and create the following function:

    ```sh
    def index(request):
        context = {}
        return render(request, 'core/index.html', context)
    ```

22. In the templates folder create a new directory named core, and inside the core folder create index.html. Add the following code to this file.

    ```sh
    {% extends 'base.html' %}
    {% block content %}

    <div class="flex flex-col justify-center items-center h-screen bg-rose-700">
      <h1 class="text-6xl font-bold text-white">Django + Tailwindcss Template</h1>
      <p class="text-xl">Your text here...</p>
    </div>
    {% endblock content %}

{% endblock content %}
23. In the core folder create a new file named urls.py, and add the following code:

   ```sh
    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
   ```

24. In the project urls.py file add the following code:

   ```sh
    from django.urls import include, ...

    urlpatterns = [
        ...
        path('', include('core.urls')),
    ]
   ```

25. At this point you can either run the server (python manage.py runserver) or you can run the initial migrate (python manage.py migrate).

#### Install & Configure Tailwindcss

1. In the root folder of the project run the following command to install tailwindcss:

  ```sh
  npm install tailwindcss postcss postcss-cli autoprefixer cssnano
  ```

2. This will create a new folder named node_modules, and two files package.json, and package-lock.json
3. At the command line run the following command:

  ```sh
  npx tailwindcss init
  ```

4. This will create a new file named tailwind.config.js
5. Inside tailwind.config.js, add the following code to the components section:

   ```sh
   "./dj_tw_template/**/*.{html,js}"
   ```

6. Manually create a postcss.config.js file, and add the following code:

  ```sh
  module.exports = {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
      cssnano: {},
    },
  }
  ```

7. Go to packages.json and add a scripts section so you can run postcss and compile the tailwindcss output css file:

   ```sh
   "scripts": {
      "dev": "postcss ./dj_tw_template/static/src/main.css -o ./dj_tw_template/static/css/custom.min.css --watch",
      "build": "postcss ./dj_tw_template/static/src/main.css -o ./dj_tw_template/static/css/custom.min.css"
    },
   ```

8. To execute the scripts, use either `npm run dev` or `npm run build`
9. You can now customize the tailwind code in either base.html or in index.html. For pre-coded examples for a navbar, footer, table or card, go to flowbite.com for some good inspiration.

### Cloning this Repository

If you don't want to do all the work yourself, you are free to clone this repository and start customizing this code for your own project.

```sh
git clone https://github.com/drobb/django-tailwind-template.git
```

In the dj_tw-template folder don't forget to create and activate a virtual environment. Once that is done run `pip install -r requirements.txt`

In the root of the cloned repository run the command `npm install`, this will download all the necessary packages to run the project.

You should be able to run both the django project, and the tailwind dev or build script (in separate terminal windows) and play with the project.

Happy coding!

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

This is intended as starter code for tailwindcss, and not necessarily for Django (although it could be used as Django starter code). I have left this basic enough that you can change any of the names and still end up with a functioning tailwindcss+Django project.

_For more examples, please refer to the [Documentation](https://github.com/drobb2020/django-tailwind-template/wiki)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/drobb2020/django-tailwind-template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Your Name - [@DavidRobb2](https://twitter.com/DavidRobb2) - drobb2011@gmail.com

Project Link: [https://github.com/drobb2020/django-tailwind-template](https://github.com/drobb2020/django-tailwind-template)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/drobb2020/django-tailwind-template.svg?style=for-the-badge
[contributors-url]: https://github.com/drobb2020/django-tailwind-template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/drobb2020/django-tailwind-template.svg?style=for-the-badge
[forks-url]: https://github.com/drobb2020/django-tailwind-template/network/members
[stars-shield]: https://img.shields.io/github/stars/drobb2020/django-tailwind-template.svg?style=for-the-badge
[stars-url]: https://github.com/drobb2020/django-tailwind-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/drobb2020/django-tailwind-template.svg?style=for-the-badge
[issues-url]: https://github.com/drobb2020/django-tailwind-template/issues
[license-shield]: https://img.shields.io/github/license/drobb2020/django-tailwind-template.svg?style=for-the-badge
[license-url]: https://github.com/drobb2020/django-tailwind-template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/david-robb-42436a20/
[product-screenshot]: static/assets/screenshot.png
