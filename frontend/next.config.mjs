/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: false,
    swcMinify: true,
    sassOptions: {
      includePaths: ['./src/styles'],
    },
  };
  
  export default nextConfig;