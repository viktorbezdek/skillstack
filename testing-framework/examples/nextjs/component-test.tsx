import { describe, it, expect, vi } from 'vitest'
import { render, screen, within } from '@testing-library/react'
import { userEvent } from '@testing-library/user-event'
import { axe, toHaveNoViolations } from 'jest-axe'

expect.extend(toHaveNoViolations)

/**
 * Example component test demonstrating RTL best practices
 * with accessibility testing via axe-core
 */

// Example component
interface EntityCardProps {
  entity: {
    id: string
    name: string
    type: string
    description?: string
  }
  onEdit?: (id: string) => void
  onDelete?: (id: string) => void
}

function EntityCard({ entity, onEdit, onDelete }: EntityCardProps) {
  return (
    <article aria-label={`Entity: ${entity.name}`}>
      <header>
        <h2>{entity.name}</h2>
        <span className="badge">{entity.type}</span>
      </header>
      {entity.description && <p>{entity.description}</p>}
      <footer>
        {onEdit && (
          <button onClick={() => onEdit(entity.id)} aria-label={`Edit ${entity.name}`}>
            Edit
          </button>
        )}
        {onDelete && (
          <button onClick={() => onDelete(entity.id)} aria-label={`Delete ${entity.name}`}>
            Delete
          </button>
        )}
      </footer>
    </article>
  )
}

describe('EntityCard', () => {
  const mockEntity = {
    id: '1',
    name: 'Test Character',
    type: 'character',
    description: 'A brave adventurer'
  }

  it('renders entity information', () => {
    render(<EntityCard entity={mockEntity} />)

    expect(screen.getByRole('heading', { name: 'Test Character' })).toBeInTheDocument()
    expect(screen.getByText('character')).toBeInTheDocument()
    expect(screen.getByText('A brave adventurer')).toBeInTheDocument()
  })

  it('does not render description when not provided', () => {
    const entityWithoutDesc = { ...mockEntity, description: undefined }
    render(<EntityCard entity={entityWithoutDesc} />)

    expect(screen.queryByText('A brave adventurer')).not.toBeInTheDocument()
  })

  it('calls onEdit when edit button is clicked', async () => {
    const user = userEvent.setup()
    const onEdit = vi.fn()

    render(<EntityCard entity={mockEntity} onEdit={onEdit} />)

    await user.click(screen.getByRole('button', { name: /edit test character/i }))

    expect(onEdit).toHaveBeenCalledTimes(1)
    expect(onEdit).toHaveBeenCalledWith('1')
  })

  it('calls onDelete when delete button is clicked', async () => {
    const user = userEvent.setup()
    const onDelete = vi.fn()

    render(<EntityCard entity={mockEntity} onDelete={onDelete} />)

    await user.click(screen.getByRole('button', { name: /delete test character/i }))

    expect(onDelete).toHaveBeenCalledTimes(1)
    expect(onDelete).toHaveBeenCalledWith('1')
  })

  it('does not render action buttons when handlers not provided', () => {
    render(<EntityCard entity={mockEntity} />)

    expect(screen.queryByRole('button', { name: /edit/i })).not.toBeInTheDocument()
    expect(screen.queryByRole('button', { name: /delete/i })).not.toBeInTheDocument()
  })

  it('has accessible structure', () => {
    render(<EntityCard entity={mockEntity} onEdit={vi.fn()} onDelete={vi.fn()} />)

    const article = screen.getByRole('article', { name: /entity: test character/i })
    expect(article).toBeInTheDocument()

    // Check heading hierarchy
    const heading = within(article).getByRole('heading', { level: 2 })
    expect(heading).toHaveTextContent('Test Character')

    // Check buttons have accessible names
    const editButton = within(article).getByRole('button', { name: /edit test character/i })
    const deleteButton = within(article).getByRole('button', { name: /delete test character/i })
    expect(editButton).toBeInTheDocument()
    expect(deleteButton).toBeInTheDocument()
  })

  it('has no accessibility violations', async () => {
    const { container } = render(
      <EntityCard entity={mockEntity} onEdit={vi.fn()} onDelete={vi.fn()} />
    )

    const results = await axe(container)
    expect(results).toHaveNoViolations()
  })
})
