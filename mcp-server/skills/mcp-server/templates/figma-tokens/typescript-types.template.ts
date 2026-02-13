/**
 * Design Tokens - TypeScript Type Definitions
 * Generated from Figma design variables
 */

// Color Tokens
export type ColorTokens = {
  primary: '#0066cc';
  secondary: '#6c757d';
  success: '#28a745';
  error: '#dc3545';
  warning: '#ffc107';
  info: '#17a2b8';
};

// Spacing Tokens
export type SpacingTokens = {
  xs: '4px';
  sm: '8px';
  md: '16px';
  lg: '24px';
  xl: '32px';
};

// Typography Tokens
export type FontFamilyTokens = {
  body: 'Inter, system-ui, sans-serif';
  heading: 'Helvetica Neue, Helvetica, Arial, sans-serif';
  monospace: 'Monaco, Consolas, monospace';
};

export type FontSizeTokens = {
  xs: '12px';
  sm: '14px';
  md: '16px';
  lg: '18px';
  xl: '20px';
  '2xl': '24px';
  '3xl': '30px';
  '4xl': '36px';
};

export type FontWeightTokens = {
  normal: 400;
  medium: 500;
  semibold: 600;
  bold: 700;
};

export type LineHeightTokens = {
  tight: 1.25;
  normal: 1.5;
  relaxed: 1.75;
};

// Shadow Tokens
export type ShadowTokens = {
  sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)';
  md: '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
  lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1)';
};

// Border Radius Tokens
export type BorderRadiusTokens = {
  sm: '4px';
  md: '8px';
  lg: '12px';
  full: '9999px';
};

// Animation Tokens
export type DurationTokens = {
  fast: '150ms';
  normal: '300ms';
  slow: '500ms';
};

export type EasingTokens = {
  easeIn: 'cubic-bezier(0.42, 0, 1, 1)';
  easeOut: 'cubic-bezier(0, 0, 0.58, 1)';
  easeInOut: 'cubic-bezier(0.42, 0, 0.58, 1)';
};

// Complete Tokens Object
export const tokens = {
  color: {
    primary: '#0066cc',
    secondary: '#6c757d',
    success: '#28a745',
    error: '#dc3545',
    warning: '#ffc107',
    info: '#17a2b8',
  },
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px',
  },
  typography: {
    fontFamily: {
      body: 'Inter, system-ui, sans-serif',
      heading: 'Helvetica Neue, Helvetica, Arial, sans-serif',
      monospace: 'Monaco, Consolas, monospace',
    },
    fontSize: {
      xs: '12px',
      sm: '14px',
      md: '16px',
      lg: '18px',
      xl: '20px',
      '2xl': '24px',
      '3xl': '30px',
      '4xl': '36px',
    },
    fontWeight: {
      normal: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    },
    lineHeight: {
      tight: 1.25,
      normal: 1.5,
      relaxed: 1.75,
    },
  },
  shadow: {
    sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
    md: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
    lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
  },
  borderRadius: {
    sm: '4px',
    md: '8px',
    lg: '12px',
    full: '9999px',
  },
  animation: {
    duration: {
      fast: '150ms',
      normal: '300ms',
      slow: '500ms',
    },
    easing: {
      easeIn: 'cubic-bezier(0.42, 0, 1, 1)',
      easeOut: 'cubic-bezier(0, 0, 0.58, 1)',
      easeInOut: 'cubic-bezier(0.42, 0, 0.58, 1)',
    },
  },
} as const;

// Type-safe token access
export type Tokens = typeof tokens;

// Example Usage:
//
// import { tokens, type ColorTokens } from './tokens';
//
// const buttonStyles: React.CSSProperties = {
//   backgroundColor: tokens.color.primary,
//   padding: tokens.spacing.md,
//   fontSize: tokens.typography.fontSize.md,
//   fontWeight: tokens.typography.fontWeight.medium,
//   borderRadius: tokens.borderRadius.md,
//   boxShadow: tokens.shadow.sm,
//   transition: `all ${tokens.animation.duration.normal} ${tokens.animation.easing.easeInOut}`,
// };
//
// function getPrimaryColor(): ColorTokens['primary'] {
//   return tokens.color.primary;
// }
