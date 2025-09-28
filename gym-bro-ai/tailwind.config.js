/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'gym-dark': '#1a1a1a',
        'gym-orange': '#ff6b35',
        'gym-gray': '#2d2d2d',
        'gym-light': '#f5f5f5',
      },
      fontFamily: {
        'gym': ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
