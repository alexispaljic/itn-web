# Institut des Transformations numériques

A web site built with [Astro](https://astro.build/) & [Astroship](https://astro.build/themes/details/astroship/).

## Live Demo

[![https://boisgera.github.io/itn-web/](https://boisgera.github.io/itn-web/ITN-preview.png)](https://boisgera.github.io/itn-web/)

## Pagespeed 

[![https://boisgera.github.io/itn-web/ITN-pagespeed.png](https://boisgera.github.io/itn-web/ITN-pagespeed.png)](https://pagespeed.web.dev/report?url=https-boisgera-github-io-itn-web)

## Installation

You can clone the project directly from this repo to your local system.

### 1. Clone the repo

```bash
git clone git@github.com:boisgera/itn-web.git
```

### 2. Install Dependencies

```bash
npm install
# or
yarn install
# or (recommended)
pnpm install
```

### 3. Start development Server

```bash
npm run dev
# or
yarn dev
# or (recommended)
pnpm dev
```

### Preview & Build

```bash
npm run preview
npm run build
# or
yarn preview
yarn build
# or (recommended)
pnpm preview
pnpm build
```

We recommend using [pnpm](https://pnpm.io/) to save disk space on your computer.

### Other Commands

```bash
pnpm astro ...
pnpm astro add
pnpm astro --help
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

## TailwindCSS

TailwindCSS is already configured in this repo, so you can start using it without any installation.
