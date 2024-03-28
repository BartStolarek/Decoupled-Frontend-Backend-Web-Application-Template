/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    sassOptions: {
      includePaths: ['./src/styles'],
    },
  };
  
  export default nextConfig;