import type * as React from 'react'
import type { UI } from '#components/ui'

/**
 * Props for the {{ComponentName}} component
 *
 * Extends the base UI component props to support polymorphic rendering
 * and all standard HTML attributes.
 */
export type {{ComponentName}}Props = Partial<React.ComponentProps<typeof UI>> & {
  /**
   * Content to render inside the component
   */
  children?: React.ReactNode

  /**
   * The element type to render as (polymorphic component)
   * @default 'div'
   */
  as?: React.ElementType

  /**
   * Visual variant of the component
   * @default undefined
   */
  variant?: 'primary' | 'secondary' | 'tertiary'

  /**
   * Size variant of the component
   * @default 'medium'
   */
  size?: 'small' | 'medium' | 'large'

  // TODO: Add additional component-specific props here
}
