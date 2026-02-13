import React from 'react';
import type { ButtonHTMLAttributes, ReactNode } from 'react';

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  /**
   * Button visual variant
   */
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';

  /**
   * Button size
   */
  size?: 'sm' | 'md' | 'lg';

  /**
   * Shows loading spinner
   */
  isLoading?: boolean;

  /**
   * Icon element (optional)
   */
  icon?: ReactNode;

  /**
   * Icon position relative to children
   */
  iconPosition?: 'left' | 'right';

  /**
   * Button content
   */
  children: ReactNode;
}

/**
 * Accessible button component with multiple variants and states
 *
 * Features:
 * - Keyboard accessible
 * - Loading state with aria-busy
 * - Focus visible styling
 * - Disabled state management
 * - Flexible icon positioning
 *
 * @example
 * ```tsx
 * <Button variant="primary" size="md" onClick={handleClick}>
 *   Click me
 * </Button>
 * ```
 */
export function Button({
  variant = 'primary',
  size = 'md',
  isLoading = false,
  icon,
  iconPosition = 'left',
  children,
  disabled,
  className = '',
  ...rest
}: ButtonProps) {
  const baseStyles = [
    'inline-flex items-center justify-center gap-2',
    'font-medium rounded-lg',
    'transition-colors duration-200',
    'focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2',
    'disabled:opacity-50 disabled:cursor-not-allowed',
  ].join(' ');

  const variantStyles = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 focus-visible:outline-blue-600 active:bg-blue-800',
    secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300 focus-visible:outline-gray-500 active:bg-gray-400',
    ghost: 'bg-transparent hover:bg-gray-100 focus-visible:outline-gray-500 active:bg-gray-200',
    danger: 'bg-red-600 text-white hover:bg-red-700 focus-visible:outline-red-600 active:bg-red-800',
  };

  const sizeStyles = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-6 py-3 text-base',
    lg: 'px-8 py-4 text-lg',
  };

  return (
    <button
      className={`${baseStyles} ${variantStyles[variant]} ${sizeStyles[size]} ${className}`}
      disabled={disabled || isLoading}
      aria-busy={isLoading}
      {...rest}
    >
      {isLoading ? (
        <>
          <svg
            className="animate-spin h-5 w-5"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            aria-hidden="true"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            />
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            />
          </svg>
          <span>Loading...</span>
        </>
      ) : (
        <>
          {icon && iconPosition === 'left' && <span aria-hidden="true">{icon}</span>}
          {children}
          {icon && iconPosition === 'right' && <span aria-hidden="true">{icon}</span>}
        </>
      )}
    </button>
  );
}
