import * as React from 'react'
// IMPORT_BASE_COMPONENT_PLACEHOLDER
// Import the existing component you're extending
// Example: import { Alert, type AlertProps } from '../alert/alert'
import type { {{ComponentName}}Props } from './{{component-name}}.types'

/**
 * {{ComponentName}} Component - Extended Version
 *
 * This component extends an existing fpkit component with additional features or variants.
 *
 * **Extension Strategy:**
 * Instead of duplicating code, this extends BASE_COMPONENT_PLACEHOLDER with:
 * - Additional variants
 * - Enhanced functionality
 * - New props or behaviors
 *
 * **Base Component:** BASE_COMPONENT_PLACEHOLDER
 *
 * **What's New:**
 * - NEW_FEATURE_1_PLACEHOLDER
 * - NEW_FEATURE_2_PLACEHOLDER
 * - NEW_FEATURE_3_PLACEHOLDER
 *
 * **Usage:**
 * ```tsx
 * <{{ComponentName}} newProp="value">
 *   Content here
 * </{{ComponentName}}>
 * ```
 *
 * **When to Extend vs Create New:**
 * ✅ Extend if:
 *    - Adding variant to existing component
 *    - Enhancing behavior without breaking changes
 *    - Sharing most of the base component's logic
 *
 * ❌ Create new if:
 *    - Completely different use case
 *    - Would require significant prop/API changes
 *    - Breaks the base component's contract
 *
 * **Accessibility:**
 * - Inherits base component's accessibility features
 * - Ensures new features maintain WCAG 2.1 AA compliance
 *
 * @component
 * @example
 * ```tsx
 * <{{ComponentName}} variant="enhanced">
 *   Enhanced content
 * </{{ComponentName}}>
 * ```
 */
export const {{ComponentName}} = ({
  children,
  // Add new props here
  // ...existing base component props
  ...props
}: {{ComponentName}}Props) => {
  // EXTENSION_LOGIC_PLACEHOLDER
  // Add your extension logic here

  // Option 1: Wrap the base component with additional functionality
  // return (
  //   <div data-{{component-name}}-wrapper>
  //     <BaseComponent {...props}>
  //       {/* Add enhancements here */}
  //       {children}
  //     </BaseComponent>
  //   </div>
  // )

  // Option 2: Enhance props before passing to base component
  // const enhancedProps = {
  //   ...props,
  //   // Add enhancements
  // }
  // return <BaseComponent {...enhancedProps}>{children}</BaseComponent>

  // Option 3: Conditional rendering with base component
  // if (someCondition) {
  //   return <BaseComponent {...props}>{children}</BaseComponent>
  // }
  // return <EnhancedVersion {...props}>{children}</EnhancedVersion>

  return (
    <div data-{{component-name}} {...props}>
      {/* TODO: Replace with actual extension implementation */}
      {children}
    </div>
  )
}

{{ComponentName}}.displayName = '{{ComponentName}}'

// Export both component and props type
export { type {{ComponentName}}Props } from './{{component-name}}.types'

/**
 * EXTENSION GUIDELINES:
 *
 * 1. **Maintain backward compatibility**
 *    - Don't break existing base component API
 *    - Make new props optional when possible
 *
 * 2. **Reuse base component styles**
 *    - Import base SCSS: @use '../base-component/base-component'
 *    - Only add CSS for new features/variants
 *
 * 3. **Enhance, don't duplicate**
 *    - Call base component's logic where possible
 *    - Add minimal custom code for new features
 *
 * 4. **Document the relationship**
 *    - Clearly state what's inherited from base
 *    - Document what's new/different
 *    - Explain when to use extended vs base version
 *
 * 5. **Consider contributing back**
 *    - If extension is widely useful, consider adding to base component
 *    - Propose variant instead of separate component
 */
