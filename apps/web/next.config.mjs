//@ts-check

// eslint-disable-next-line @typescript-eslint/no-var-requires
import { composePlugins, withNx } from '@nx/next';
import createNextIntlPlugin from 'next-intl/plugin';

const withNextIntl = createNextIntlPlugin();

/** @type {import('next').NextConfig} */
const nextConfig = {
  nx: {
    // Set this to true if you would like to use SVGR
    // See: https://github.com/gregberge/svgr
    svgr: false,
  },
  eslint: {
    ignoreDuringBuilds: true,
  }
};

const plugins = [
  // Add more Next.js plugins to this list if needed.
  withNextIntl,
  withNx,
];

export default composePlugins(...plugins)(nextConfig);
