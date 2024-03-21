/** @type {import('tailwindcss').Config} */

const myColors = {
  text: 'rgb(8, 28, 24)', // Usually best to have a monochrome (black to white)
  background: 'rgb(243, 255, 252)',
  primary: 'rgb(72, 203, 171)',
  secondary: 'rgb(152, 159, 226)',
  accent: 'rgb(130, 96, 210)',
  neutral: "rgb(8, 28, 24, 0.15)", // 15% opacity of text is usually good for neutral
  info: "#48a4cb",
  success: "#96D05D",
  warning: "#EDB95E", 
  error: "#E2363F",
};

module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
  ],
  daisyui: {
    themes: [
      {
        mytheme: { ...myColors },
      },
    ],
  },
  theme: {
    extend: {
      colors: myColors,
      backgroundImage: {
        'linear-primary-secondary': `linear-gradient(${myColors.primary}, ${myColors.secondary})`,
        'linear-primary-accent': `linear-gradient(${myColors.primary}, ${myColors.accent})`,
        'linear-secondary-accent': `linear-gradient(${myColors.secondary}, ${myColors.accent})`,
        'radial-primary-secondary': `radial-gradient(circle, ${myColors.primary}, ${myColors.secondary})`,
        'radial-primary-accent': `radial-gradient(circle, ${myColors.primary}, ${myColors.accent})`,
        'radial-secondary-accent': `radial-gradient(circle, ${myColors.secondary}, ${myColors.accent})`,
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"),
    require('daisyui'),
  ],
};
