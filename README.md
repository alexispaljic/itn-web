# Institut des Transformations numériques

A web site built with [Astro](https://astro.build/) & [Astroship](https://astro.build/themes/details/astroship/).

## Live Demo

[![https://boisgera.github.io/itn-web/](https://boisgera.github.io/itn-web/ITN-preview.png)](https://boisgera.github.io/itn-web/)

## Pagespeed 

[![https://boisgera.github.io/itn-web/ITN-pagespeed.png](https://boisgera.github.io/itn-web/ITN-pagespeed.png)](https://pagespeed.web.dev/report?url=https://boisgera.github.io/itn-web/)

## Installation

You can work on the project in the cloud with use Github Codespaces.

### 1. Open the repository in Codespaces

[Create a new Codespace](https://codespaces.new/boisgera/itn-web)

Alternatively, to work locally, clone the repo:

```bash
git clone git@github.com:boisgera/itn-web.git
```

### 2. Install Dependencies

Codespace will perform this task automatically. But if you work locally, type:

```bash
npm install
```

### 3. Start development Server

```bash
npm run dev
```


## Project Structure

Inside of your Astro project, you'll see the following folders and files:

```
/
├── public/
│   └── ...
├── src/
│   ├── components/
│   │   └── ...
│   ├── layouts/
│   │   └── ...
│   └── pages/
│       └── ...
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

Any static assets, like images, can be placed in the `public/` directory.
