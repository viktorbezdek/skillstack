import { render, screen } from '@testing-library/react'
import { userEvent } from '@testing-library/user-event'
import { describe, it, expect, vi } from 'vitest'
import { {{ComponentName}} } from './{{component-name}}'

describe('{{ComponentName}}', () => {
  describe('Basic Rendering', () => {
    it('renders children correctly', () => {
      render(<{{ComponentName}}>Test content</{{ComponentName}}>)
      expect(screen.getByText('Test content')).toBeInTheDocument()
    })

    it('renders with custom className', () => {
      render(
        <{{ComponentName}} data-testid="component" className="custom-class">
          Content
        </{{ComponentName}}>
      )
      const component = screen.getByTestId('component')
      expect(component).toHaveClass('custom-class')
    })

    it('renders as custom element when "as" prop is provided', () => {
      render(
        <{{ComponentName}} as="section" data-testid="component">
          Content
        </{{ComponentName}}>
      )
      const component = screen.getByTestId('component')
      expect(component.tagName.toLowerCase()).toBe('section')
    })

    it('applies custom styles when provided', () => {
      const style = { backgroundColor: 'red' }
      render(
        <{{ComponentName}} data-testid="component" styles={style}>
          Content
        </{{ComponentName}}>
      )
      const component = screen.getByTestId('component')
      expect(component).toHaveStyle(style)
    })
  })

  describe('Variants', () => {
    it('applies primary variant styling', () => {
      render(
        <{{ComponentName}} variant="primary" data-testid="component">
          Content
        </{{ComponentName}}>
      )
      const component = screen.getByTestId('component')
      expect(component).toHaveAttribute('data-{{component-name}}', 'primary')
    })

    it('applies secondary variant styling', () => {
      render(
        <{{ComponentName}} variant="secondary" data-testid="component">
          Content
        </{{ComponentName}}>
      )
      const component = screen.getByTestId('component')
      expect(component).toHaveAttribute('data-{{component-name}}', 'secondary')
    })
  })

  describe('Sizes', () => {
    it('applies small size', () => {
      render(
        <{{ComponentName}} size="small" data-testid="component">
          Content
        </{{ComponentName}}>
      )
      const component = screen.getByTestId('component')
      // Add size-specific attribute or class assertions
      expect(component).toBeInTheDocument()
    })

    it('applies large size', () => {
      render(
        <{{ComponentName}} size="large" data-testid="component">
          Content
        </{{ComponentName}}>
      )
      const component = screen.getByTestId('component')
      // Add size-specific attribute or class assertions
      expect(component).toBeInTheDocument()
    })
  })

  describe('Event Handling', () => {
    it('calls onClick handler when clicked', async () => {
      const handleClick = vi.fn()
      render(
        <{{ComponentName}} as="button" type="button" onClick={handleClick}>
          Click me
        </{{ComponentName}}>
      )

      const button = screen.getByRole('button')
      await userEvent.click(button)

      expect(handleClick).toHaveBeenCalledTimes(1)
    })

    it('handles keyboard Enter key', async () => {
      const handleClick = vi.fn()
      render(
        <{{ComponentName}} as="button" type="button" onClick={handleClick}>
          Press Enter
        </{{ComponentName}}>
      )

      const button = screen.getByRole('button')
      button.focus()
      await userEvent.keyboard('{Enter}')

      expect(handleClick).toHaveBeenCalled()
    })

    it('handles keyboard Space key', async () => {
      const handleClick = vi.fn()
      render(
        <{{ComponentName}} as="button" type="button" onClick={handleClick}>
          Press Space
        </{{ComponentName}}>
      )

      const button = screen.getByRole('button')
      button.focus()
      await userEvent.keyboard(' ')

      expect(handleClick).toHaveBeenCalled()
    })
  })

  describe('Accessibility', () => {
    it('has correct ARIA attributes', () => {
      render(
        <{{ComponentName}}
          aria-label="Test label"
          aria-describedby="description"
          data-testid="component"
        >
          Content
        </{{ComponentName}}>
      )

      const component = screen.getByTestId('component')
      expect(component).toHaveAttribute('aria-label', 'Test label')
      expect(component).toHaveAttribute('aria-describedby', 'description')
    })

    it('is focusable when interactive', async () => {
      render(
        <{{ComponentName}} as="button" type="button">
          Focusable
        </{{ComponentName}}>
      )

      const button = screen.getByRole('button')
      expect(button).not.toHaveFocus()

      await userEvent.tab()
      expect(button).toHaveFocus()
    })

    it('handles disabled state correctly', async () => {
      const handleClick = vi.fn()
      render(
        <{{ComponentName}}
          as="button"
          type="button"
          onClick={handleClick}
          aria-disabled="true"
          data-testid="component"
        >
          Disabled
        </{{ComponentName}}>
      )

      const button = screen.getByTestId('component')
      expect(button).toHaveAttribute('aria-disabled', 'true')

      // Note: Depending on implementation, disabled buttons might not call onClick
      // Adjust this test based on your actual implementation
    })
  })

  describe('Custom Props', () => {
    it('forwards data attributes', () => {
      render(
        <{{ComponentName}}
          data-testid="component"
          data-custom="value"
        >
          Content
        </{{ComponentName}}>
      )

      const component = screen.getByTestId('component')
      expect(component).toHaveAttribute('data-custom', 'value')
    })

    it('forwards ref correctly', () => {
      const ref = vi.fn()
      render(
        <{{ComponentName}} ref={ref}>
          Content
        </{{ComponentName}}>
      )

      expect(ref).toHaveBeenCalled()
    })
  })
})
