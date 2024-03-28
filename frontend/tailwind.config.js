/** @type {import('tailwindcss').Config} */
const myColors = {
  text: 'rgb(8, 28, 24)', // Should contrast well with background (between black and white)
  background: 'rgb(243, 255, 252)', // Sets the tone, should not compete with content. Neutral and not distracting
  primary: 'rgb(72, 203, 171)', // For main interactive elements, like primary buttons, links, active states, or things you want drawn to
  secondary: 'rgb(152, 159, 226)', // Elements that are not the main focus but still need emphasis
  accent: 'rgb(130, 96, 210)', // Vibrant and used sparingly to draw attention
  neutral: "rgb(8, 28, 24, 0.15)", // Useful for borders, shadows, disabled states, suggest to just do 0.15 opacity of text color
  info: "#48a4cb",
  success: "#96D05D",
  warning: "#EDB95E", 
  error: "#E2363F",
};

module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
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
    require('@tailwindcss/forms'),
  ],
};