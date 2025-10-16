/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone', // For Docker optimization
  reactStrictMode: true,
  
  // Environment variables
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
    NEXT_PUBLIC_APP_NAME: process.env.NEXT_PUBLIC_APP_NAME || 'StockGenie',
  },

  // Image optimization
  images: {
    domains: ['localhost'],
  },

  // Experimental features
  experimental: {
    optimizePackageImports: ['recharts', 'lucide-react'],
  },
}

module.exports = nextConfig

