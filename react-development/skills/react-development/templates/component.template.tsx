import * as React from 'react'
import { UI } from '#components/ui'
import type { {{ComponentName}}Props } from './{{component-name}}.types'

/**
 * {{ComponentName}} component
 *
 * A flexible component that [describe what the component does].
 *
 * ## Features
 * - [Key feature 1]
 * - [Key feature 2]
 * - Fully accessible (WCAG 2.1 Level AA)
 * - Keyboard navigable
 * - Customizable via CSS variables
 *
 * ## Usage
 *
 * @example
 * ```tsx
 * <{{ComponentName}}>
 *   Content goes here
 * </{{ComponentName}}>
 * ```
 *
 * @example With variant
 * ```tsx
 * <{{ComponentName}} variant="primary">
 *   Content
 * </{{ComponentName}}>
 * ```
 *
 * ## Styling
 *
 * Customize appearance using CSS variables:
 * - `--{{component-name}}-bg`: Background color
 * - `--{{component-name}}-color`: Text color
 * - `--{{component-name}}-padding`: Padding
 * - `--{{component-name}}-radius`: Border radius
 *
 * @example Custom styles
 * ```tsx
 * <{{ComponentName}}
 *   style={{
 *     '--{{component-name}}-bg': '#f0f0f0',
 *     '--{{component-name}}-padding': '1.5rem',
 *   }}
 * >
 *   Content
 * </{{ComponentName}}>
 * ```
 *
 * ## Accessibility
 *
 * - Uses semantic HTML elements
 * - Keyboard accessible (Tab, Enter, Space where applicable)
 * - Screen reader compatible
 * - Proper ARIA attributes
 * - Focus management
 *
 * @see {@link https://www.w3.org/WAI/ARIA/apg/ WAI-ARIA Authoring Practices Guide}
 * @see {@link https://www.w3.org/WAI/WCAG21/quickref/ WCAG 2.1 Quick Reference}
 */
export const {{ComponentName}} = ({
  children,
  as = 'div',
  variant,
  ...props
}: {{ComponentName}}Props) => {
  // Add component logic here

  return (
    <UI
      as={as}
      data-{{component-name}}={variant}
      {...props}
    >
      {children}
    </UI>
  )
}

{{ComponentName}}.displayName = '{{ComponentName}}'

// TODO: Remove this export and move types to separate file if component becomes complex
export type { {{ComponentName}}Props }
