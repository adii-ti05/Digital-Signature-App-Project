import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  webpack(config: any) {
    config.resolve.alias = {
      ...config.resolve.alias,
      canvas: false,
    };
    return config;
  },
};

export default nextConfig;