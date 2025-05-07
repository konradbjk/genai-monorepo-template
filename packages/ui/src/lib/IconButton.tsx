import React from 'react';
import { GitHubIcon } from './Icons';

// Define props for the IconButton component
interface IconButtonProps {
  icon: React.ReactNode;
  href: string;
  label?: string;
  variant?: 'primary' | 'secondary' | 'tertiary';
  size?: 'small' | 'medium' | 'large';
  className?: string;
  target?: '_blank' | '_self';
  rel?: string;
}

/**
 * IconButton component that displays an icon with an optional label
 * and links to the provided href
 */
export const IconButton = ({
  icon,
  href,
  label,
  variant = 'primary',
  size = 'medium',
  className = '',
  target = '_blank',
  rel = 'noopener noreferrer',
}: IconButtonProps) => {
  // Determine styles based on variant and size
  const variantStyles = {
    primary: 'bg-blue-500 hover:bg-blue-600 text-white',
    secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-800',
    tertiary: 'bg-transparent hover:bg-gray-100 text-gray-700',
  };

  const sizeStyles = {
    small: 'p-1 text-sm',
    medium: 'p-2',
    large: 'p-3 text-lg',
  };

  return (
    <a
      href={href}
      target={target}
      rel={rel}
      className={`flex items-center justify-center rounded-full transition-colors duration-200 ${variantStyles[variant]} ${sizeStyles[size]} ${className}`}
    >
      <span className="flex items-center justify-center">
        {icon}
      </span>
      {label && <span className="ml-2">{label}</span>}
    </a>
  );
};

export const GitHubButton = ({ href, label }: { href: string, label: string }) => (
  <IconButton
    icon={<GitHubIcon />}
    href={href}
    label={label}
  />
);
