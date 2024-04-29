# Frontend Web App

This frontend web app is built using [Next.js](https://nextjs.org/), a powerful React framework for building server-rendered applications. It provides a modern and interactive user interface for interacting with the backend API.

## Overview

This frontend web app is designed to be a scalable and modular foundation for building web applications. It leverages the power of Next.js for server-side rendering, efficient client-side updates, and automatic code splitting. The app is bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app) and utilizes various Next.js features and best practices.

### Key Features

- Next.js: A React framework for server-rendered applications.
- Tailwind CSS: A utility-first CSS framework for rapid UI development.
- TypeScript: A typed superset of JavaScript for enhanced code quality.
- DaisyUI: A plugin for Tailwind CSS providing pre-designed UI components.
- Responsive Design: Built with a mobile-first approach for optimal viewing across devices.
- API Integration: Seamless communication with the backend API for data fetching and manipulation.
- Code Splitting: Optimized bundle sizes through automatic code splitting and lazy loading.
- Font Optimization: Utilizes [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) for automatic font optimization.

## Getting Started

To set up and run the frontend web app, follow these steps:

1. Navigate to the `frontend/` directory:
```cd frontend```
2. Install the dependencies:
```npm install```
or
```yarn install```
or
```pnpm install```
or
```bun install```
3. Start the development server:
```npm run dev```
or
```yarn dev```
or
```pnpm dev```
or
```bun dev```
4. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

## Folder Structure

The frontend folder structure follows the Next.js convention and is organized as follows:
```
frontend/
├── app/
│   ├── api/
│   ├── components/
│   ├── fonts/
│   ├── lib/
│   ├── styles/
│   └── page.tsx
├── public/
│   ├── favicon.ico
│   └── images/
├── next.config.js
├── package.json
├── postcss.config.js
├── README.md
├── tailwind.config.js
└── tsconfig.json
```
- The `app/` directory contains the main application code.
  - `api/`: Contains API route handlers.
  - `components/`: Contains reusable React components.
  - `fonts/`: Contains custom fonts.
  - `lib/`: Contains utility functions and libraries.
  - `styles/`: Contains global styles and Tailwind CSS configurations.
  - `page.tsx`: The main entry point of the application.
- The `public/` directory contains static assets.
- The `next.config.js` file contains Next.js configuration options.
- The `package.json` file contains project dependencies and scripts.
- The `postcss.config.js` file contains PostCSS configuration for CSS processing.
- The `README.md` file provides information and instructions for the frontend.
- The `tailwind.config.js` file contains Tailwind CSS configuration.
- The `tsconfig.json` file contains TypeScript configuration.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - Learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - An interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out the [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.